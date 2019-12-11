import pymysql


def importCSV(cursor, filepath, table):
    import csv
    allData = csv.reader(open(filepath), delimiter=',', quotechar='\'')
    l1 = next(allData)
    sql1 = ','.join(l1)
    for row in allData:
        sql2 = str(row).strip('[]')
        sql = "insert into " + table + " (" + sql1 + ") " + "values (" + sql2 + ");"
        cursor.execute(sql)
        print(sql)

cnx = pymysql.connect(user='root', password='',
                               host='127.0.0.1',
                               database='employees')

cur = cnx.cursor()
table = 'employees'
filepath = "C:/Users/hanwe/Downloads/Data/1.employees.csv"
table1 = "departments"
filepath1 = "C:/Users/hanwe/Downloads/Data/2.departments.csv"
table2 = "dept_manager"
filepath2 = "C:/Users/hanwe/Downloads/Data/3.dept_manager.csv"
table3 = "dept_emp"
filepath3 = "C:/Users/hanwe/Downloads/Data/4.dept_emp.csv"
table4 = "salaries"
filepath4 = "C:/Users/hanwe/Downloads/Data/5.salaries.csv"
table5 = "titles"
filepath5 = "C:/Users/hanwe/Downloads/Data/6.titles.csv"
importCSV(cur, filepath, table)
importCSV(cur, filepath1, table1)
importCSV(cur, filepath2, table2)
importCSV(cur, filepath3, table3)
importCSV(cur, filepath4, table4)
importCSV(cur, filepath5, table5)
cnx.commit()
cur.close()
cnx.close()



