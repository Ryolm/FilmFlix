# import necessary modules from flask and sqlite3
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# initialize your flask app
app = Flask(__name__)

# define a function to connect to your sqlite database
def db_access():
    connection = sqlite3.connect('filmflix.db')  # connect to the database named filmflix.db
    cursor = connection.cursor()  # create a cursor object to interact with the database
    return connection, cursor  # return both connection and cursor

# define the route for your homepage
@app.route('/')
def index():
    conn, cursor = db_access()  # get database connection and cursor
    cursor.execute("SELECT * FROM tblFilms")  # execute SQL query to select all records from tblFilms
    records = cursor.fetchall()  # fetch all records from the query result
    conn.close()  # close the database connection
    return render_template('index.html', records=records)  # render index.html template passing the records

# define the route for adding a film record, supporting both GET and POST requests
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':  # if the form has been submitted
        conn, cursor = db_access()
        # insert form data into the database
        cursor.execute("INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)",
                       (request.form['title'], request.form['yearReleased'], request.form['rating'], request.form['duration'], request.form['genre']))
        conn.commit()  # commit the transaction
        conn.close()  # close the database connection
        return redirect(url_for('index'))  # redirect back to the homepage
    return render_template('add.html')  # if request is GET, show the add record form

# define the route for deleting a film record, supporting both GET and POST requests
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':  # if the form has been submitted
        conn, cursor = db_access()
        # execute SQL query to delete the record with the given filmID
        cursor.execute("DELETE FROM tblFilms WHERE filmID = ?", (request.form['filmID'],))
        conn.commit()  # commit the transaction
        conn.close()  # close the database connection
        return redirect(url_for('index'))  # redirect back to the homepage
    return render_template('delete.html')  # if request is GET, show the delete record form

# define the route for updating a film record, supporting both GET and POST requests
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':  # if the form has been submitted
        conn, cursor = db_access()
        # execute SQL query to update the record with the given form data
        cursor.execute("UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ? WHERE filmID = ?",
                       (request.form['title'], request.form['yearReleased'], request.form['rating'], request.form['duration'], request.form['genre'], request.form['filmID']))
        conn.commit()  # commit the transaction
        conn.close()  # close the database connection
        return redirect(url_for('index'))  # redirect back to the homepage
    return render_template('update.html')  # if request is GET, show the update record form

# define the route for generating a report, supporting both GET and POST requests
@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':  # if the form has been submitted
        search_field = request.form['search_field']  # get the field to search by from the form
        search_value = request.form['search_value']  # get the value to search for from the form
        conn, cursor = db_access()
        # execute SQL query to find records that match the search criteria
        query = f"SELECT * FROM tblFilms WHERE {search_field} LIKE ?"
        cursor.execute(query, ('%' + search_value + '%',))
        records = cursor.fetchall()  # fetch all matching records
        conn.close()  # close the database connection
        # render report.html template passing the found records and search criteria
        return render_template('report.html', records=records, search_field=search_field, search_value=search_value)
    else:
        # if request is GET, show the report form without any records
        return render_template('report.html', records=[], search_field=None, search_value=None)

# run the app if this file is executed directly
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)