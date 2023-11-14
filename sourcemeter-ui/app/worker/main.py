import time
from kafka import KafkaConsumer
import docker

from ..constants import KAFKA_HOST, KAFKA_PORT
from ..models.task import Task, TaskStatus
from ..dependencies import get_db

consumer = KafkaConsumer('tasks', group_id='worker',
                         bootstrap_servers=f'{KAFKA_HOST}:{KAFKA_PORT}')
docker_client = docker.from_env()

if __name__ == "__main__":
    print("Worker started")
    for msg in consumer:
        consumer.commit()
        task_id = int(msg.value.decode())
        print(f"New task {task_id}")
        for db in get_db():
            task: Task = db.get(Task, task_id)
            task.status = TaskStatus.in_progress
            db.commit()

            try:
                docker_client.containers.run(
                    "amoriodi/sourcemeter",
                    task.repo_url,
                    remove=True,
                    platform="linux/x86_64",
                    volumes={
                        "sourcemeter-ui_reports": {
                            "bind": "/results",
                            "mode": "rw",
                        }
                    },
                )

                task.status = TaskStatus.success
                db.commit()
            except Exception as e:
                print(e)
                task.status = TaskStatus.failure
                db.commit()
