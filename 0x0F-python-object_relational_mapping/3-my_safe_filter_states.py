#!/usr/bin/python3
"""
python script that displays all states from the database hbtn_0e_0_usa where 
name matches the argument and is safe from MySQL injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    records = cursor.fetchall()
    for record in records:
      if record[1] == argv[4]:
        print(record)
    cursor.close()
    db.close()
