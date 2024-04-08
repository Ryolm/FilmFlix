from connect import *
import sqlite3 as sql

def search_report():
    try:
        dbCon, dbCursor = db_access()

        print("Search by filmID, title, yearReleased, rating, genre")
        search_field = input("Please choose your search criteria: ").lower()

        if search_field == "filmid":
            value = int(input("Enter the FilmID: "))
            dbCursor.execute("SELECT * FROM tblfilms WHERE filmID = ?", (value,))
        elif search_field in ["title", "yearreleased", "rating", "genre"]:
            value = input(f"Enter the {search_field}: ")
            if search_field == "yearreleased":  # For exact matches like year
                dbCursor.execute(f"SELECT * FROM tblfilms WHERE {search_field} = ?", (value,))
            else:  # For partial matches like title, rating, genre
                dbCursor.execute(f"SELECT * FROM tblfilms WHERE {search_field} LIKE ?", (f"%{value}%",))
        else:
            print(f"Search criteria '{search_field}' is not valid.")
            return

        rows = dbCursor.fetchall()
        if rows:
            print("*" * 100)
            print(f"filmID{'':<3}|title{'':<25}|yearReleased{'':<15}|rating{'':<10}|duration{'':<10}|genre")
            print("*" * 100)
            for row in rows:
                print_film_details(row)
            print("-" * 100)
        else:
            print("No records found.")

    except sql.Error as e:
        print(f"Database operation failed: {e}")
    except ValueError:
        print("Invalid input. Please enter appropriate values.")

def print_film_details(record):
    # Print a single film record
    print(f"{record[0]:<6}|{record[1]:<30}|{record[2]:<15}|{record[3]:<10}|{record[4]:<10}|{record[5]}")

if __name__ == "__main__":
    search_report()
