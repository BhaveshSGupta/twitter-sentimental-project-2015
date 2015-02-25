#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","TEST" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO SUMMARY(ECOM_CODE,
         NAME, TOTAL_TWEET, POS_TWEET, NEG_TWEET)
         VALUES ('ECOM_01', 'FLIPKART',1000, 500, 500)"""
cursor.execute(sql)
sql = """INSERT INTO SUMMARY(ECOM_CODE,
         NAME, TOTAL_TWEET, POS_TWEET, NEG_TWEET)
         VALUES ('ECOM_02', 'Amazon',1000, 500, 500)"""
cursor.execute(sql)
sql = """INSERT INTO SUMMARY(ECOM_CODE,
         NAME, TOTAL_TWEET, POS_TWEET, NEG_TWEET)
         VALUES ('ECOM_03', 'Snapdeal',1000, 500, 500)"""

"""


sql = CREATE TABLE SUMMARY (
         ECOM_CODE  CHAR(20) NOT NULL,
         NAME  CHAR(20),
         TOTAL_TWEET INT,
         POS_TWEET INT,
         NEG_TWEET INT )"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   print "he"
   db.rollback()

# disconnect from server
db.close()
