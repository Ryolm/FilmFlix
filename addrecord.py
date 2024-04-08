# import all modules from connect.py
from connect import *

#function to inset records in table
def insert_record():
    try:
        dbCon, dbCursor = db_access()

        #inputs for user to insert data
        film_title = input("Enter film title: ")
        film_yearReleased = int(input("Enter film year of release: "))
        film_rating =  input("Enter film rating: ")
        film_duration = int(input("Enter film duration "))
        film_genre = input("Enter film genre ")

        #sql statement to insert data into their respective vars
        dbCursor.execute("INSERT INTO tblFilms VALUES(NULL,?,?,?,?,?)",(film_title,film_yearReleased,film_rating,film_duration,film_genre))

        #commit the records to the table in database/
        dbCon.commit()
        print(f"{film_title} inserted into the Films table")

    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    
    except sql.Error as er:
        print(f"Error: {er}")

if __name__ == "__main__":
    insert_record()