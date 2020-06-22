import gspread

gc = gspread.oauth()

def readData():
    sh = gc.open("quotingProjectAutomation")
    print(sh.sheet1.get('A1'))

readData()



