# import all modules from connect.py
from connect import *

def update_record():
    try: 
        dbCon, dbCursor = db_access()

        #check to see if filmID exists
        film_id = int(input("Enter the FilmID to delete a record: "))
        dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (film_id,))

        # invoke the fetchone method and assign it to a variable called row
        row = dbCursor.fetchone()

        if row == None: # Using none object to check if the value exists or not
            print(f"No record with filmID {film_id} in the tblFilms table.")
        
        else:
            film_title = input("Enter updated film title: ")
            film_yearReleased = int(input("Enter updated film year of release: "))
            film_rating = input("Enter updated film rating: ")
            film_duration = int(input("Enter updated film duration: "))
            film_genre = input("Enter updated film genre: ")

            #perform update
            dbCursor.execute(f"UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ? WHERE filmID = ? ", (film_title,film_yearReleased,film_rating,film_duration,film_genre,film_id,))
            #Commit updates
            dbCon.commit()
            print(f"Record {film_id} updated successfully")

    except sql.ProgrammingError as e:
        print(f"Update error: {e}")

if __name__ == "__main__":
    update_record()


