# Analog_Devices_Project
This Python program takes a directory as a required argument () and a filename extension as optional argument that defaults to “.txt”. The program locate all files with the given extension in the given directory and all its subdirectories to produce a list of all matching files with the numbers of lines within the file. The program also output the total number of lines and the average number of lines per file. 
The arguments of the program is  
```
  --ext EXT, -e EXT  file extension
  --dir DIR, -d DIR  name of directory.
```  
The program can run in this way:  
```
python parser.py -e txt -d tests 
```
And the result is  
```
tests/a2/fa2.txt        7
tests/a1/a11/fa2.txt    9
tests/a1/fa2.txt        6
tests/fa1.txt           3
==============================
Number of files found: 4
Total number of lines: 25
Average lines per file: 6.25
```  
The unit test is under the test.py and can run with 
```
python test.py    
```  
