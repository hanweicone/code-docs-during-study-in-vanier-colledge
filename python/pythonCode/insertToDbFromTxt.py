def insertDataToDB(new_database_name, new_table_name, file_path):
    import pymysql
    databaseServerIP = "127.0.0.1"  # IP address of the MySQL database server

    databaseUserName = "root"  # User name of the database server

    databaseUserPassword = ""  # Password for the database user

    charSet = "utf8mb4"  # Character set

    cusrorType = pymysql.cursors.DictCursor

    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,

                                         charset=charSet, cursorclass=cusrorType)


    cursor = connectionInstance.cursor()
    sqlStatement = "CREATE DATABASE " + new_database_name
    try:
        cursor.execute(sqlStatement)
        print('DATABASE: {0} created'.format(new_database_name))
        cursor.close()
        connectionInstance.close()
    except Exception as e:
        print("Exeception occured:{}".format(e))

    cnx = pymysql.connect(user=databaseUserName, password=databaseUserPassword,
                          host=databaseServerIP,
                          database=new_database_name)
    sql_table = "CREATE TABLE "+new_table_name + " (gender ENUM ('M','F') NOT NULL, student_id INT NOT NULL," \
                " last_name  VARCHAR(16) NOT NULL, first_name  VARCHAR(14)" \
                " NOT NULL,  PRIMARY KEY (student_id))"
    cur = cnx.cursor()
    try:
        cur.execute(sql_table)
        print('TABLE: {0} created'.format(new_table_name))
    except Exception as e:
        print("Exeception occured:{}".format(e))

    f = open(file_path, 'r')
    json_data = '[' + f.read().replace('(', '{').replace(')', '},').rstrip(',') + ']'
    json_list = eval(json_data)
    # sql = "insert into students values ('{gender:s}',{student_id:d},'{last_name:s}','{first_name:s}');"
    sql = "insert into students values ('{gender}',{student_id},'{last_name}','{first_name}');"
    for x in json_list:

        try:
            cur.execute(sql.format(**x))
            cnx.commit()
            print('values ({gender:s},{student_id:d},{last_name:s},{first_name:s}) inserted'.format(**x))
        except Exception as e:
            print("Exeception occured:{}".format(e))



insertDataToDB('FINAL', 'students', 'data.txt')