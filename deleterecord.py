# import all modules from connect.py
from connect import *

# function to delete records
def delete_record():
    try:
        dbCon, dbCursor = db_access()

        #check to see if filmID exists
        film_id = int(input("Enter the FilmID to delete a record: "))
        dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (film_id,))
        # invoke the fetchone method and assign it to a variable called row
        row = dbCursor.fetchone()

        if row == None: # Using none object to check if the value exists or not
            print(f"No record with filmID {film_id} in the tblFilms table.")
        else: # if there is a match with filmID provided run
            dbCursor.execute("DELETE FROM tblFilms WHERE filmID = ?", (film_id,))
            dbCon.commit()

            print(f"Record {film_id} deleted from the tblFilms table")
        # error exception
    except sql.ProgrammingError as e:
        print("Delete operation failed: {e}")
if __name__ == "__main__":
    delete_record()