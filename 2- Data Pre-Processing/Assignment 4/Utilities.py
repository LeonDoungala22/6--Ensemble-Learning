#!/usr/bin/env python
# coding: utf-8

# In[2]:



def read_txt(file_name):
    ##Data_description = np.loadtxt("dataset_description.txt", dtype=int)
    #get file object
    f = open(file_name , "r")

    while(True):
        #read next line
        line = f.readline()
        #if line is empty, you are done with all lines in the file
        if not line:
            break
        #you can access the line
        print(line.strip())

    #close file
    f.close


def DataAnalisis(Dataset ):
    Dataset = 0 ;
    #Dataset description
    print("Dataset description : \n")
    Dataset.describe()
   #mode 
    print("Mode : \n")
    Dataset.mode()
    


# In[ ]:




