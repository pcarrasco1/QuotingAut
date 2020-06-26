import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import numpy as np
gc = gspread.oauth()
 


def readData():
    sh = gc.open("quotingProjectAutomation")
    print(sh.sheet1.get('A1'))
    worksheet = sh.sheet1
    df = get_as_dataframe(worksheet, header= 0)
    print(df)


    



    
readData()



