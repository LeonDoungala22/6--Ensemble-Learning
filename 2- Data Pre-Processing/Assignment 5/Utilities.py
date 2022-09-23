from yapf.yapflib.yapf_api import FormatCode

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno
import json

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder 
from sklearn.preprocessing import PowerTransformer

from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline

import pickle
from scipy.stats import norm
import warnings
warnings.filterwarnings("ignore")




def read_txt(file_name):
    import codecs
    ##Data_description = np.loadtxt("dataset_description.txt", dtype=int)
    #get file object
    f = codecs.open(file_name, "r", errors="ignore")
   
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



        
        

