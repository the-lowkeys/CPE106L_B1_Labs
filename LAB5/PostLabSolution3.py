# This File contains the Solution to the Machine Problem 3

# Module Imports
import sqlite3 as sql3

# Wait Function
def wait_for_proceed():
    usri = str(input('[Type \'prcd\' to Proceed] >> ')).strip()
    if usri.upper() == 'PRCD':
        pass
    elif usri.upper() == 'EXIT':
        raise SystemExit
    

# Program Main Function
def main():
    # Create Database
    atDB = sql3.connect('Database\PostLabSolution3.db')
    wait_for_proceed()


# Program Entry Point
if __name__ == '__main__':
    main()