READ ME

This program is made in Python and decisionTree is the starting of the program in Windows platform.
I have used Python 2.7 as the Python interpreter.

Thus it will be compiled by the following command.

python -u decisionTree.py 

Following files are there along with this code
1)train.dat
2)train-1.dat
3)train-2.dat
4)train-3.dat
5)test.dat
6)test-1.dat
7)test-2.dat
8)test-3.dat

As the program starts put the corresponding training filename when the user is asked to write the filename
 and the corresponding testing file name as the user is asked to write the filename
 
 Example:
 Please enter name of train file - 
 train.dat
 Please enter name of test file -
 test.dat 
 
 The getFiles.py gets the training and testing files that are input by user and which are there in the directory.
 
 The recursive.py recursively finds the splitting attribute and makes recursion till the class label is not found.
 
 The entropy.py files calculates the entropy and information gain of each attribute
  and then takes the best gain as the splitting attribute.
  
  