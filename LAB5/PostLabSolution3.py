# This File contains the Solution to the Machine Problem 3

# Module Imports
import sqlite3 as sql3

# Wait Function
def wait_for_proceed(log):
    print(str(log))
    usri = str(input('[Type \'prcd\' to Proceed] >> ')).strip()
    if usri.upper() == 'PRCD':
        pass
    else:
        raise SystemExit
    
# Script Function
def read_sql_script(script_path):
    # Type Check
    if type(script_path) != str:
        raise TypeError('The input path is not of type \'str\'!')
    script = open(script_path, 'r')
    query = script.read()
    script.close()
    return query

# Program Main Function
def main():
    # Create Database
    atDB = sql3.connect('PostLabSolution3.db')
    wait_for_proceed('Connected to the Database.')

    # Create Cursor
    atDB_ptr = atDB.cursor()
    
    # Create Table
    atDB_ptr.execute(read_sql_script('PostLabSolution3Queries/MakeTables.sql'))
    atDB.commit()
    wait_for_proceed('Applied Create Table Script.')

    # Create Entry
    atDB_ptr.execute(read_sql_script('PostLabSolution3Queries/CreateEntry.sql'))
    atDB.commit()
    atDB_ptr.execute('SELECT * FROM ADVENTURE_TRIP')
    db_table = atDB_ptr.fetchall()
    for row in db_table: # Show Select
        print(row)
    wait_for_proceed('Applied Create Entry Script')

    # Drop Table
    atDB_ptr.execute('DROP TABLE ADVENTURE_TRIP')
    atDB.commit()
    wait_for_proceed('Dropped Table.')    

# Program Entry Point
if __name__ == '__main__':
    main()