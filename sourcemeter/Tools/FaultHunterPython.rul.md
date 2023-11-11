# ToolDescription
## Default
### ID=FaultHunterPython
### Description
  FaultHunter is the coding rule violation checker module of SourceMeter for Python. This module makes it possible to identify common Python coding rule violations in the code (so-called bad practices) in a similar way as provided by the pylint, pyflakes, pychecker or pep8 tools. However, the algorithms implemented in the FaultHunter module work on the precise Abstract Semantic Graph of SourceMeter which results in higher precision and recall compared to other tools with a rougher syntactic analyzer.

  FaultHunter implements many pep8[^4] guidelines, but it also provides additional checks that are not present in pep8.

# Includes
- FaultHunterPython.rul_metadata.md

# Metrics
## FHPY_AAI
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=__all__ After Imports
#### WarningText
  Put any relevant __all__ specification after the imports.

#### HelpText
  Put any relevant \_\_all\_\_ specification after the imports.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Variable Rules

#### Settings
- Max=0
- Min=0
- Priority=Minor


## FHPY_BE
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Bare Except
#### WarningText
  You shouldn't use bare excepts.

#### HelpText
  If you really want to catch all exceptions, then use 'except Exception:', but it is many times better to only trap exceptions that you expect. A bare 'except:' clause will catch SystemExit and KeyboardInterrupt exceptions, making it harder to interrupt a program with Control-C, and can disguise other problems.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Exception Rules
- /collection/PEP8/Programming Recommendations
- /collection/The Little Book of Python Anti-Patterns/No exception type(s) specified
- /collection/The Little Book of Python Anti-Patterns/Bad except clauses order
- /collection/Pylint/bare-except (W0702)
- /collection/Pylint/bad-except-order (E0701)

#### Settings
- Max=0
- Min=0
- Priority=Major


## FHPY_BT
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Big Try
#### WarningText
  The length of a try block is %. The length (LLOC) of the try block should be smaller than % lines.

#### HelpText
  For all try/except clauses, limit the 'try' clause to the absolute minimum amount of code necessary. This avoids masking bugs.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Design Rules
- /collection/PEP8/Programming Recommendations

#### Settings
- Max=10
- Min=0
- Priority=Major


## FHPY_BoC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Bool Compare
#### WarningText
  Don't compare boolean values to True or False using '==' or 'is'

#### HelpText
  Don't compare boolean values to True or False using '==' or 'is'


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Basic Rules
- /collection/PEP8/Programming Recommendations
- /collection/The Little Book of Python Anti-Patterns/Comparing things to True the wrong way
- /collection/Pylint/singleton-comparison (C0121)

#### Settings
- Max=0
- Min=0
- Priority=Major


## FHPY_DA
### Default
#### Enabled=false
#### NumericType=true
#### Warning=true
#### DisplayName=Define __all__
#### WarningText
  If you are writing a module, you should always define __all__.

#### HelpText
  Modules that are designed for use via "from M import \*" should use the \_\_all\_\_ mechanism to prevent exporting globals, or use the older convention of prefixing such globals with an underscore (which you might want to do to indicate these globals are "module non-public").


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Variable Rules
- /collection/PEP8/Global Variable Names

#### Settings
- Max=0
- Min=0
- Priority=Minor


## FHPY_DDV
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Dangerous Default Value
#### WarningText
  You mustn't use mutable objects (like dictionaries or lists) as default arguments.

#### HelpText
  Default arguments are created on parsing, not when a function/method is called. You mustn't use mutable objects (like dictionaries or lists) as default arguments.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Basic Rules
- /collection/The Little Book of Python Anti-Patterns/Using a mutable default value as an argument
- /collection/Pylint/dangerous-default-value (W0102)

#### Settings
- Max=0
- Min=0
- Priority=Major


## FHPY_LTL
### Default
#### Enabled=false
#### NumericType=true
#### Warning=true
#### DisplayName=Line Too Long
#### WarningText
  The maximum line length should be 79 characters.

#### HelpText
  Limit all lines to a maximum of 79 characters.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Format Rules
- /collection/PEP8/Maximum Line Length

#### Settings
- Max=79
- Min=0
- Priority=Minor


## FHPY_MS
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Multiple Statements
#### WarningText
  Multiple statements per line should be avoided.

#### HelpText
  Multiple statements per line should be avoided.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Format Rules
- /collection/PEP8/Other Recommendations
- /collection/Pylint/multiple-statements (C0321)

#### Settings
- Max=0
- Min=0
- Priority=Major


## FHPY_MeN
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Method Naming
#### WarningText
  Function/method names should also be lowercase with underscores to separate words.

#### HelpText
  Function/method names should also be lowercase with underscores to separate words.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Basic Rules
- /collection/PEP8/Function and Variable Names
- /collection/PEP8/Method Names and Instance Variables
- /collection/The Little Book of Python Anti-Patterns/Using CamelCase in function names

#### Settings
- Max=0
- Min=0
- Priority=Minor


## FHPY_MoN
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Module Naming
#### WarningText
  Module names should be lowercase with underscores instead of spaces.

#### HelpText
  Module names should be lowercase with underscores instead of spaces.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Basic Rules
- /collection/PEP8/Package and Module Names

#### Settings
- Max=0
- Min=0
- Priority=Minor


## FHPY_NoC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=None Comparison
#### WarningText
  Comparisons to singletons like None should always be done with 'is' or 'is not', never the equality operators.

#### HelpText
  Comparisons to singletons like None should always be done with 'is' or 'is not', never the equality operators. This is because None is a singleton and the identity test is more efficient than testing for equality.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Basic Rules
- /collection/PEP8/Programming Recommendations
- /collection/The Little Book of Python Anti-Patterns/Comparing things to None the wrong way
- /collection/Pylint/singleton-comparison (C0121)

#### Settings
- Max=0
- Min=0
- Priority=Major


## FHPY_OC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Object Comparison
#### WarningText
  Object type comparisons should always use isinstance() instead of comparing types directly.

#### HelpText
  Object type comparisons should always use isinstance() instead of comparing types directly.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Basic Rules
- /collection/PEP8/Programming Recommendations
- /collection/The Little Book of Python Anti-Patterns/Using type() to compare types
- /collection/Pylint/unidiomatic-typecheck (C0123)

#### Settings
- Max=0
- Min=0
- Priority=Major


## FHPY_ORS
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Old Raise Syntax
#### WarningText
  When raising an exception, the form "raise ValueError('message')" should be used instead of the older form "raise ValueError, 'message'".

#### HelpText
  The parentheses-using form is preferred because when the exception arguments are long or include string formatting, you don't need to use line continuation characters thanks to the containing parentheses.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Python3 Rules
- /collection/PEP8/Programming Recommendations
- /collection/Pylint/old-raise-syntax (E1604)

#### Settings
- Max=0
- Min=0
- Priority=Critical


## FHPY_OSC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Old Style Class
#### WarningText
  Classes should inherit from object.

#### HelpText
  If a class has no base classes, then it is better to make it a new style class by inheriting from object.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Newstyle Rules
- /collection/Pylint/old-style-class (C1001)

#### Settings
- Max=0
- Min=0
- Priority=Major


## FHPY_RI
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Relative Import
#### WarningText
  You shouldn't use relative imports. Always use the absolute package path for all imports.

#### HelpText
  Relative imports for intra-package imports are highly discouraged. Always use the absolute package path for all imports.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Import Rules
- /collection/PEP8/Imports
- /collection/Pylint/relative-beyond-top-level (E0402)
- /collection/Pylint/relative-import (W0403)

#### Settings
- Max=0
- Min=0
- Priority=Minor


## FHPY_RS
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Raising String
#### WarningText
  You should use class-based exceptions instead of string exceptions.

#### HelpText
  String exceptions in new code are forbidden, because this language feature is being removed in Python 2.6. Modules or packages should define their own domain-specific base exception class, which should be subclassed from the built-in Exception class.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Python3 Rules
- /collection/PEP8/Programming Recommendations
- /collection/Pylint/raising-string (W1625)
- /collection/Pylint/raising-bad-type (E0702)

#### Settings
- Max=0
- Min=0
- Priority=Critical


## FHPY_SFC
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Sequence False Checking
#### WarningText
  For sequences, (strings, lists, tuples), use the fact that empty sequences are false.

#### HelpText
  For sequences, (strings, lists, tuples), use the fact that empty sequences are false. Method of usage should be: if not seq: or if seq:


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Basic Rules
- /collection/PEP8/Programming Recommendations
- /collection/Pylint/assert-on-tuple (W0199)

#### Settings
- Max=0
- Min=0
- Priority=Major


## FHPY_SI
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Single Import
#### WarningText
  Imports should usually be on separate lines.

#### HelpText
  Imports should usually be on separate lines.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Import Rules
- /collection/PEP8/Imports
- /collection/Pylint/multiple-imports (C0410)

#### Settings
- Max=0
- Min=0
- Priority=Minor


## FHPY_SSP
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=String Slicing Prefix
#### WarningText
  Use ''.startswith() instead of string slicing to check for prefixes.

#### HelpText
  Use ''.startswith() instead of string slicing to check for prefixes. The startswith() is cleaner and less error prone.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/String Rules
- /collection/PEP8/Programming Recommendations

#### Settings
- Max=0
- Min=0
- Priority=Major


## FHPY_SSS
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=String Slicing Suffix
#### WarningText
  Use ''.endswith() instead of string slicing to check for suffixes.

#### HelpText
  Use ''.endswith() instead of string slicing to check for suffixes. The endswith() is cleaner and less error prone.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/String Rules
- /collection/PEP8/Programming Recommendations

#### Settings
- Max=0
- Min=0
- Priority=Major


## FHPY_TI
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Top Import
#### WarningText
  You should place imports at the top of modules.

#### HelpText
  Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Import Rules
- /collection/PEP8/Imports
- /collection/Pylint/wrong-import-position (C0413)

#### Settings
- Max=0
- Min=0
- Priority=Major


## FHPY_WI
### Default
#### Enabled=true
#### NumericType=true
#### Warning=true
#### DisplayName=Wildcard Import
#### WarningText
  Never use 'from xxx import *'.

#### HelpText
  Even for importing a lot of names it is better to be able to see where your names come from. Tools like pylint and PyFlakes can help warn you about unused imports.


#### Tags
- /tool/SourceMeter/FaultHunterPython
- /general/Import Rules
- /collection/PEP8/Imports
- /collection/The Little Book of Python Anti-Patterns/using wildcard imports (from ... import *)
- /collection/Pylint/wildcard-import (W0401)

#### Settings
- Max=0
- Min=0
- Priority=Major
