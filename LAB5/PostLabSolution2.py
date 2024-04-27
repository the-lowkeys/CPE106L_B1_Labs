# This is the solution to the PostLab2 for Lab5, using existing code from PostLab3

# Module Imports
import sqlite3 as sql3
import PostLabSolution3 as pls3

# Main Function
def main():
    # Make Database and Cursor
    sqlynk = sql3.connect('PostLabSolution2.db')
    lynkcursor = sqlynk.cursor()
    pls3.wait_for_proceed('Created Database.')

    # Trigger Tables
    script = pls3.read_sql_script('PostLabSolution2Queries/MakeTables.sql')
    script = script.split(';')
    script.pop(-1) # Remove Trailing Space
    for query in script:
        query = query.strip() + ';'
        lynkcursor.execute(query)
    pls3.wait_for_proceed('Executed Scripts.')

# Entry Point
if __name__ == '__main__':
    main()