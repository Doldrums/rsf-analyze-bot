# ToolDescription
## Default
### ID=MET

## java
### Description
  Source code metrics are used to quantify different source code characteristics. FrontEndART SourceMeter computes source code metrics for the following source code element kinds: components (e.g. archives), source files, packages, class types (including classes, interfaces, enums and annotations) and methods.

  Note that in the **free version** the following 26 metrics are not available (these metrics will get the value 0): HCPL, HDIF, HEFF, HNDB, HPL, HPV, HTRP, HVOL, MIMS, MI, MISEI, MISM, NL, NLE, CD, TCD, NII, CBOI, NA, NLA, NPA, NLPA, TNA, TNLA, TNPA, TNLPA

## cpp
### Description
  Source code metrics are used to quantify different source code characteristics. FrontEndART SourceMeter computes source code metrics for the following source code element kinds: components (e.g. executables), source files, namespaces, class types (including classes, structures, unions, interfaces, and enums), methods, and functions. Interfaces are defined as classes or structures that have only pure virtual functions and no data members.

  Note that in the **free version** the following 26 metrics are not available (these metrics will get the value 0): HCPL, HDIF, HEFF, HNDB, HPL, HPV, HTRP, HVOL, MIMS, MI, MISEI, MISM, NL, NLE, CD, TCD, NII, CBOI, NA, NLA, NPA, NLPA, TNA, TNLA, TNPA, TNLPA

## python
### Description
  Source code metrics are used to quantify different source code characteristics. SourceMeter computes source code metrics for the following source code element kinds: components (e.g. modules), source files, packages, class types, methods and functions.

  Note that in the **free version** the following 10 metrics are not available (these metrics will get the value 0): NL, NLE, CD, TCD, NII, CBOI, NA, NLA, TNA, TNLA

## javascript
### Description
  Source code metrics are used to quantify different source code characteristics. FrontEndART SourceMeter computes source code metrics for the following source code element kinds: components, source files, classes, methods and functions.

  Note that in the **free version** the following 4 metrics are not available (these metrics will get the value 0): NL, NLE, CD, TCD

## csharp
### Description
  Source code metrics are used to quantify different source code characteristics. FrontEndART SourceMeter computes source code metrics for the following source code element kinds: components (e.g. C# assemblies), source files, namespaces, types (including classes, interfaces, enums and structures) and methods.

  Note that in the **free version** the following 14 metrics are not available (these metrics will get the value 0): NL, NLE, CD, TCD, NII, CBOI, NA, NLA, NPA, NLPA, TNA, TNLA, TNPA, TNLPA

# Includes
- general_metadata.md

# Metrics
## AD
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=API Documentation
#### Tags
- /general/Documentation
- /internal/csv_column
- /internal/metric_group/Documentation
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** ratio of the number of documented public methods in the class +1 if the class itself is documented to the number of all public methods in the class + 1 (the class itself); however, the nested, anonymous, and local classes are not included.

  **Enum:** ratio of the number of documented enumerators in the enum +1 if the enum itself is documented to the number of all enumerators in the enum + 1 (the enum itself).

  **Namespace:** ratio of the number of documented public classes and methods in the namespace to the number of all of its public classes and methods; however, the classes and methods of its subnamespaces are not included.
#### Calculated
- Class
- Enum
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** ratio of the number of documented public methods in the class +1 if the class itself is documented to the number of all public methods in the class + 1 (the class itself); however, the nested and anonymous classes are not included.

  **Namespace:** ratio of the number of documented public classes and methods in the namespace to the number of all of its public classes and methods; however, the classes and methods of its subnamespaces are not included.

#### Calculated
- Class
- Enum
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** ratio of the number of documented public methods in the class +1 if the class itself is documented to the number of all public methods in the class + 1 (the class itself); however, the nested, anonymous, and local classes are not included.

  **Package:** ratio of the number of documented public classes and methods in the package to the number of all of its public classes and methods; however, the classes and methods of its subpackages are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** ratio of the number of documented methods in the class +1 if the class itself is documented to the number of all methods in the class + 1 (the class itself).

#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class
- Module
- Package


## CBO
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Coupling Between Object classes
#### Tags
- /general/Coupling
- /internal/csv_column
- /internal/metric_group/Coupling
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of directly used other classes (e.g. by inheritance, function call, type reference, attribute reference). Classes using many other classes highly depend on their environment, so it is difficult to test or reuse them; furthermore, they are very sensitive to the changes in the system.

#### Calculated
- Class
- Interface
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of directly used other classes (e.g. by inheritance, function call, type reference, attribute reference). Classes using many other classes highly depend on their environment, so it is difficult to test or reuse them; furthermore, they are very sensitive to the changes in the system.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of directly used other classes (e.g. by inheritance, function call, type reference, attribute reference). Classes using many other classes highly depend on their environment, so it is difficult to test or reuse them; furthermore, they are very sensitive to the changes in the system.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Class:** number of directly used other classes (e.g. by inheritance, function call, type reference, attribute reference). Classes using many other classes highly depend on their environment, so it is difficult to test or reuse them; furthermore, they are very sensitive to the changes in the system.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of directly used other classes (e.g. by inheritance, function call, type reference, attribute reference). Classes using many other classes highly depend on their environment, so it is difficult to test or reuse them; furthermore, they are very sensitive to the changes in the system.

#### Calculated
- Class


## CBOI
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Coupling Between Object classes Inverse
#### Tags
- /general/Coupling
- /internal/csv_column
- /internal/metric_group/Coupling
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of other classes, which directly use the class. Classes which are used by many other classes have a high impact on the behavior of the system, and should be modified very carefully and tested intensively.

#### Calculated
- Class
- Interface
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of other classes, which directly use the class. Classes which are used by many other classes have a high impact on the behavior of the system, and should be modified very carefully and tested intensively.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of other classes, which directly use the class. Classes which are used by many other classes have a high impact on the behavior of the system, and should be modified very carefully and tested intensively.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Class:** number of other classes, which directly use the class. Classes which are used by many other classes have a high impact on the behavior of the system, and should be modified very carefully and tested intensively.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of other classes, which directly use the class. Classes which are used by many other classes have a high impact on the behavior of the system, and should be modified very carefully and tested intensively.

#### Calculated
- Class


## CD
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Comment Density
#### Tags
- /general/Documentation
- /internal/csv_column
- /internal/metric_group/Documentation
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** ratio of the comment lines of the method (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

  **Class, Structure, Union:** ratio of the comment lines of the class (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

  **Namespace:** ratio of the comment lines of the namespace (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

#### Calculated
- Class
- Function
- Method
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** ratio of the comment lines of the method (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

  **Class, Structure:** ratio of the comment lines of the class (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

  **Namespace:** ratio of the comment lines of the namespace (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

#### Calculated
- Class
- Delegate
- Method
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** ratio of the comment lines of the method (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

  **Class**: ratio of the comment lines of the class (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

  **Package:** ratio of the comment lines of the package (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Method
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** ratio of the comment lines of the method/function (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

  **Class:** ratio of the comment lines of the class (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

#### Calculated
- Class
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method/Function:** ratio of the comment lines of the method/function (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

  **Class:** ratio of the comment lines of the class (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

  **Module:** ratio of the comment lines of the module (CLOC) to the sum of its comment (CLOC) and logical lines of code (LLOC).

#### Calculated
- Class
- Function
- Method
- Module
- Package


## CLOC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Comment Lines of Code
#### Tags
- /general/Documentation
- /internal/csv_column
- /internal/metric_group/Documentation
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of comment and documentation code lines of the method; however, its anonymous and local classes are not included.

  **Class, Structure, Union, Interface:** number of comment and documentation code lines of the class, including its local methods and attributes; however, its nested, anonymous, and local classes are not included.

  **Namespace:** number of comment and documentation code lines of the namespace; however, its subnamespaces are not included.

  **File:** number of comment and documentation code lines of the file.

#### Calculated
- Class
- File
- Function
- Interface
- Method
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of comment and documentation code lines of the method; however, its anonymous classes are not included.

  **Class, Structure:** number of comment and documentation code lines of the class, including its local methods and attributes; however, its nested and anonymous classes are not included.

  **Namespace:** number of comment and documentation code lines of the namespace; however, its subnamespaces are not included.

#### Calculated
- Class
- Delegate
- File
- Interface
- Method
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method**: number of comment and documentation code lines of the method; however, its anonymous and local classes are not included.

  **Class:** number of comment and documentation code lines of the class, including its local methods and attributes; however, its nested, anonymous, and local classes are not included.

  **File:** number of comment and documentation code lines of the file.

  **Package:** number of comment and documentation code lines of the package; however, its subpackages are not included.

#### Calculated
- Annotation
- Class
- Enum
- File
- Interface
- Method
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of comment and documentation code lines of the method/function; however, its anonymous and local classes are not included.

  **Class:** number of comment and documentation code lines of the class, including its local methods and attributes; however, its nested, anonymous, and local classes are not included.

  **File:** number of comment and documentation code lines of the file.

#### Calculated
- Class
- File
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method/Function:** number of comment and documentation code lines of the method/function; however, its local classes are not included.

  **Class:** number of comment and documentation code lines of the class, including its local methods and attributes; however, its nested and local classes are not included.

  **Module:** number of comment and documentation code lines of the module.

  **File:** number of comment and documentation code lines in the file.

#### Calculated
- Class
- File
- Function
- Method
- Module
- Package





## DIT
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Depth of Inheritance Tree
#### Tags
- /general/Inheritance
- /internal/csv_column
- /internal/metric_group/Inheritance
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** length of the path that leads from the class to its farthest ancestor in the inheritance tree.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** length of the path that leads from the class to its farthest ancestor in the inheritance tree.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** length of the path that leads from the class to its farthest ancestor in the inheritance tree.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** length of the path that leads from the class to its farthest ancestor in the inheritance tree.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** length of the path that leads from the class to its farthest ancestor in the inheritance tree.

#### Calculated
- Class


## DLOC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Documentation Lines of Code
#### Tags
- /general/Documentation
- /internal/csv_column
- /internal/metric_group/Documentation
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of documentation code lines of the method.

  **Class, Structure, Union, Interface:** number of documentation code lines of the class, including its local methods and attributes; however, its nested, anonymous, and local classes are not included.

  **Enum:** number of documentation code lines of the enum, including its enumerators.

#### Calculated
- Class
- Enum
- Function
- Interface
- Method
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of documentation code lines of the method.

  **Class, Structure:** number of documentation code lines of the class, including its local methods and attributes; however, its nested and anonymous classes are not included.

#### Calculated
- Class
- Delegate
- Enum
- Interface
- Method
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method**: number of documentation code lines of the method.

  **Class:** number of documentation code lines of the class, including its local methods and attributes; however, its nested, anonymous, and local classes are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Method

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of documentation code lines of the method/function.

  **Class:** number of documentation code lines of the class, including its local methods and attributes; however, its nested, anonymous, and local classes are not included.

#### Calculated
- Class
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method/Function:** number of documentation code lines of the method/function.

  **Class:** number of documentation code lines of the class, including its local methods and attributes; however, its nested and local classes are not included.

  **Module:** number of documentation code lines of the modul.

#### Calculated
- Class
- Function
- Method



## HCPL
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Halstead Calculated Program Length
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)

  The calculated program length is *n1 \* log<sub>2</sub>(n1) + n2 \* log<sub>2</sub>(n2)*.

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Calculated Program Length

#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)

  The calculated program length is *n1 \* log<sub>2</sub>(n1) + n2 \* log<sub>2</sub>(n2)*.

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Calculated Program Length

#### Calculated
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Calculated Program Length

#### Calculated
- Method


## HDIF
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Halstead Difficulty
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)
  -   *N2*: total number of operands

  The Halstead difficulty is *n1/2 \* N2/n2*.

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Difficulty

#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)
  -   *N2*: total number of operands

  The Halstead difficulty is *n1/2 \* N2/n2*.

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Difficulty

#### Calculated
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Difficulty

#### Calculated
- Method


## HEFF
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Halstead Effort
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)
  -   *N1*: total number of operators
  -   *N2*: total number of operands
  -   *n : n1 + n2* (program vocabulary)
  -   *N : N1 + N2* (program length)
  -   *V : N \* log<sub>2</sub>(n)* (volume)
  -   *D : n1/2 \* N2/n2* (difficulty)

  The Halstead effort is *D \* V*.

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Effort

#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)
  -   *N1*: total number of operators
  -   *N2*: total number of operands
  -   *n : n1 + n2* (program vocabulary)
  -   *N : N1 + N2* (program length)
  -   *V : N \* log<sub>2</sub>(n)* (volume)
  -   *D : n1/2 \* N2/n2* (difficulty)

  The Halstead effort is *D \* V*.

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Effort

#### Calculated
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Effort

#### Calculated
- Method


## HNDB
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Halstead Number of Delivered Bugs
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)
  -   *N1*: total number of operators
  -   *N2*: total number of operands
  -   *n : n1 + n2* (program vocabulary)
  -   *N : N1 + N2* (program length)
  -   *V : N \* log<sub>2</sub>(n)* (volume)
  -   *D : n1/2 \* N2/n2* (difficulty)
  -   *E : D \* V* (effort)

  Number of delivered bugs is *E<sup>2/3</sup>/3000*.

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Number of Delivered Bugs

#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)
  -   *N1*: total number of operators
  -   *N2*: total number of operands
  -   *n : n1 + n2* (program vocabulary)
  -   *N : N1 + N2* (program length)
  -   *V : N \* log<sub>2</sub>(n)* (volume)
  -   *D : n1/2 \* N2/n2* (difficulty)
  -   *E : D \* V* (effort)

  Number of delivered bugs is *E<sup>2/3</sup>/3000*.

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Number of Delivered Bugs

#### Calculated
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Number of Delivered Bugs

#### Calculated
- Method


## HPL
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Halstead Program Length
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:**

  -   *N1*: total number of operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *N2*: total number of operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)

  Halstead program length is *N1 + N2*.

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Program Length

#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:**

  -   *N1*: total number of operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *N2*: total number of operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)

  Halstead program length is *N1 + N2*.

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Program Length

#### Calculated
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Program Length

#### Calculated
- Method


## HPV
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Halstead Program Vocabulary
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)

  Halstead program vocabulary is *n1 + n2*.

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Program Vocabulary

#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)

  Halstead program vocabulary is *n1 + n2*.

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Program Vocabulary

#### Calculated
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Program Vocabulary

#### Calculated
- Method


## HTRP
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Halstead Time Required to Program
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)
  -   *N1*: total number of operators
  -   *N2*: total number of operands
  -   *n : n1 + n2* (program vocabulary)
  -   *N : N1 + N2* (program length)
  -   *V : N \* log<sub>2</sub>(n)* (volume)
  -   *D : n1/2 \* N2/n2* (difficulty)
  -   *E : D \* V* (effort)

  Halstead time required to program is *E/18* seconds.

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Time Required to Program

#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)
  -   *N1*: total number of operators
  -   *N2*: total number of operands
  -   *n : n1 + n2* (program vocabulary)
  -   *N : N1 + N2* (program length)
  -   *V : N \* log<sub>2</sub>(n)* (volume)
  -   *D : n1/2 \* N2/n2* (difficulty)
  -   *E : D \* V* (effort)

  Halstead time required to program is *E/18* seconds.

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Time Required to Program

#### Calculated
- Function
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Time Required to Program

#### Calculated
- Method


## HVOL
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Halstead Volume
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)
  -   *N1*: total number of operators
  -   *N2*: total number of operands
  -   *n : n1 + n2* (program vocabulary)
  -   *N : N1 + N2* (program length)

  The Halstead volume is *N \* log<sub>2</sub>(n)*.

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Volume

#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:**

  -   *n1*: number of distinct operators (semantic meanings of the reserved keywords, semicolons, blocks, and identifiers except in their declarations)
  -   *n2*: number of distinct operands (literals - e.g. character, string, and integer literals, - and the identifiers in their declarations)
  -   *N1*: total number of operators
  -   *N2*: total number of operands
  -   *n : n1 + n2* (program vocabulary)
  -   *N : N1 + N2* (program length)

  The Halstead volume is *N \* log<sub>2</sub>(n)*.

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Volume

#### Calculated
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Method:** Halstead Volume

#### Calculated
- Method



## LCOM5
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Lack of Cohesion in Methods 5
#### Tags
- /general/Cohesion
- /internal/csv_column
- /internal/metric_group/Cohesion
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union:** number of functionalities of the class. One of the basic principles of object-oriented programming is encapsulation, meaning that attributes belonging together and the operations that use them should be organized into one class, and one class shall implement only one functionality, i.e. its attributes and methods should be coherent. This metric measures the lack of cohesion and computes into how many coherent classes the class could be split. It is calculated by taking a non-directed graph, where the nodes are the implemented local methods of the class and there is an edge between the two nodes if and only if a common (local or inherited) attribute or abstract method is used or a method invokes another. The value of the metric is the number of connected components in the graph not counting those, which contain only constructors, destructors, getters, or setters.

#### Calculated
- Class
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of functionalities of the class. One of the basic principles of object-oriented programming is encapsulation, meaning that attributes belonging together and the operations that use them should be organized into one class, and one class shall implement only one functionality, i.e. its attributes and methods should be coherent. This metric measures the lack of cohesion and computes into how many coherent classes the class could be split. It is calculated by taking a non-directed graph, where the nodes are the implemented local methods of the class and there is an edge between the two nodes if and only if a common (local or inherited) attribute or abstract method is used or a method invokes another. The value of the metric is the number of connected components in the graph except the ones that contain only constructors, destructors, getters or setters – as they are integral parts of the class.

#### Calculated
- Class
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of functionalities of the class. One of the basic principles of object-oriented programming is encapsulation, meaning that attributes belonging together and the operations that use them should be organized into one class, and one class shall implement only one functionality, i.e. its attributes and methods should be coherent. This metric measures the lack of cohesion and computes into how many coherent classes the class could be split. It is calculated by taking a non-directed graph, where the nodes are the implemented local methods of the class and there is an edge between the two nodes if and only if a common (local or inherited) attribute or abstract method is used or a method invokes another. The value of the metric is the number of connected components in the graph not counting those, which contain only constructors, destructors, getters, or setters.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Class:** number of functionalities of the class. One of the basic principles of object-oriented programming is encapsulation, meaning that attributes belonging together and the operations that use them should be organized into one class, and one class shall implement only one functionality, i.e. its attributes and methods should be coherent. This metric measures the lack of cohesion and computes into how many coherent classes the class could be split. It is calculated by taking a non-directed graph, where the nodes are the implemented local methods of the class and there is an edge between the two nodes if and only if a common (local or inherited) attribute or abstract method is used or a method invokes another. The value of the metric is the number of connected components in the graph not counting those, which contain only constructors, getters, or setters.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of functionalities of the class. One of the basic principles of object-oriented programming is encapsulation, meaning that attributes belonging together and the operations that use them should be organized into one class, and one class shall implement only one functionality, i.e. its attributes and methods should be coherent. This metric measures the lack of cohesion and computes into how many coherent classes the class could be split. It is calculated by taking a non-directed graph, where the nodes are the implemented local methods of the class and there is an edge between the two nodes if and only if a common (local or inherited) attribute or abstract method is used or a method invokes another. The value of the metric is the number of connected components in the graph not counting those, which contain only constructors.

#### Calculated
- Class


## LLOC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Logical Lines of Code
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of non-empty and non-comment code lines of the method; however, its anonymous and local classes are not included.

  **Class, Structure, Union, Interface:** number of non-empty and non-comment code lines of the class, including the non-empty and non-comment lines of its local methods; however, its nested, anonymous, and local classes are not included.

  **Enum:** number of non-empty and non-comment code lines of the enum.

  **Namespace:** number of non-empty and non-comment code lines of the namespace; however, its subnamespaces are not included.

  **File:** number of non-empty and non-comment code lines of the file.

#### Calculated
- Class
- Enum
- File
- Function
- Interface
- Method
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of non-empty and non-comment code lines of the method; however, its anonymous classes are not included.

  **Class, Structure:** number of non-empty and non-comment code lines of the class, including the non-empty and non-comment lines of its local methods; however, its nested and anonymous classes are not included.

  **Namespace:** number of non-empty and non-comment code lines of the namespace; however, its subnamespaces are not included.

  **File:** number of non-empty and non-comment code lines of the file.

#### Calculated
- Class
- Delegate
- Enum
- File
- Interface
- Method
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of non-empty and non-comment code lines of the method; however, its anonymous and local classes are not included.

  **Class:** number of non-empty and non-comment code lines of the class, including the non-empty and non-comment lines of its local methods; however, its nested, anonymous, and local classes are not included.

  **File:** number of non-empty and non-comment code lines of the file.

  **Package:** number of non-empty and non-comment code lines of the package; however, its subpackages are not included.

#### Calculated
- Annotation
- Class
- Enum
- File
- Interface
- Method
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of non-empty and non-comment code lines of the method/function; however, its anonymous and local functions are not included.

  **Class:** number of non-empty and non-comment code lines of the class, including the non-empty and non-comment lines of its local methods; however, its nested, anonymous, and local classes are not included.

  **File:** number of non-empty and non-comment code lines of the file.

#### Calculated
- Class
- File
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method / Function:** number of non-empty and non-comment code lines of the method/function; however, its nested functions are not included.

  **Class:** number of non-empty and non-comment code lines of the class, including the non-empty and non-comment lines of its local methods; however, its nested and local classes are not included.

  **Module:** number of non-empty and non-comment code lines of the module.

  **Package:** number of non-empty and non-comment code lines of the package; however, its subpackages are not included.

  **File:** number of non-empty and non-comment code lines in the file.

#### Calculated
- Class
- File
- Function
- Method
- Module
- Package


## LOC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Lines of Code
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of code lines of the method, including empty and comment lines; however, its anonymous and local classes are not included.

  **Class, Structure, Union, Interface:** number of code lines of the class, including empty and comment lines, as well as its local methods; however, its nested, anonymous, and local classes are not included.

  **Enum:** number of code lines of the enum, including empty and comment lines.

  **Namespace:** number of code lines of the namespace, including empty and comment lines; however, its subnamespaces are not included.

  **File:** number of code lines of the file, including empty and comment lines.

#### Calculated
- Class
- Enum
- File
- Function
- Interface
- Method
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of code lines of the method, including empty and comment lines; however, its anonymous classes are not included.

  **Class, Structure:** number of code lines of the class, including empty and comment lines, as well as its local methods; however, its nested and anonymous classes are not included.

  **Namespace:** number of code lines of the namespace, including empty and comment lines; however, its subnamespaces are not included.

#### Calculated
- Class
- Delegate
- Enum
- File
- Interface
- Method
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method**: number of code lines of the method, including empty and comment lines; however, its anonymous and local classes are not included.

  **Class:** number of code lines of the class, including empty and comment lines, as well as its local methods; however, its nested, anonymous, and local classes are not included.

  **File:** number of code lines of the file.

  **Package:** number of code lines of the package, including empty and comment lines; however, its subpackages are not included.

#### Calculated
- Annotation
- Class
- Enum
- File
- Interface
- Method
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of code lines of the method/function, including empty and comment lines; however, its anonymous and local classes are not included.

  **Class:** number of code lines of the class, including empty and comment lines, as well as its local methods; however, its nested, anonymous, and local classes are not included.

  **File:** number of code lines of the file, including empty and comment lines.

#### Calculated
- Class
- File
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method / Function:** number of code lines of the method/function, including empty and comment lines; however, its nested functions are not included.

  **Class:** number of code lines of the class, including empty and comment lines, as well as its local methods; however, its nested and local classes are not included.

  **Module:** number of code lines of the module, including empty and comment lines.

  **Package:** number of code lines of the package, including empty and comment lines; however, its subpackages are not included.

  **File:** number of code lines in the file, including empty and comment lines.

#### Calculated
- Class
- File
- Function
- Method
- Module
- Package


## MI
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Maintainability Index (Original version)
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  -   *HVOL*: Halstead Volume
  -   *McCC*: McCabe's cyclomatic complexity
  -   *LLOC*: logical lines of code

  The original Maintainability Index is computed by the following formula:

  *MI = 171 - 5.2 \* ln(HVOL) - 0.23 \* (McCC) - 16.2 \* ln(LLOC)*

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  -   *HVOL*: Halstead Volume
  -   *McCC*: McCabe’s cyclomatic complexity
  -   *LLOC*: logical lines of code

  The original Maintainability Index is computed by the following formula:

  *MI = 171 - 5.2 \* ln(HVOL) - 0.23 \* (McCC) - 16.2 \* ln(LLOC)*

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method


## MIMS
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Maintainability Index (Microsoft version)
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  -   *HVOL*: Halstead Volume
  -   *McCC*: McCabe's cyclomatic complexity
  -   *LLOC*: logical lines of code

  The Maintainability Index used by Microsoft's Visual Studio is computed by the following formula:

  *MIMS = max(0,(171 - 5.2 \* ln(HVOL) - 0.23 \* (McCC) - 16.2 \* ln(LLOC)) \* 100 / 171)*

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  -   *HVOL*: Halstead Volume
  -   *McCC*: McCabe’s cyclomatic complexity
  -   *LLOC*: logical lines of code

  The Maintainability Index used by Microsoft’s Visual Studio is computed by the following formula:

  *MIMS = max(0,(171 - 5.2 \* ln(HVOL) - 0.23 \* (McCC) - 16.2 \* ln(LLOC)) \* 100 / 171)*

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method


## MISEI
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Maintainability Index (SEI version)
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  -   *HVOL*: Halstead Volume
  -   *McCC*: McCabe's cyclomatic complexity
  -   *LLOC*: logical lines of code
  -   *CD*: comment density

  The Maintainability Index derived by the Software Engineering Institute (SEI) is computed by the following formula:

  *MISEI = 171 - 5.2 \* log<sub>2</sub>(HVOL) - 0.23 \* McCC - 16.2 \* log<sub>2</sub>(LLOC) + 50 \* sin(sqrt(2.4 \* CD))*

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  -   *HVOL*: Halstead Volume
  -   *McCC*: McCabe’s cyclomatic complexity
  -   *LLOC*: logical lines of code
  -   *CD*: comment density

  The Maintainability Index derived by the Software Engineering Institute (SEI) is computed by the following formula:

  *MISEI = 171 - 5.2 \* log<sub>2</sub>(HVOL) - 0.23 \* McCC - 16.2 \* log<sub>2</sub>(LLOC) + 50 \* sin(sqrt(2.4 \* CD))*

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method


## MISM
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Maintainability Index (SourceMeter version)
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  -   *HVOL*: Halstead Volume
  -   *McCC*: McCabe's cyclomatic complexity
  -   *LLOC*: logical lines of code
  -   *CD*: comment density

  The Maintainability Index proposed by SourceMeter combines the different scaling approach from Microsoft's version with the inclusion of comment percentage from the Software Engineering Institute (SEI) version into the following formula:

  *MISM = max(0, (171 - 5.2 \* log<sub>2</sub>(HVOL) - 0.23 \* McCC - 16.2 \* log<sub>2</sub>(LLOC) + 50 \* sin(sqrt(2.4 \* CD))) \* 100 / 171)*

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  -   *HVOL*: Halstead Volume
  -   *McCC*: McCabe’s cyclomatic complexity
  -   *LLOC*: logical lines of code
  -   *CD*: comment density

  The Maintainability Index proposed by SourceMeter combines the different scaling approach from Microsoft’s version with the inclusion of comment percentage from the Software Engineering Institute (SEI) version into the following formula:

  *MISM = max(0, (171 - 5.2 \* log<sub>2</sub>(HVOL) - 0.23 \* McCC - 16.2 \* log<sub>2</sub>(LLOC) + 50 \* sin(sqrt(2.4 \* CD))) \* 100 / 171)*

#### Calculated
- Method

### javascript -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Method


## McCC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=McCabe's Cyclomatic Complexity
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** complexity of the method expressed as the number of independent control flow paths in it. It represents a lower bound for the number of possible execution paths in the source code and at the same time it is an upper bound for the minimum number of test cases needed for achieving full branch test coverage. The value of the metric is calculated as the number of the following instructions plus 1: if, for, foreach, range-based for, while, do-while, case label (which belongs to a switch instruction), catch, conditional expression (?:). Moreover, logical "and" (&&) and logical "or" (||) expressions also add 1 to the value because their short-circuit evaluation can cause branching depending on the first operand. The following instructions are not included: else, switch, default label (which belongs to a switch instruction), try.

  **File:** complexity of the file expressed as the number of independent control flow paths in it. It represents a lower bound for the number of possible execution paths in the source code and at the same time it is an upper bound for the minimum number of test cases needed for achieving full branch test coverage. The value of the metric is calculated as the number of the following instructions plus 1: if, for, foreach, range-based for, while, do-while, case label (which belongs to a switch instruction), catch, conditional expression (?:). Moreover, logical "and" (&&) and logical "or" (||) expressions also add 1 to the value because their short-circuit evaluation can cause branching depending on the first operand. The following instructions are not included: else, switch, default label (which belongs to a switch instruction), try.

#### Calculated
- File
- Function
- Method

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** complexity of the method expressed as the number of independent control flow paths in it. It represents a lower bound for the number of possible execution paths in the source code and at the same time it is an upper bound for the minimum number of test cases needed for achieving full branch test coverage. The value of the metric is initially 1 which increases by 1 for each occurence of the following instructions: if, for, foreach, while, do-while, case label (label that belongs to a switch instruction), catch (handler that belongs to a try block), conditional statement (?:) and conditional access operators (?. and ?\[\]). Moreover, logical and (&&), logical or (||) and null coalescing (??) expressions also add to the final value because their short-circuit evalutaion can cause branching depending on the first operand. The following language elements do not increase the value: else, try, switch, default label (default label that belongs to a switch instruction), finally.

#### Calculated
- File
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** complexity of the method expressed as the number of independent control flow paths in it. It represents a lower bound for the number of possible execution paths in the source code and at the same time it is an upper bound for the minimum number of test cases needed for achieving full branch test coverage. The value of the metric is calculated as the number of the following instructions plus 1: if, for, foreach, while, do-while, case label (which belongs to a switch instruction), catch, conditional statement (?:). Moreover, logical “and” (&&) and logical “or” (||) expressions also add 1 to the value because their short-circuit evaluation can cause branching depending on the first operand. The following instructions are not included: else, switch, default label (which belongs to a switch instruction), try, finally.

  **File:** complexity of the file expressed as the number of independent control flow paths in it. It is calculated as the sum of the McCabe’s Cyclomatic Complexity values of the methods can be found in the file.

#### Calculated
- File
- Method

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** complexity of the method expressed as the number of independent control flow paths in it. It represents a lower bound for the number of possible execution paths in the source code and at the same time it is an upper bound for the minimum number of test cases needed for achieving full branch test coverage. The value of the metric is calculated as the number of the following instructions plus 1: if, else if, for, for…in, for…of, while, do-while, case label (which belongs to a switch instruction), catch clause, conditional expression (?:). Moreover, logical “and” (&&) and logical “or” (||) expressions also add 1 to the value because their short-circuit evaluation can cause branching depending on the first operand. The following instructions are not included: else, switch, try, finally.

  **File:** complexity of the file expressed as the number of independent control flow paths in it. It is calculated as the sum of the McCabe’s Cyclomatic Complexity values of the methods can be found in the file.

#### Calculated
- File
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method / Function:** complexity of the method/function expressed as the number of independent control flow paths in it. It represents a lower bound for the number of possible execution paths in the source code and at the same time it is an upper bound for the minimum number of test cases needed for achieving full branch test coverage. The value of the metric is calculated as the number of the following instructions plus 1: if, for, while, except and conditional expression. Moreover, logical “and” and logical “or” expressions also add 1 to the value because their short-circuit evaluation can cause branching depending on the first operand. The following instructions are not included: else, try, finally.

  **File:** complexity of the file expressed as the number of independent control flow paths in it. It represents a lower bound for the number of possible execution paths in the source code and at the same time it is an upper bound for the minimum number of test cases needed for achieving full branch test coverage. The value of the metric is calculated as the number of the following instructions plus 1: if, for, while, except and conditional expression. Moreover, logical “and” and logical “or” expressions also add 1 to the value because their short-circuit evaluation can cause branching depending on the first operand. The following instructions are not included: else, try, finally.

#### Calculated
- File
- Function
- Method


## NA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Attributes
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of attributes in the class, including the inherited ones; however, the attributes of its nested, anonymous, and local classes are not included.

  **Enum:** number of enumerators in the enum.

  **Namespace:** number of attributes in the namespace; however, attributes of its subnamespaces are not included.

#### Calculated
- Class
- Enum
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of attributes in the class, including the inherited ones and generated ones backing auto properties; however, the attributes of its nested and anonymous classes are not included.

  **Namespace:** number of attributes in the namespace; however, attributes of its subnamespaces are not included.

#### Calculated
- Class
- Enum
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of attributes in the class, including the inherited ones; however, the attributes of its nested, anonymous, and local classes are not included.

  **Package:** number of attributes in the package; however, attributes of its subpackages are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Class:** number of attributes in the class, including the inherited ones; however, the attributes of its nested, anonymous, and local classes are not included.

  **Enum:** number of enumerators in the enum.

  **Namespace:** number of attributes in the namespace; however, attributes of its subnamespaces are not included.

#### Calculated
- Class
- File

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of attributes in the class, including the inherited ones; however, the attributes of its nested and local classes are not included.

  **Module:** number of attributes in the module.

  **Package:** number of attributes in the package; however, attributes of its subpackages are not included.

#### Calculated
- Class
- Module
- Package


## NCL
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Classes
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of classes in the namespace; however, the classes of its subnamespaces are not included.

#### Calculated
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of classes in the namespace; however, the classes of its subnamespaces are not included.

#### Calculated
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of classes in the package; however, the classes of its subpackages are not included.

#### Calculated
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **File:** number of classes in the file.

#### Calculated
- File

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Module:** number of classes in the module.

  **Package:** number of classes in the package; however, the classes of its subpackages are not included.

#### Calculated
- Module
- Package


## NEN
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Enums
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of enums in the namespace; however, the enums of its subnamespaces are not included.

#### Calculated
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of enums in the namespace; however, the enums of its subnamespaces are not included.

#### Calculated
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of enums in the package; however, the enums of its subpackages are not included.

#### Calculated
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## NG
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Getters
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of getter methods in the class, including the inherited ones; however, the getter methods of its nested, anonymous, and local classes are not included. Methods that override abstract methods are not counted.

  **Namespace:** number of getter methods in the namespace; however, getter methods of its subnamespaces are not included.

#### Calculated
- Class
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of getter methods in the class, including the inherited ones; however, the getter methods of its nested and anonymous classes are not included. Methods that override abstract methods are not counted.

  **Namespace:** number of getter methods in the namespace; however, getter methods of its subnamespaces are not included.

#### Calculated
- Class
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of getter methods in the class, including the inherited ones; however, the getter methods of its nested, anonymous, and local classes are not included. Methods that override abstract methods are not counted.

  **Package**: number of getter methods in the package; however, getter methods of its subpackages are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of getter methods in the class, including the inherited ones.

#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class
- Module
- Package


## NII
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Incoming Invocations
#### Tags
- /general/Coupling
- /internal/csv_column
- /internal/metric_group/Coupling
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of other methods and attribute initializations which directly call the method. If the method is invoked several times from the same method or attribute initialization, it is counted only once.

  **Class, Structure, Union, Interface:** number of other methods and attribute initializations which directly call the local methods of the class. If a method is invoked several times from the same method or attribute initialization, it is counted only once.

#### Calculated
- Class
- Function
- Interface
- Method
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of other methods and attribute initializations which directly call the method. If the method is invoked several times from the same method or attribute initialization, it is counted only once.

  **Class, Structure:** number of other methods and attribute initializations which directly call the local methods of the class. If a method is invoked several times from the same method or attribute initialization, it is counted only once.

#### Calculated
- Class
- Interface
- Method
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of other methods and attribute initializations which directly call the method. If the method is invoked several times from the same method or attribute initialization, it is counted only once.

  **Class:** number of other methods and attribute initializations which directly call the local methods of the class. If a method is invoked several times from the same method or attribute initialization, it is counted only once.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Method

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of other methods/functions which directly call the method. If the method/function is invoked several times from the same method/function, it is counted only once.

  **Class:** number of other methods/functions which directly call the local methods of the class. If a method is invoked several times from the same method, it is counted only once.

#### Calculated
- Class
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method / Function:** number of other methods/functions and attribute initializations which directly call the method/function. If the method/function is invoked several times from the same method/function or attribute initialization, it is counted only once.

  **Class:** number of other methods and attribute initializations which directly call the local methods of the class. If a method is invoked several times from the same method or attribute initialization, it is counted only once.

#### Calculated
- Class
- Function
- Method


## NIN
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Interfaces
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of interfaces in the namespace; however, the interfaces of its subnamespaces are not included.

#### Calculated
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of interfaces in the namespace; however, the interfaces of its subnamespaces are not included.

#### Calculated
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of interfaces in the package; however, the interfaces of its subpackages are not included.

#### Calculated
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## NL
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Nesting Level
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** complexity of the method expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes. The following instructions are taken into account: if, else-if, else, for, while, do-while, switch, try, catch and block statements that are directly inside another block statement. The following instructions do not increase the value by themselves; however, if additional embeddednesses can be found in their blocks, they are considered: case and default label (which belong to a switch instruction).

  **Class, Structure, Union:** complexity of the class expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes. It is calculated as the maximum nesting level (NL) of its local methods.

#### Calculated
- Class
- Function
- Method
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** complexity of the method expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes. The following instructions are taken into account: if, else-if, else, for, foreach, while, do-while, switch, try, catch, finally, lock, checked, unchecked, fixed, using statement, conditional statement (?:) and block statements that are directly inside another block statement. The following instructions do not increase the value by themselves; however, if additional embeddednesses can be found in their blocks, they are considered: case and default label.

  **Class, Structure:** complexity of the class expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes. It is calculated as the maximum nesting level (NL) of its local methods.

#### Calculated
- Class
- Method
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** complexity of the method expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes. The following instructions are taken into account: if, else-if, else, for, while, do-while, switch, try, catch, finally and block statements that are directly inside another block statement. The following instructions do not increase the value by themselves; however, if additional embeddednesses can be found in their blocks, they are considered: case and default label (which belong to a switch instruction).

  **Class:** complexity of the class expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes. It is calculated as the maximum nesting level (NL) of its local methods and init blocks.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Method

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** complexity of the method/function expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes. The following instructions are taken into account: if, else-if, else, for, for-in, for-of, while, do-while, switch, try, catch, finally and block statements that are directly inside another block statement. The following instructions do not increase the value by themselves; however, if additional embeddedness can be found in their blocks, they are considered: case and default label (which belong to a switch instruction).

  **Class:** complexity of the class expressed as the depth of the maximum embeddedness of its conditional and iteration block scopes. It is calculated as the maximum nesting level (NL) of its local methods.

#### Calculated
- Class
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method / Function:** complexity of the method/function expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes. The following instructions are taken into account: if, else-if, else, for, while, with, try, except, finally.

  **Class:** complexity of the class expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes. It is calculated as the maximum nesting level (NL) of its local methods.

#### Calculated
- Class
- Function
- Method


## NLA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Local Attributes
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) attributes in the class; however, the attributes of nested, anonymous, and local classes are not included.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) attributes in the class, including generated ones backing auto properties; however, the attributes of nested and anonymous classes are not included.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) attributes in the class; however, the attributes of nested, anonymous, and local classes are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) attributes in the class.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) attributes in the class; however, the attributes of nested and local classes are not included.

#### Calculated
- Class


## NLE
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Nesting Level Else-If
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** complexity of the method expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes, where in the if-else-if construct only the first if instruction and in case of multiply catch blocks only the first catch is considered. The following instructions are taken into account: if, else, for, while, do-while, switch, try, catch and block statements that are directly inside another block statement. The following instructions do not increase the value by themselves; however, if additional embeddednesses can be found in their blocks, they are considered: else-if (i.e. in the if-else-if construct the use of else-if does not increase the value of the metric), case and default label (which belong to a switch instruction).

  **Class, Structure, Union:** complexity of the class expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes, where in the if-else-if construct only the first if instruction is considered. It is calculated as the maximum nesting level (NLE) of its local methods.

#### Calculated
- Class
- Function
- Method
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** complexity of the method expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes, where in the if-else-if construct only the first if instruction is considered. The following instructions are taken into account: if, for, foreach, while, do-while, switch, try, catch, finally, lock, checked, unchecked, fixed, using statement, conditional statement (?:) and block statements that are directly inside another block statement. The following instructions do not increase the value by themselves; however, if additional embeddednesses can be found in their blocks, they are considered: else, else-if (i.e. in the if-else-if construct the use of else-if does not increase the value of the metric), case and default label.

  **Class, Structure:** complexity of the class expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes, where in the if-else-if construct only the first if instruction is considered. It is calculated as the maximum nesting level (NLE) of its local methods.

#### Calculated
- Class
- Method
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** complexity of the method expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes, where in the if-else-if construct only the first if instruction is considered. The following instructions are taken into account: if, else, for, while, do-while, switch, try, catch, finally and block statements that are directly inside another block statement. The following instructions do not increase the value by themselves; however, if additional embeddednesses can be found in their blocks, they are considered: else-if (i.e. in the if-else-if construct the use of else-if does not increase the value of the metric), case and default label (which belong to a switch instruction).

  **Class:** complexity of the class expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes, where in the if-else-if construct only the first if instruction is considered. It is calculated as the maximum nesting level (NLE) of its local methods and init blocks.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Method

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** complexity of the method/function expressed as the depth of the maximum embeddedness of its conditional and iteration block scopes, where in the if-else-if construct only the first if instruction is considered. The following instructions are taken into account: if, for, while, conditional expression. The following instructions do not increase the value by themselves; however, if additional embeddedness can be found in their blocks, they are considered: else, else if (i.e. in the if-else-if construct the use of else-if does not increase the value of the metric), try, except, finally.

  **Class:** complexity of the class expressed as the depth of the maximum embeddedness of its conditional and iteration block scopes, where in the if-else-if construct only the first if instruction is considered. It is calculated as the maximum nesting level (NLE) of its local methods.

#### Calculated
- Class
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method / Function:** complexity of the method/function expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes, where in the if-else-if construct only the first if instruction is considered. The following instructions are taken into account: if, else, for, while, with, try, except, finally. The following instructions do not increase the value by themselves; however, if additional embeddedness can be found in their blocks, they are considered: else-if (i.e. in the if-else-if construct the use of else-if does not increase the value of the metric).

  **Class:** complexity of the class expressed as the depth of the maximum embeddedness of its conditional, iteration and exception handling block scopes, where in the if-else-if construct only the first if instruction is considered. It is calculated as the maximum nesting level (NLE) of its local methods.

#### Calculated
- Class
- Function
- Method


## NLG
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Local Getters
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) getter methods in the class; however, the getter methods of its nested, anonymous, and local classes are not included. Methods that override abstract methods are not counted.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) getter methods in the class; however, the getter methods of its nested and anonymous classes are not included. Methods that override abstract methods are not counted.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) getter methods in the class; however, the getter methods of its nested, anonymous, and local classes are not included. Methods that override abstract methods are not counted.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) getter methods in the class; however, the getter methods of its nested, anonymous, and local classes are not included. Methods that override abstract methods are not counted.

#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class


## NLM
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Local Methods
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) methods in the class; however, the methods of nested, anonymous, and local classes are not included.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) methods in the class; however, the methods of nested and anonymous classes are not included.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) methods in the class; however, the methods of nested, anonymous, and local classes are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) methods in the class.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) methods in the class; however, the methods of nested and local classes are not included.

#### Calculated
- Class


## NLPA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Local Public Attributes
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) public attributes in the class; however, the attributes of nested, anonymous, and local classes are not included.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) public attributes in the class, including generated ones backing public auto properties; however, the attributes of nested and anonymous classes are not included.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) public attributes in the class; however, the attributes of nested, anonymous, and local classes are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class


## NLPM
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Local Public Methods
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) public methods in the class; however, the methods of nested, anonymous, and local classes are not included.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) public methods in the class; however, the methods of nested and anonymous classes are not included.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) public methods in the class; however, the methods of nested, anonymous, and local classes are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class


## NLS
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Local Setters
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) setter methods in the class; however, the setter methods of its nested, anonymous, and local classes are not included. Methods that override abstract methods are not counted.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) setter methods in the class; however, the setter methods of its nested and anonymous classes are not included. Methods that override abstract methods are not counted.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) setter methods in the class; however, the setter methods of its nested, anonymous, and local classes are not included. Methods that override abstract methods are not counted.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) setter methods in the class.

#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class


## NM
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Methods
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of methods in the class, including the inherited ones; however, the methods of its nested, anonymous and local classes are not included. Methods that override abstract methods are not counted.

  **Namespace:** number of methods in the namespace; however, methods of its subnamespaces are not included.

#### Calculated
- Class
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of methods in the class, including the inherited ones; however, the methods of its nested and anonymous classes are not included. Methods that override abstract methods are not counted.

  **Namespace:** number of methods in the namespace; however, methods of its subnamespaces are not included.

#### Calculated
- Class
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of methods in the class, including the inherited ones; however, the methods of its nested, anonymous and local classes are not included. Methods that override abstract methods are not counted.

  **Package:** number of methods in the package; however, methods of its subpackages are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of methods in the class, including the inherited ones.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of methods/functions in the class, including the inherited ones; however, the methods of its nested and local classes are not included. Methods that override abstract methods are not counted.

  **Module:** number of methods in the module.

  **Package:** number of methods in the package; however, methods of its subpackages are not included.

#### Calculated
- Class
- Module
- Package


## NOA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Ancestors
#### Tags
- /general/Inheritance
- /internal/csv_column
- /internal/metric_group/Inheritance
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of classes, interfaces, enums and annotations from which the class is directly or indirectly inherited.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of classes and interfaces from which the class is directly or indirectly inherited.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of classes, interfaces, enums and annotations from which the class is directly or indirectly inherited.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of classes from which the class is directly or indirectly inherited.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of classes from which the class is directly or indirectly inherited.

#### Calculated
- Class


## NOC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Children
#### Tags
- /general/Inheritance
- /internal/csv_column
- /internal/metric_group/Inheritance
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of classes, interfaces, enums and annotations which are directly derived from the class.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of classes and interfaces which are directly derived from the class.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of classes, interfaces, enums and annotations which are directly derived from the class.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of classes which are directly derived from the class.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of classes which are directly derived from the class.

#### Calculated
- Class


## NOD
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Descendants
#### Tags
- /general/Inheritance
- /internal/csv_column
- /internal/metric_group/Inheritance
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of classes, interfaces, enums, annotations, which are directly or indirectly derived from the class.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of classes and interfaces which are directly or indirectly derived from the class.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of classes, interfaces, enums, annotations, which are directly or indirectly derived from the class.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of classes which are directly or indirectly derived from the class.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of classes, which are directly or indirectly derived from the class.

#### Calculated
- Class


## NOI
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Outgoing Invocations
#### Tags
- /general/Coupling
- /internal/csv_column
- /internal/metric_group/Coupling
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of directly called methods. If a method is invoked several times, it is counted only once.

  **Class, Structure, Union:** number of directly called methods of other classes, including method invocations from attribute initializations. If a method is invoked several times, it is counted only once.

#### Calculated
- Class
- Function
- Method
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of directly called methods. If a method is invoked several times, it is counted only once.

  **Class, Structure:** number of directly called methods of other classes, including method invocations from attribute initializations. If a method is invoked several times, it is counted only once.

#### Calculated
- Class
- Method
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of directly called methods. If a method is invoked several times, it is counted only once.

  **Class:** number of directly called methods of other classes, including method invocations from attribute initializations. If a method is invoked several times, it is counted only once.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Method

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of directly called methods. If a method is invoked several times, it is counted only once.

  **Class:** number of directly called methods of other classes, including method invocations from attribute initializations. If a method is invoked several times, it is counted only once.

#### Calculated
- Class
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method / Function:** number of directly called methods/functions. If a method/function is invoked several times, it is counted only once.

  **Class:** number of directly called methods of other classes, including method invocations from attribute initializations. If a method is invoked several times, it is counted only once.

#### Calculated
- Class
- Function
- Method


## NOP
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Parents
#### Tags
- /general/Inheritance
- /internal/csv_column
- /internal/metric_group/Inheritance
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of classes, interfaces, enums and annotations from which the class is directly inherited.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of classes and interfaces from which the class is directly inherited.

#### Calculated
- Class
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of classes, interfaces, enums and annotations from which the class is directly inherited.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of classes from which the class is directly inherited.

#### Calculated
- Class


## NOS
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Statements
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of statements in the method; however, the statements of its anonymous and local classes are not included.

  **Class, Structure, Union:** number of statements in the class; however, the statements of its nested, anonymous, and local classes are not included.

  **File:** number of statements in the file.

#### Calculated
- Class
- File
- Function
- Method
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of statements in the method; however, the statements of its anonymous classes are not included.

  **Class, Structure:** number of statements in the class; however, the statements of its nested and anonymous classes are not included.

#### Calculated
- Class
- Method
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of statements in the method; however, the statements of its anonymous and local classes are not included.

  **Class:** number of statements in the class; however, the statements of its nested, anonymous, and local classes are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Method

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of statements in the method.

  **Class:** number of statements in the class.

  **File:** number of statements in the file.

#### Calculated
- Class
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method / Function:** number of statements in the method/function; however, the statements of its nested functions are not included.

  **Class:** number of statements in the class; however, the statements of its nested and local classes are not included.

  **File:** number of statements in the file.

#### Calculated
- Class
- File
- Function
- Method


## NPA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Public Attributes
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of public attributes in the class, including the inherited ones; however, the public attributes of its nested, anonymous, and local classes are not included.

  **Namespace:** number of public attributes in the namespace; however, the public attributes of its subnamespaces are not included.

#### Calculated
- Class
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of public attributes in the class, including the inherited ones and generated ones backing public auto properties; however, the public attributes of its nested and anonymous classes are not included.

  **Namespace:** number of public attributes in the namespace; however, the public attributes of its subnamespaces are not included.

#### Calculated
- Class
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of public attributes in the class, including the inherited ones; however, the public attributes of its nested, anonymous, and local classes are not included.

  **Package:** number of public attributes in the package; however, the public attributes of its subpackages are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class
- Module
- Package


## NPKG
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Packages
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of directly contained subnamespaces of the namespace.

#### Calculated
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of directly contained subnamespaces of the namespace.

#### Calculated
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### DisplayName=Number of packages
#### HelpText
  **Package:** number of directly contained subpackages of the package.

#### Calculated
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of directly contained subpackages of the package.

#### Calculated
- Package


## NPM
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Public Methods
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of public methods in the class, including the inherited ones; however, the public methods of nested, anonymous, and local classes are not included. Methods that override abstract methods are not counted.

  **Namespace:** number of public methods in the namespace; however, the public methods of its subnamespaces are not included.

#### Calculated
- Class
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of public methods in the class, including the inherited ones; however, the public methods of nested and anonymous classes are not included. Methods that override abstract methods are not counted.

  **Namespace:** number of public methods in the namespace; however, the public methods of its subnamespaces are not included.

#### Calculated
- Class
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of public methods in the class, including the inherited ones; however, the public methods of nested, anonymous, and local classes are not included. Methods that override abstract methods are not counted.

  **Package:** number of public methods in the package; however, the public methods of its subpackages are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class
- Module
- Package


## NS
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Setters
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of setter methods in the class, including the inherited ones; however, the setter methods of its nested, anonymous, and local classes are not included. Methods that override abstract methods are not counted.

  **Namespace:** number of setter methods in the namespace; however, setter methods of its subnamespaces are not included.

#### Calculated
- Class
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of setter methods in the class, including the inherited ones; however, the setter methods of its nested and anonymous classes are not included. Methods that override abstract methods are not counted.

  **Namespace:** number of setter methods in the namespace; however, setter methods of its subnamespaces are not included.

#### Calculated
- Class
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of setter methods in the class, including the inherited ones; however, the setter methods of its nested, anonymous, and local classes are not included. Methods that override abstract methods are not counted.

  **Package:** number of setter methods in the package; however, setter methods of its subpackages are not included.

#### Calculated
- Annotation
- Class
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of setter methods in the class, including the inherited ones.

#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class
- Module
- Package


## NST
### Default
#### Enabled=false
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Structures
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of structures in the namespace; however, the structures of its subnamespaces are not included.

#### Calculated
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of structures in the namespace; however, the structures of its subnamespaces are not included.

#### Calculated
- Namespace

### java -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## NUMPAR
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Parameters
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of the parameters of the method. The varargs parameter counts as one.

#### Calculated
- Function
- Method

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of the parameters of the method. The varargs parameter counts as one.

#### Calculated
- Method

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method**: number of the parameters of the method. The varargs parameter counts as one.

#### Calculated
- Method

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of the parameters of the method. Counts only the explicitly given number of parameters (‘arguments’ object is not counted).

#### Calculated
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method / Function:** number of the parameters of the method/function. The varargs and kwargs parameters counts as one.

#### Calculated
- Function
- Method


## NUN
### Default
#### Enabled=false
#### NumericType=true
#### Warning=false
#### DisplayName=Number of Unions
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of unions in the namespace; however, the unions of its subnamespaces are not included.

#### Calculated
- Namespace

### csharp -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  Placeholder


### java -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## PDA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Public Documented API
#### Tags
- /general/Documentation
- /internal/csv_column
- /internal/metric_group/Documentation
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of documented public methods in the class (+1 if the class itself is documented); however, the methods of its nested, anonymous, and local classes are not counted.

  **Namespace:** number of documented public classes and methods in the namespace; however, the classes and methods of its subnamespaces are not counted.

  **File:** number of documented public classes and methods in the file.

#### Calculated
- Class
- File
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** the number of the documented public methods of the class (+1 if the class itself is documented). When calculating the metrics the nested, anonymous or local classes found in the class and their methods are not calculated.

  **Namespace:** the number of the documented public classes and public documented methods found in the namespace. When calculating the metric, classes and methods found in the subnamespaces of the namespace are not taken into account.

#### Calculated
- Class
- File
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of documented public methods in the class (+1 if the class itself is documented); however, the methods of its nested, anonymous, and local classes are not counted.

  **File:** number of documented public classes and methods in the file.

  **Package:** number of documented public classes and methods in the package; however, the classes and methods of its subpackages are not counted.

#### Calculated
- Annotation
- Class
- Enum
- File
- Interface
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of documented methods in the class (+1 if the class itself is documented); however, the methods of its nested, anonymous, and local classes are not counted.

#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class
- Module
- Package


## PUA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Public Undocumented API
#### Tags
- /general/Documentation
- /internal/csv_column
- /internal/metric_group/Documentation
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of undocumented public methods in the class (+1 if the class itself is undocumented); however, the methods of its nested, anonymous, and local classes are not counted.

  **Namespace:** number of undocumented public classes and methods in the namespace; however, the classes and methods of its subnamespaces are not counted.

  **File:** number of undocumented public classes and methods in the file.

#### Calculated
- Class
- File
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** the number of the undocumented public methods of the class (+1 if the class itself is undocumented). When calculating the metrics the nested, anonymous or local classes to be found in the class and their methods are not calculated.

  **Namespace:** the number of the undocumented public classes and undocumented public methods to be found in the namespace. When calculating the metric, classes and methods to be found in the subnamespaces of the namespace are not taken into account.

#### Calculated
- Class
- File
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of undocumented public methods in the class (+1 if the class itself is undocumented); however, the methods of its nested, anonymous, and local classes are not counted.

  **File:** number of undocumented public classes and methods in the file.

  **Package:** number of undocumented public classes and methods in the package; however, the classes and methods of its subpackages are not counted.

#### Calculated
- Annotation
- Class
- Enum
- File
- Interface
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of undocumented methods in the class (+1 if the class itself is undocumented); however, the methods of its nested, anonymous, and local classes are not counted.

#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class
- Module
- Package


## RFC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Response set For Class
#### Tags
- /general/Coupling
- /internal/csv_column
- /internal/metric_group/Coupling
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union:** number of local (i.e. not inherited) methods in the class (NLM) plus the number of directly invoked other methods by its methods or attribute initializations (NOI).

#### Calculated
- Class
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) methods in the class (NLM) plus the number of directly invoked other methods by its methods or attribute initializations (NOI).

#### Calculated
- Class
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) methods in the class (NLM) plus the number of directly invoked other methods by its methods or attribute initializations (NOI).

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) methods in the class (NLM) plus the number of directly invoked other methods by its methods or attribute initializations (NOI).

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) methods in the class (NLM) plus the number of directly invoked other methods by its methods or attribute initializations (NOI).

#### Calculated
- Class



## TAD
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total API Documentation
#### Tags
- /general/Documentation
- /internal/csv_column
- /internal/metric_group/Documentation
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** ratio of the number of documented public classes and methods in the namespace to the number of all of its public classes and methods, including its subnamespaces.

  **Component:** ratio of the number of documented public classes and methods in the component to the number of all of its public classes and methods, including its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** ratio of the number of documented public classes and methods in the namespace to the number of all of its public classes and methods, including its subnamespaces.

  **Component:** ratio of the number of documented public classes and methods in the component to the number of all of its public classes and methods, including its subcomponents.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** ratio of the number of documented public classes and methods in the package to the number of all of its public classes and methods, including its subpackages.

  **Component:** ratio of the number of documented public classes and methods in the component to the number of all of its public classes and methods, including its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Component:** ratio of the number of documented classes and methods in the component to the number of all of its classes and methods, including its subcomponents.

#### Calculated
- Component

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Component
- Module
- Package


## TCD
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Comment Density
#### Tags
- /general/Documentation
- /internal/csv_column
- /internal/metric_group/Documentation
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** ratio of the total comment lines of the method (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Class, Structure, Union:** ratio of the total comment lines of the class (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Namespace:** ratio of the total comment lines of the namespace (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Component:** ratio of the total comment lines of the component (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

#### Calculated
- Class
- Component
- Function
- Method
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** ratio of the total comment lines of the method (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Class, Structure:** ratio of the total comment lines of the class (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Namespace:** ratio of the total comment lines of the namespace (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Component:** ratio of the total comment lines of the component (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

#### Calculated
- Class
- Component
- Delegate
- Method
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** ratio of the total comment lines of the method (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Class:** ratio of the total comment lines of the class (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Package:** ratio of the total comment lines of the package (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Component:** ratio of the total comment lines of the component (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

#### Calculated
- Annotation
- Class
- Component
- Enum
- Interface
- Method
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method/Function:** ratio of the total comment lines of the method/function (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Class:** ratio of the total comment lines of the class (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Component:** ratio of the total comment lines of the component (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

#### Calculated
- Class
- Component
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method/Function:** ratio of the total comment lines of the method/function (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Class:** ratio of the total comment lines of the class (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Module:** ratio of the total comment lines of the module (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Package:** ratio of the total comment lines of the package (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

  **Component:** ratio of the total comment lines of the component (TCLOC) to the sum of its total comment (TCLOC) and total logical lines of code (TLLOC).

#### Calculated
- Class
- Component
- Function
- Method
- Module
- Package


## TCLOC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Comment Lines of Code
#### Tags
- /general/Documentation
- /internal/csv_column
- /internal/metric_group/Documentation
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of comment and documentation code lines of the method, including its anonymous and local classes.

  **Class, Structure, Union, Interface:** number of comment and documentation code lines of the class, including its local methods and attributes, as well as its nested, anonymous, and local classes.

  **Namespace:** number of comment and documentation code lines of the namespace, including its subnamespaces.

  **Component:** number of comment and documentation code lines of the component, including its subcomponents.

#### Calculated
- Class
- Component
- Function
- Interface
- Method
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of comment and documentation code lines of the method, including its anonymous classes.

  **Class, Structure:** number of comment and documentation code lines of the class, including its local methods and attributes, as well as its nested and anonymous classes.

  **Namespace:** number of comment and documentation code lines of the namespace, including its subnamespaces.

  **Component:** number of comment and documentation code lines of the component, including its subcomponents.

#### Calculated
- Class
- Component
- Delegate
- Interface
- Method
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method**: number of comment and documentation code lines of the method, including its anonymous and local classes.

  **Class:** number of comment and documentation code lines of the class, including its local methods and attributes, as well as its nested, anonymous, and local classes.

  **Package:** number of comment and documentation code lines of the package, including its subpackages.

  **Component:** number of comment and documentation code lines of the component, including its subcomponents.

#### Calculated
- Annotation
- Class
- Component
- Enum
- Interface
- Method
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method/Function:** number of comment and documentation code lines of the method/function, including its local classes.

  **Class:** number of comment and documentation code lines of the class, including its local methods and attributes, as well as its nested and local classes.

  **Component:** number of comment and documentation code lines of the component, including its subcomponents.

#### Calculated
- Class
- Component
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method/Function:** number of comment and documentation code lines of the method/function, including its local classes.

  **Class:** number of comment and documentation code lines of the class, including its local methods and attributes, as well as its nested and local classes.

  **Module:** number of comment and documentation code lines of the module.

  **Package:** number of comment and documentation code lines of the package, including its subpackages.

  **Component:** number of comment and documentation code lines of the component, including its subcomponents.

#### Calculated
- Class
- Component
- Function
- Method
- Module
- Package


## TLLOC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Logical Lines of Code
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of non-empty and non-comment code lines of the method, including the non-empty and non-comment lines of its anonymous and local classes.

  **Class, Structure, Union, Interface:** number of non-empty and non-comment code lines of the class, including the non-empty and non-comment code lines of its local methods, anonymous, local, and nested classes.

  **Namespace:** number of non-empty and non-comment code lines of the namespace, including its subnamespaces.

  **Component:** number of non-empty and non-comment code lines of the component, including its subcomponents.

#### Calculated
- Class
- Component
- Enum
- Function
- Interface
- Method
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of non-empty and non-comment code lines of the method, including the non-empty and non-comment lines of its anonymous classes.

  **Class, Structure:** number of non-empty and non-comment code lines of the class, including the non-empty and non-comment code lines of its local methods, anonymous and nested classes.

  **Namespace:** number of non-empty and non-comment code lines of the namespace, including its subnamespaces.

  **Component:** number of non-empty and non-comment code lines of the component, including its subcomponents.

#### Calculated
- Class
- Component
- Delegate
- Enum
- Interface
- Method
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method**: number of non-empty and non-comment code lines of the method, including the non-empty and non-comment lines of its anonymous and local classes.

  **Class:** number of non-empty and non-comment code lines of the class, including the non-empty and non-comment code lines of its local methods, anonymous, local, and nested classes.

  **Package:** number of non-empty and non-comment code lines of the package, including its subpackages.

  **Component:** number of non-empty and non-comment code lines of the component, including its subcomponents.

#### Calculated
- Annotation
- Class
- Component
- Enum
- Interface
- Method
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of non-empty and non-comment code lines of the method/function, including the non-empty and non-comment lines of its nested functions.

  **Class:** number of non-empty and non-comment code lines of the class, including the non-empty and non-comment code lines of its nested and local classes.

  **Component:** number of non-empty and non-comment code lines of the component, including its subcomponents.

#### Calculated
- Class
- Component
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method / Function:** number of non-empty and non-comment code lines of the method/function, including the non-empty and non-comment lines of its nested functions.

  **Class:** number of non-empty and non-comment code lines of the class, including the non-empty and non-comment code lines of its nested and local classes.

  **Module:** number of non-empty and non-comment code lines of the module.

  **Package:** number of non-empty and non-comment code lines of the package, including its subpackages.

  **Component:** number of non-empty and non-comment code lines of the component, including its subcomponents.

#### Calculated
- Class
- Component
- Function
- Method
- Module
- Package


## TLOC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Lines of Code
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of code lines of the method, including empty and comment lines, as well as its anonymous and local classes.

  **Class, Structure, Union, Interface:** number of code lines of the class, including empty and comment lines, as well as its local methods, anonymous, local, and nested classes.

  **Namespace:** number of code lines of the namespace, including empty and comment lines, as well as its subnamespaces.

  **Component:** number of code lines of the component, including empty and comment lines, as well as its subcomponents.

#### Calculated
- Class
- Component
- Enum
- Function
- Interface
- Method
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of code lines of the method, including empty and comment lines, as well as its anonymous classes.

  **Class, Structure:** number of code lines of the class, including empty and comment lines, as well as its local methods, anonymous and nested classes.

  **Namespace:** number of code lines of the namespace, including empty and comment lines, as well as its subnamespaces.

  **Component:** number of code lines of the component, including empty and comment lines, as well as its subcomponents.

#### Calculated
- Class
- Component
- Delegate
- Enum
- Interface
- Method
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method**: number of code lines of the method, including empty and comment lines, as well as its anonymous and local classes.

  **Class:** number of code lines of the class, including empty and comment lines, as well as its local methods, anonymous, local, and nested classes.

  **Package:** number of code lines of the package, including empty and comment lines, as well as its subpackages.

  **Component:** number of code lines of the component, including empty and comment lines, as well as its subcomponents.

#### Calculated
- Annotation
- Class
- Component
- Enum
- Interface
- Method
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of code lines of the method/function, including empty and comment lines, as well as its nested functions.

  **Class:** number of code lines of the class, including empty and comment lines, as well as its nested and local classes.

  **Component:** number of code lines of the component, including empty and comment lines, as well as its subcomponents.

#### Calculated
- Class
- Component
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method / Function:** number of code lines of the method/function, including empty and comment lines, as well as its nested functions.

  **Class:** number of code lines of the class, including empty and comment lines, as well as its nested and local classes.

  **Module:** number of code lines of the module, including empty and comment lines.

  **Package:** number of code lines of the package, including empty and comment lines, as well as its subpackages.

  **Component:** number of code lines of the component, including empty and comment lines, as well as its subcomponents.

#### Calculated
- Class
- Component
- Function
- Method
- Module
- Package


## TNA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Attributes
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of attributes in the class, including the inherited ones, as well as the inherited and local attributes of its nested, anonymous and local classes.

  **Namespace:** number of attributes in the namespace, including the attributes of its subnamespaces.

  **Component:** number of attributes in the component, including the attributes of its subcomponents.

#### Calculated
- Class
- Component
- Enum
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of attributes in the class, including the inherited ones and generated ones backing auto properties, as well as the inherited and local attributes of its nested and anonymous classes.

  **Namespace:** number of attributes in the namespace, including the attributes of its subnamespaces.

  **Component:** number of attributes in the component, including the attributes of its subcomponents.

#### Calculated
- Class
- Component
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of attributes in the class, including the inherited ones, as well as the inherited and local attributes of its nested, anonymous and local classes.

  **Package:** number of attributes in the package, including the attributes of its subpackages.

  **Component:** number of attributes in the component, including the attributes of its subcomponents.

#### Calculated
- Annotation
- Class
- Component
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Class:** number of attributes in the class, including the inherited ones, as well as the inherited and local attributes of its nested and local classes.

  **Component:** number of attributes in the component, including the attributes of its subcomponents.

#### Calculated
- Class
- Component

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of attributes in the class, including the inherited ones, as well as the inherited and local attributes of its nested and local classes.

  **Module:** number of attributes in the module.

  **Package:** number of attributes in the package, including the attributes of its subpackages.

  **Component:** number of attributes in the component, including the attributes of its subcomponents.

#### Calculated
- Class
- Component
- Module
- Package


## TNCL
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Classes
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of classes in the namespace, including the classes of its subnamespaces.

  **Component:** number of classes in the component, including the classes of its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of classes in the namespace, including the classes of its subnamespaces.

  **Component:** number of classes in the component, including the classes of its subcomponents.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of classes in the package, including the classes of its subpackages.

  **Component:** number of classes in the component, including the classes of its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Component:** number of classes in the component, including the classes of its subcomponents.

#### Calculated
- Component

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Module:** number of classes in the module.

  **Package:** number of classes in the package, including the classes of its subpackages.

  **Component:** number of classes in the component, including the classes of its subcomponents.

#### Calculated
- Component
- Module
- Package


## TNDI
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Directories
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of directories that belong to the namespace, including the directories of its subnamespaces.

  **Component:** number of directories that belong to the component, including its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of directories that belong to the namespace, including the directories of its subnamespaces.

  **Component:** number of directories that belong to the component, including its subcomponents.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of directories that belong to the package, including the directories of its subpackages.

  **Component:** number of directories that belong to the component, including its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Component:** number of directories that belong to the component, including its subcomponents.

#### Calculated
- Component

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of directories that belong to the package, including the directories of its subpackages.

  **Component:** number of directories that belong to the component, including its subcomponents.

#### Calculated
- Component
- Package


## TNEN
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Enums
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of enums in the namespace, including the enums of its subnamespaces.

  **Component:** number of enums in the component, including the enums of its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of enums in the namespace, including the enums of its subnamespaces.

  **Component:** number of enums in the component, including the enums of its subcomponents.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of enums in the package, including the enums of its subpackages.

  **Component:** number of enums in the component, including the enums of its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## TNFI
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Files
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of files that belong to the namespace, including the files of its subnamespaces.

  **Component:** number of files that belong to the component, including its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of files that belong to the namespace, including the files of its subnamespaces.

  **Component:** number of files that belong to the component, including its subcomponents.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of files that belong to the package, including the files of its subpackages.

  **Component:** number of files that belong to the component, including its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Component:** number of files that belong to the component, including its subcomponents.

#### Calculated
- Component

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of files that belong to the package, including the files of its subpackages.

  **Component:** number of files that belong to the component, including its subcomponents.

#### Calculated
- Component
- Package


## TNG
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Getters
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of getter methods in the class, including the inherited ones, as well as the inherited and local getter methods of its nested, anonymous and local classes.

  **Namespace:** number of getter methods in the namespace, including the getter methods of its subnamespaces.

  **Component:** number of getter methods in the component, including the getter methods of its subcomponents.

#### Calculated
- Class
- Component
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of getter methods in the class, including the inherited ones, as well as the inherited and local getter methods of its nested and anonymous classes.

  **Namespace:** number of getter methods in the namespace, including the getter methods of its subnamespaces.

  **Component:** number of getter methods in the component, including the getter methods of its subcomponents.

#### Calculated
- Class
- Component
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of getter methods in the class, including the inherited ones, as well as the inherited and local getter methods of its nested, anonymous and local classes.

  **Package:** number of getter methods in the package, including the getter methods of its subpackages.

  **Component:** number of getter methods in the component, including the getter methods of its subcomponents.

#### Calculated
- Annotation
- Class
- Component
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of getter methods in the class, including the inherited ones, as well as the inherited and local getter methods of its nested, anonymous and local classes.

  **Component:** number of getter methods in the component, including the getter methods of its subcomponents.

#### Calculated
- Class
- Component

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class
- Component
- Module
- Package


## TNIN
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Interfaces
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of interfaces in the namespace, including the interfaces of its subnamespaces.

  **Component:** number of interfaces in the component, including the interfaces of its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of interfaces in the namespace, including the interfaces of its subnamespaces.

  **Component:** number of interfaces in the component, including the interfaces of its subcomponents.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of interfaces in the package, including the interfaces of its subpackages.

  **Component:** number of interfaces in the component, including the interfaces of its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## TNLA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Local Attributes
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) attributes in the class, including the attributes of its nested, anonymous, and local classes.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) attributes in the class, including the generated ones backing auto properties and also attributes of its nested and anonymous classes.

#### Calculated
- Class
- Component
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) attributes in the class, including the attributes of its nested, anonymous, and local classes.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) attributes in the class, including the attributes of its nested and local classes.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) attributes in the class, including the attributes of its nested and local classes.

#### Calculated
- Class


## TNLG
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Local Getters
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) getter methods in the class, including the local getter methods of its nested, anonymous, and local classes.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) getter methods in the class, including the local getter methods of its nested and anonymous classes.

#### Calculated
- Class
- Component
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) getter methods in the class, including the local getter methods of its nested, anonymous, and local classes.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) getter methods in the class, including the local getter methods of its nested, anonymous, and local classes.

#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class


## TNLM
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Local Methods
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) methods in the class, including the local methods of its nested, anonymous, and local classes.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) methods in the class, including the local methods of its nested and anonymous classes.

#### Calculated
- Class
- Component
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) methods in the class, including the local methods of its nested, anonymous, and local classes.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) methods in the class, including the local methods of its nested and local classes.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) methods in the class, including the local methods of its nested and local classes.

#### Calculated
- Class


## TNLPA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Local Public Attributes
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) public attributes in the class, including the local public attributes of its nested, anonymous, and local classes.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) public attributes in the class, including the generated ones backing public auto properties and also local public attributes of its nested and anonymous classes.

#### Calculated
- Class
- Component
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) public attributes in the class, including the local public attributes of its nested, anonymous, and local classes.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class


## TNLPM
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Local Public Methods
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) public methods in the class, including the local methods of its nested, anonymous, and local classes.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) public methods in the class, including the local methods of its nested and anonymous classes.

#### Calculated
- Class
- Component
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) public methods in the class, including the local methods of its nested, anonymous, and local classes.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class


## TNLS
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Local Setters
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** number of local (i.e. not inherited) setter methods in the class, including the local setter methods of its nested, anonymous, and local classes.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of local (i.e. not inherited) setter methods in the class, including the local setter methods of its nested and anonymous classes.

#### Calculated
- Class
- Component
- Interface
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) setter methods in the class, including the local setter methods of its nested, anonymous, and local classes.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of local (i.e. not inherited) setter methods in the class, including the local setter methods of its nested, anonymous, and local classes.

#### Calculated
- Class

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class


## TNM
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Methods
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of methods in the class, including the inherited ones, as well as the inherited and local methods of its nested, anonymous, and local classes. Methods that override abstract methods are not counted.

  **Namespace:** number of methods in the namespace, including the methods of its subnamespaces.

  **Component:** number of methods in the component, including the methods of its subcomponents.

#### Calculated
- Class
- Component
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of methods in the class, including the inherited ones, as well as the inherited and local methods of its nested and anonymous classes. Methods that override abstract methods are not counted.

  **Namespace:** number of methods in the namespace, including the methods of its subnamespaces.

  **Component:** number of methods in the component, including the methods of its subcomponents.

#### Calculated
- Class
- Component
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of methods in the class, including the inherited ones, as well as the inherited and local methods of its nested, anonymous, and local classes. Methods that override abstract methods are not counted.

  **Package:** number of methods in the package, including the methods of its subpackages.

  **Component:** number of methods in the component, including the methods of its subcomponents.

#### Calculated
- Annotation
- Class
- Component
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of methods in the class, including the inherited ones, as well as the inherited and local methods of its nested, anonymous, and local classes.

  **Component:** number of methods in the component, including the methods of its subcomponents.

#### Calculated
- Class
- Component

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of methods/functions in the class, including the inherited ones, as well as the inherited and local methods of its nested and local classes. Methods that override abstract methods are not counted.

  **Package:** number of methods in the module.

  **Package:** number of methods in the package, including the methods of its subpackages.

  **Component:** number of methods in the component, including the methods of its subcomponents.

#### Calculated
- Class
- Component
- Module
- Package


## TNOS
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Statements
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of statements in the method, including the statements of its anonymous and local classes.

  **Class, Structure, Union:** number of statements in the class, including the statements of its nested, anonymous, and local classes.

  **Namespace:** number of statements in the namespace, including the statements of its subnamespaces.

  **Component:** number of statements in the component, including the statements of its subcomponents.

#### Calculated
- Class
- Component
- Function
- Method
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of statements in the method, including the statements of its anonymous classes.

  **Class, Structure:** number of statements in the class, including the statements of its nested and anonymous classes.

  **Namespace:** number of statements in the namespace, including the statements of its subnamespaces.

  **Component:** number of statements in the component, including the statements of its subcomponents.

#### Calculated
- Class
- Component
- Method
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method:** number of statements in the method, including the statements of its anonymous and local classes.
  **Class:** number of statements in the class, including the statements of its nested, anonymous, and local classes.
  **Package:** number of statements in the package, including the statements of its subpackages.
  **Component:** number of statements in the component, including the statements of its subcomponents.

#### Calculated
- Annotation
- Class
- Component
- Enum
- Interface
- Method
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method, Function:** number of statements in the method/function, including the statements of its nested functions.Class: number of statements in the class, including the statements of its nested and local classes.Component: number of statements in the component, including the statements of its subcomponents.

#### Calculated
- Class
- Component
- Function
- Method

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Method/Function:** number of statements in the method/function, including the statements of its nested functions.**Class:** number of statements in the class, including the statements of its nested and local classes.**Module:** number of statements in the module.**Package:** number of statements in the package, including the statements of its subpackages.**Component:** number of statements in the component, including the statements of its subcomponents.

#### Calculated
- Class
- Component
- Function
- Method
- Module
- Package


## TNPA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Public Attributes
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of public attributes in the class, including the inherited ones, as well as the inherited and local public attributes of its nested, anonymous, and local classes.

  **Namespace:** number of public attributes in the namespace, including the public attributes of its subnamespaces.

  **Component:** number of public attributes in the component, including the public attributes of its subcomponents.

#### Calculated
- Class
- Component
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of public attributes in the class, including the inherited ones and the generated ones backing public auto properties as well as the inherited and local public attributes of its nested and anonymous classes.

  **Namespace:** number of public attributes in the namespace, including the public attributes of its subnamespaces.

  **Component:** number of public attributes in the component, including the public attributes of its subcomponents.

#### Calculated
- Class
- Component
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of public attributes in the class, including the inherited ones, as well as the inherited and local public attributes of its nested, anonymous, and local classes.

  **Package:** number of public attributes in the package, including the public attributes of its subpackages.

  **Component:** number of public attributes in the component, including the public attributes of its subcomponents.

#### Calculated
- Annotation
- Class
- Component
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class
- Component
- Module
- Package


## TNPCL
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Public Classes
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of public classes in the namespace, including the public classes of its subnamespaces.

  **Component:** number of public classes in the component, including the public classes of its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of public classes in the namespace, including the public classes of its subnamespaces.

  **Component:** number of public classes in the component, including the public classes of its subcomponents.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of public classes in the package, including the public classes of its subpackages.

  **Component:** number of public classes in the component, including the public classes of its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Component
- Module
- Package


## TNPEN
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Public Enums
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of public enums in the namespace, including the public enums of its subnamespaces.

  **Component:** number of public enums in the component, including the public enums of its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of public enums in the namespace, including the public enums of its subnamespaces.

  **Component:** number of public enums in the component, including the public enums of its subcomponents.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of public enums in the package, including the public enums of its subpackages.

  **Component:** number of public enums in the component, including the public enums of its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## TNPIN
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Public Interfaces
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of public interfaces in the namespace, including the public interfaces of its subnamespaces.

  **Component:** number of public interfaces in the component, including the public interfaces of its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of public interfaces in the namespace, including the public interfaces of its subnamespaces.

  **Component:** number of public interfaces in the component, including the public interfaces of its subcomponents.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of public interfaces in the package, including the public interfaces of its subpackages.

  **Component:** number of public interfaces in the component, including the public interfaces of its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## TNPKG
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Packages
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of subnamespaces in the namespace, including all directly or indirectly contained subnamespaces.

  **Component:** number of namespaces and subnamespaces that belong to the component, including its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of subnamespaces in the namespace, including all directly or indirectly contained subnamespaces.

  **Component:** number of namespaces and subnamespaces that belong to the component, including its subcomponents.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of subpackages in the package, including all directly or indirectly contained subpackages.

  **Component:** number of packages and subpackages that belong to the component, including its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of subpackages in the package, including all directly or indirectly contained subpackages.

  **Component:** number of packages and subpackages that belong to the component, including its subcomponents.

#### Calculated
- Component
- Package


## TNPM
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Public Methods
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of public methods in the class, including the inherited ones, as well as the inherited and local public methods of its nested, anonymous, and local classes.

  **Namespace:** number of public methods in the namespace, including the public methods of its subnamespaces.

  **Component:** number of public methods in the component, including the public methods of its subcomponents.

#### Calculated
- Class
- Component
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of public methods in the class, including the inherited ones, as well as the inherited and local public methods of its nested and anonymous classes.

  **Namespace:** number of public methods in the namespace, including the public methods of its subnamespaces.

  **Component:** number of public methods in the component, including the public methods of its subcomponents.

#### Calculated
- Class
- Component
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of public methods in the class, including the inherited ones, as well as the inherited and local public methods of its nested, anonymous, and local classes.

  **Package:** number of public methods in the package, including the public methods of its subpackages.

  **Component:** number of public methods in the component, including the public methods of its subcomponents.

#### Calculated
- Annotation
- Class
- Component
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class
- Component
- Module
- Package


## TNPST
### Default
#### Enabled=false
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Public Structures
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of public structures in the namespace, including the public structures of its subnamespaces.

  **Component:** number of public structures in the component, including the public structures of its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of public structures in the namespace, including the public structures of its subnamespaces.

  **Component:** number of public structures in the component, including the public structures of its subcomponents.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## TNPUN
### Default
#### Enabled=false
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Public Unions
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of public unions in the namespace, including the public unions of its subnamespaces.

  **Component:** number of public unions in the component, including the public unions of its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  Placeholder


### java -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## TNS
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Setters
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Union, Interface:** number of setter methods in the class, including the inherited ones, as well as the inherited and local setter methods of its nested, anonymous and local classes.

  **Namespace:** number of setter methods in the namespace, including the setter methods of its subnamespaces.

  **Component:** number of setter methods in the component, including the setter methods of its subcomponents.

#### Calculated
- Class
- Component
- Interface
- Namespace
- Structure
- Union

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** number of setter methods in the class, including the inherited ones, as well as the inherited and local setter methods of its nested and anonymous classes.

  **Namespace:** number of setter methods in the namespace, including the setter methods of its subnamespaces.

  **Component:** number of setter methods in the component, including the setter methods of its subcomponents.

#### Calculated
- Class
- Component
- Interface
- Namespace
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of setter methods in the class, including the inherited ones, as well as the inherited and local setter methods of its nested, anonymous and local classes.

  **Package:** number of setter methods in the package, including the setter methods of its subpackages.

  **Component:** number of setter methods in the component, including the setter methods of its subcomponents.

#### Calculated
- Annotation
- Class
- Component
- Enum
- Interface
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** number of setter methods in the class, including the inherited ones, as well as the inherited and local setter methods of its nested, anonymous and local classes.

  **Component:** number of setter methods in the component, including the setter methods of its subcomponents.

#### Calculated
- Class
- Component

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Class
- Component
- Module
- Package


## TNST
### Default
#### Enabled=false
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Structures
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of structures in the namespace, including the structures of its subnamespaces.

  **Component:** number of structures in the component, including the structures of its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  Placeholder

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## TNUN
### Default
#### Enabled=false
#### NumericType=true
#### Warning=false
#### DisplayName=Total Number of Unions
#### Tags
- /general/Size
- /internal/csv_column
- /internal/metric_group/Size
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  Placeholder

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=false
#### Warning=false
#### HelpText
  Placeholder


### java -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=false
#### Warning=false
### python -> Default
#### Enabled=false
#### Warning=false

## TPDA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Public Documented API
#### Tags
- /general/Documentation
- /internal/csv_column
- /internal/metric_group/Documentation
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of documented public classes and methods in the namespace, including the documented public classes and methods of its subnamespaces.

  **Component:** number of documented public classes and methods in the component, including the documented public classes and methods of its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** the number of the public documented classes and their public documented methods found in the namespace. When calculating the metric, classes and methods found in subnamespaces of the namespace are also taken into account.

  **Component:** the number of public documented classes and public documented methods found in the component, where in calculating the metric, classes and methods to be found in subcomponents of the component are also taken into account.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of documented public classes and methods in the package, including the documented public classes and methods of its subpackages.

  **Component:** number of documented public classes and methods in the component, including the documented public classes and methods of its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Component:** number of documented classes and methods in the component, including the documented classes and methods of its subcomponents.

#### Calculated
- Component

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Component
- Module
- Package


## TPUA
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Total Public Undocumented API
#### Tags
- /general/Documentation
- /internal/csv_column
- /internal/metric_group/Documentation
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** number of undocumented public classes and methods in the namespace, including the undocumented public classes and methods of its subnamespaces.

  **Component:** number of undocumented public classes and methods in the component, including the undocumented public classes and methods of its subcomponents.

#### Calculated
- Component
- Namespace

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Namespace:** the number of the public undocumented classes and their public undocumented methods found in the namespace. When calculating the metric, classes and methods found in subnamespaces of the namespace are also taken into account.

  **Component:** the number of public undocumented classes and public undocumented methods found in the component, where in calculating the metric, classes and methods to be found in subcomponents of the component are also taken into account.

#### Calculated
- Component
- Namespace

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Package:** number of undocumented public classes and methods in the package, including the undocumented public classes and methods of its subpackages.

  **Component:** number of undocumented public classes and methods in the component, including the undocumented public classes and methods of its subcomponents.

#### Calculated
- Component
- Package

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Component:** number of undocumented classes and methods in the component, including the undocumented classes and methods of its subcomponents.

#### Calculated
- Component

### python -> Default
#### Enabled=false
#### Warning=false
#### Calculated
- Component
- Module
- Package


## WMC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=false
#### DisplayName=Weighted Methods per Class
#### Tags
- /general/Complexity
- /internal/csv_column
- /internal/metric_group/Complexity
- /tool/SourceMeter/MET

#### Settings
- Max=0
- Min=0

### cpp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure, Interface:** complexity of the class expressed as the number of independent control flow paths in it. It is calculated as the sum of the McCabe's Cyclomatic Complexity (McCC) values of its local methods.

#### Calculated
- Class
- Interface
- Structure

### csharp -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class, Structure:** complexity of the class expressed as the number of independent control flow paths in it. It is calculated as the sum of the McCabe’s Cyclomatic Complexity (McCC) values of its local methods.

#### Calculated
- Class
- Structure

### java -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** complexity of the class expressed as the number of independent control flow paths in it. It is calculated as the sum of the McCabe’s Cyclomatic Complexity (McCC) values of its local methods and init blocks.

#### Calculated
- Annotation
- Class
- Enum
- Interface

### javascript -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** complexity of the class expressed as the number of independent control flow paths in it. It is calculated as the sum of the McCabe’s Cyclomatic Complexity (McCC) values of its local methods.

#### Calculated
- Class

### python -> Default
#### Enabled=true
#### Warning=false
#### HelpText
  **Class:** complexity of the class expressed as the number of independent control flow paths in it. It is calculated as the sum of the McCabe’s Cyclomatic Complexity (McCC) values of its local methods.

#### Calculated
- Class
