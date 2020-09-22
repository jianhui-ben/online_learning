
## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os
import sys

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    l_path=[] ##save the output
    all_path= os.listdir(path)  ## open this path
    for p in all_path:  
        cur_path= os.path.join(path, p)
        if os.path.isfile(cur_path) and suffix in cur_path:  ## if it's a file and the name contain suffic
            l_path.append(cur_path.replace('\\', '/'))
        elif os.path.isdir(cur_path):
            l_path+= find_files(suffix, cur_path) ##call the recursion
    return l_path

## set up the initial path; previouly I was using anaconda so the default os path is not the same directory of this .py file
#init_path="C:/Users/ben29/OneDrive/Desktop/Udecity_python/submit"
#os.chdir(init_path)

###test case 1:
init_path= "."
suffix='.c'
output=find_files(suffix, init_path)

for i in output:
    print(i)


###test case 2:
init_path= "."
suffix=''  ## contain an empty string
output=find_files(suffix, init_path)

for i in output:  ##should return all the files
    print(i)

###test case 3: no suffic 
init_path= "./testdir_problem_2/testdir/subdir1"
suffix=''  ## this file is in subdir2 instead of subdir1
output=find_files(suffix, init_path)

for i in output:
    print(i)


###Helper
#init_path="C:/Users/ben29/OneDrive/Desktop/Udecity_python/P1/testdir_problem_2"
#fir=os.listdir(path)[0]
#os.listdir(os.path.join(init_path, fir, ''))
#l=os.path.join(init_path, fir)
#print(l)
#l.replace('\\', '/')
## Let us print the files in the directory in which you are running this script
#print (os.listdir("."))
## Let us check if this file is indeed a file!
#print (os.path.isfile("./ex.py"))
## Does the file end with .py?
#print ("./ex.py".endswith(".py"))

