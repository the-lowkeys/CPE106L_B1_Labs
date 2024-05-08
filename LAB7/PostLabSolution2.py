"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")
    print("Input:" )
    print(frame)
    frame = cleanStats(frame)
    print("Cleaned: ")
    print(frame)
    HoopStatsView(frame)

def cleanStats(frame):
    unfmtd_clmns = [frame['FG'], frame['3PT'], frame['FT']]
    frame = frame.drop(['FG', '3PT', 'FT'], axis=1)
    
    for column in unfmtd_clmns:
        column = pd.DataFrame(column)    
        colname = str(column.columns.tolist()[0]) # Get column name
        cleancols = [] # final clean columns
        
        # get new column names
        colnames = [colname + 'M', colname + 'A']
        for entry in column.itertuples(): # process each entry
            value = str(tuple(entry)[-1]) #get string entry
            values = value.split('-') # split with delimiter
            cleancols.append(values)
        cleancols = pd.DataFrame(cleancols, columns=colnames)
        # naming find cascade
        index = frame.columns.tolist().index(colname[0:2] + '%')
        print(index)
        frame.insert(index, colnames[0], cleancols[colnames[0]])
        frame.insert(index + 1, colnames[1], cleancols[colnames[1]])
    return frame

if __name__ == "__main__":
    main()
