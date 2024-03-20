**CPSC 323 Project 1**

**Documentation:**

**FSADesign.docx**
This file contains a diagram of the FSA design that was used to acquire the acceptable states.
Also contains the regular expressions that contains samples of expressions that would lead to acceptable
states in our FSA Design

**input_sourcecode.txt**
This file contains the code that will be examined by the python source code.
Code can be changed and would output their appropriate tokens and lexemes
in th output file.

**main.py**
Main portion of the python source code that will read the input code and produce
two columns, tokens and lexemes, into the output file

**lexer.py**
Supporting code that contains the class "Lexer" that will assist the main source code
in identifying the proper tokens and lexemes taken from input_sourcecode.txt

**output.txt**
Output file where the resulting tokens and lexemes determined by the main source code will
be written into two separate columns, tokens and lexemes.

**How to Run Program:**
1. Insert code that you want to analyze into input_sourcecode.txt file
2. Run the program
3. Check output.txt file or terminal to identify the results of the analyzed code