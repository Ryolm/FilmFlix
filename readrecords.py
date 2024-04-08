from connect import *

#function to read records from a table in database.
def read_records():
    try:
        dbCursor = db_access()[1]

        dbCursor.execute("SELECT * FROM tblFilms")

        all_records = dbCursor.fetchall()

        if all_records:

            print("*" * 100)
            print(f"filmID{'':<3}|title{'':<25}|yearRelease{'':<4}|rating{'':<3}|duration{'':<3}|genre{'':<10}")
            print("*" * 100)

            for aRecord in all_records:
                print(f"{aRecord[0]:<9}|{aRecord[1]:<30}|{aRecord[2]:<15}|{aRecord[3]:<9}|{aRecord[4]:<11}|{aRecord[5]:<10}")
                print("-" * 100)
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
if __name__ == "__main__":
    read_records()