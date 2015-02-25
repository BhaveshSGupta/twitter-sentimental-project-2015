#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","new" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS SUMMARY")
cursor.execute("DROP TABLE IF EXISTS TWEETS")

sql = """CREATE TABLE SUMMARY(
         ECOM_CODE  CHAR(20) NOT NULL PRIMARY KEY,
         NAME  CHAR(20),
         TOTAL_TWEET INT,
         POS_TWEET INT,
         NEG_TWEET INT )"""
# execute SQL query using execute() method.
cursor.execute(sql)

sql = """CREATE TABLE TWEETS(ID INT AUTO_INCREMENT PRIMARY KEY , ECOM_CODE  CHAR(20) NOT NULL,TEXT  CHAR(200),VALUE INT,SENTIMENT BOOL)"""
# execute SQL query using execute() method.
cursor.execute(sql)
    

    
sql = """INSERT INTO SUMMARY(ECOM_CODE,NAME, TOTAL_TWEET, POS_TWEET, NEG_TWEET)VALUES ('ECOM_01','FLIPKART',1000, 500, 500)"""
cursor.execute(sql)


sql="""INSERT INTO SUMMARY(ECOM_CODE, NAME, TOTAL_TWEET, POS_TWEET, NEG_TWEET)VALUES ('ECOM_02','AMAZON',1500, 5000, 4500)"""
cursor.execute(sql)


sql = """INSERT INTO SUMMARY(ECOM_CODE,NAME, TOTAL_TWEET, POS_TWEET, NEG_TWEET)VALUES ('ECOM_03', 'SNAPDEAL',10030, 5040, 532400)"""
cursor.execute(sql)

db.commit()
# disconnect from server
db.close()
