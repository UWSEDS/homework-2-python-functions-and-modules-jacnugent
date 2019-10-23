'''
Homework 2
Jacqueline Nugent
'''

import pandas as pd

##### Task 1 #####
def create_dataframe_url(url):
    df = pd.read_csv(url)
    return df

##### Task 2 #####
def test_create_dataframe(df, colnames):
    
    ### test for columns ###
    argNames = True
    # test if the list and dataframe have the same number of columns
    if len(df.columns) == len(colnames):
        # loop through the data frame columns, and stop if any are NOT in the given list
        for col in df.columns:
            if col not in colnames:
                argNames = False
                break
    else:
        argNames = False   
 
    ### test for same type within each column ###
    sameType = True
    for col in df.columns:
        # if the type of a column is "object," check if each entry 
        # has the same data type as the previous
        if df[col].dtype == 'O':
            for i in range(1,len(df[col])):
                if type(df[col][i]) != type(df[col][i-1]):
                    sameType = False
                    break
        
    ### test for 10 rows ###
    if (df.shape[0] >= 10):
        tenRows = True
    else:
        tenRows = False
        
    ### function returns true if all three conditions are met ###
    if argNames == True and sameType == True and tenRows == True:
        func = True
    else:
        func = False
        
    return func 
