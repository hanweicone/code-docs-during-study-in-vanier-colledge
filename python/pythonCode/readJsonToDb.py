import re
import json
import pymysql
# Create a connection object


databaseServerIP = "127.0.0.1"  # IP address of the MySQL database server

databaseUserName = "root"  # User name of the database server

databaseUserPassword = ""  # Password for the database user

newDatabaseName = "FINAL"  # Name of the database that is to be created

charSet = "utf8mb4"  # Character set

cusrorType = pymysql.cursors.DictCursor

connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,

                                     charset=charSet, cursorclass=cusrorType)

try:

    # Create a cursor object

    cursorInsatnce = connectionInstance.cursor()

    # SQL Statement to create a database

    sqlStatement = "CREATE DATABASE " + newDatabaseName

    # Execute the create database SQL statment through the cursor instance

    cursorInsatnce.execute(sqlStatement)


except Exception as e:

    print("Exeception occured:{}".format(e))

finally:

    connectionInstance.close()

cnx = pymysql.connect(user='root', password='',
                               host='127.0.0.1',
                               database='FINAL')
sql_table = "CREATE TABLE students (gender ENUM ('M','F') NOT NULL, student_id INT NOT NULL," \
            " last_name  VARCHAR(16) NOT NULL, first_name  VARCHAR(14)" \
            " NOT NULL,  PRIMARY KEY (student_id))"
try:
    cur = cnx.cursor()
    cur.execute(sql_table)
except Exception as e:
    print("Exeception occured:{}".format(e))
finally:
    cur.close()

cnx = pymysql.connect(user='root', password='',
                               host='127.0.0.1',
                               database='FINAL')
cur = cnx.cursor()
f = open('data.txt', 'r')
json_data = '['+f.read().replace('(','{').replace(')','},').rstrip(',')+']'
json_list = eval(json_data)
#sql = "insert into students values ('{gender:s}',{student_id:d},'{last_name:s}','{first_name:s}');"
sql = "insert into students values ('{gender}',{student_id},'{last_name}','{first_name}');"
for x in json_list:

    try:
        cur.execute(sql.format(**x))
        cnx.commit()
        print('values ({gender:s},{student_id:d},{last_name:s},{first_name:s}) inserted'.format(**x))
    except Exception as e:
        print("Exeception occured:{}".format(e))



    # str1 = f.read().strip("()")
    # str_list = re.split('\)\(', str1)
    #for x in str_list:
        #try:
            #str1 = '{'+x+'}'
            #jdict = json.loads(str1)
            #sql2 =str(list(jdict.values())).strip("[]").replace("u",'')
            #sql2 = str(list(jdict.values())).strip("[]")
            #print(sql2)
            #sql = "insert into " + "students" + " values (" + sql2 + ");"
            #cur.execute(sql)
            #cnx.commit()
        #except Exception as e:
            #print("Exeception occured:{}".format(e))
#except Exception as e:
    #print("Exeception occured:{}".format(e))







