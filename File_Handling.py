'''
File Handling:
---->File Handler is an object od file to maintain several functions of file such as creating, reading, writing and update also deleting the file.

How to open a file: there are two ways
1.open() (if we open the file with open keyword then we must the use keyword close to close the file).
---> This open() function takes 2 parameters and in this we have to close the file by calling close() function after program.
1.file name
2.Mode:Modes("r","w","a","x","t"):

1."r"-->To read the file we will use this mode an dif the doesn't exist . it will through the error.
any = open("demo.txt","r")
print(any.read())
any.close()

2."w" -->TO write the text into the file wwe will use this mode and it will create the file if it doesn't exist.
It will overwrite the data in it.
any = open("demo.txt","w")
any.write("Hello! Teja")
any.write("I am studying in Codegnan")
any.close()

3."a" --> To add the text into the file this is used and it will create th efile if it doesn't exist.
any = open("demo.txt","a")
any.write("we are done with read and write mode")
any.close()

4."x" ---> This is used to create the new file. 
any = open("some","x")
any.write("This is a file")
any.close()

To read a file These are the methods:
1.read()--->
This method can read the entire file chunk by chunk we can also specify the size.
any = open("demo.txt","r")
print(any.read(10))
any.close()

2.readline()----->
This method can only read one line at a time.
any = open("demo.txt","r")
print(any.readline())
any.close()

3.readlines()------->
This method can read the entire file and return into list with each line is one index in the list.
any = open("demo.txt","r")
print(any.readlines())
any.close()

import os 
os.remove("demo.text")

2.with open() (Here it will close the file manually when we use with open()).

'''
