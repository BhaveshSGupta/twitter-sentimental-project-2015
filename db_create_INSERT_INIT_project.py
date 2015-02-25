#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS SUMMARY")

try:
    sql = """CREATE TABLE SUMMARY(
         ECOM_CODE  CHAR(20) NOT NULL,
         NAME  CHAR(20),
         TOTAL_TWEET INT,
         POS_TWEET INT,
         NEG_TWEET INT)"""
    cusor.execute(sql)
    print "created"

except:
    print "Database nt Created:"



try:
    sql = """INSERT INTO SUMMARY(ECOM_CODE,
         NAME, TOTAL_TWEET, POS_TWEET, NEG_TWEET)
         VALUES ('ECOM_01', 'FLIPKART',1000, 500, 500)"""
    cursor.execute(sql)
    print "added flipkart"
    sql = """INSERT INTO SUMMARY(ECOM_CODE,
         NAME, TOTAL_TWEET, POS_TWEET, NEG_TWEET)
         VALUES ('ECOM_02', 'AMAZON',1000, 500, 500)"""
    cursor.execute(sql)
    print "Added Amazon"
    sql = """INSERT INTO SUMMARY(ECOM_CODE,
         NAME, TOTAL_TWEET, POS_TWEET, NEG_TWEET)
         VALUES ('ECOM_03', 'SNAPDEAL',1000, 500, 500)"""
    cursor.execute(sql)
    print "Added Snapdeal"
    db.commit()
    
except:
    db.rollback()

db.close()
