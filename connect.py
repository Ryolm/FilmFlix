# importing sqlite3 module and giving alias 'sql
import sqlite3 as sql 

# Creating function for database access
def db_access():
    try:  
        # invoke sqlite connect method and assign alias dbCon
        with sql.connect("filmflix.db") as dbCon:
            # creating var called dbCursor, initalise with cursor method from connect function
            dbCursor = dbCon.cursor()
            return dbCon, dbCursor
    except sql.OperationalError as e: #raise sqlerror 
        print(f"Connection failed: {e}")
    
if __name__ == "__main__":
    db_access()
    print(f"Connection successful")