from flask import Flask, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
from tkinter import Button, Entry, Frame, Label, ttk

import tkinter as tk
from tkinter.constants import END
import bluetooth 
import mysql.connector
from tkinter import messagebox

app = Flask(__name__)
#code for connection
#MySQL Hostname
app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
#MySQL username
app.config['MYSQL_USER'] = 'sql6427260'
#MySQL password here in my case password is null so i left empty
app.config['MYSQL_PASSWORD'] = 'cZayPVNPww'
#Database name In my case database name is projectreporting
app.config['MYSQL_DB'] = 'sql6427260'

mysql = MySQL(app)

@app.route('/')
@app.route('/projectlist',methods=['GET','POST'])
def projectlist():
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("TRUNCATE `bluetooth`")

    mySql_insert_query = """INSERT INTO bluetooth (name, address) 
                           VALUES (%s, %s) """

    nearByDevices = bluetooth.discover_devices(lookup_names=True)

    for address, name in nearByDevices:

        records_to_insert = [( name, address)]

        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.executemany(mySql_insert_query, records_to_insert)
        mysql.connection.autocommit(True)
    #creating variable for connection
    
    #executing query
    cursor.execute("select * from bluetooth")
    #fetching all records from database
    data=cursor.fetchall()
    #returning back to projectlist.html with all records from MySQL which are stored in variable data
    return render_template("projectlist.html",data=data)

@app.route('/save',methods=['GET','POST'])
def save():
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("TRUNCATE `bluetooth`")

    mySql_insert_query = """INSERT INTO bluetoothsave (name, address) 
                           VALUES (%s, %s) """

    nearByDevices = bluetooth.discover_devices(lookup_names=True)

    for address, name in nearByDevices:

        records_to_insert = [( name, address)]

        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.executemany(mySql_insert_query, records_to_insert)
        mysql.connection.autocommit(True)
    #creating variable for connection
    
    #executing query
    cursor.execute("select * from bluetoothsave")
    #fetching all records from database
    data=cursor.fetchall()
    #returning back to projectlist.html with all records from MySQL which are stored in variable data
    return render_template("save.html",data=data)

@app.route('/saved',methods=['GET','POST'])
def saved():
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
    #creating variable for connection
    
    #executing query
    cursor.execute("select * from bluetoothsave")
    #fetching all records from database
    data=cursor.fetchall()
    #returning back to projectlist.html with all records from MySQL which are stored in variable data
    return render_template("saved.html",data=data)
if __name__ == '__main__':
    app.run(port=5000,debug=True)