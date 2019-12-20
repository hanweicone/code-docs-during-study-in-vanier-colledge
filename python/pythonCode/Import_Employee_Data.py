import pymysql

_PATH = 'E:/DBClass/Data'

def importCSV(cursor,sql,file):
    import csv
    global _PATH

    with open('{0}/{1}.csv'.format(_PATH,file)) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='\'')
        i = 0
        for row in reader:
            i += 1
            print('Processing Line {0}'.format(i))
            cursor.execute(sql,row)

db=pymysql.connect(host='localhost',user='root',passwd='',db='employees')
db.autocommit(True)  # do not forget commit
cursor = db.cursor()

sql1 = 'INSERT INTO employees (emp_no,birth_date,first_name,last_name,gender,hire_date) ' \
      'VALUES (%(emp_no)s,%(birth_date)s,%(first_name)s,%(last_name)s,%(gender)s,%(hire_date)s)'
importCSV(cursor,sql1,'1.employees')

sql2 = 'INSERT INTO departments (dept_no,dept_name) ' \
      'VALUES (%(dept_no)s,%(dept_name)s)'
importCSV(cursor,sql2,'2.departments')

sql3 = 'INSERT INTO dept_manager (emp_no,dept_no,from_date,to_date) ' \
      'VALUES (%(emp_no)s,%(dept_no)s,%(from_date)s,%(to_date)s)'
importCSV(cursor,sql3,'3.dept_manager')


sql4 = 'INSERT INTO dept_emp (emp_no,dept_no,from_date,to_date) ' \
      'VALUES (%(emp_no)s,%(dept_no)s,%(from_date)s,%(to_date)s)'
importCSV(cursor,sql4,'4.dept_emp')


sql5 = 'INSERT INTO salaries (emp_no,salary,from_date,to_date) ' \
      'VALUES (%(emp_no)s,%(salary)s,%(from_date)s,%(to_date)s)'
importCSV(cursor,sql5,'5.salaries')

sql6 = 'INSERT INTO titles (emp_no,title,from_date,to_date) ' \
      'VALUES (%(emp_no)s,%(title)s,%(from_date)s,%(to_date)s)'
importCSV(cursor,sql6,'6.titles')

db.close()

# my way use auto generated sql
# cnx = pymysql.connect(user='root', password='',
#                               host='127.0.0.1',
#                               database='employees')
#
# cur = cnx.cursor()
# cur.execute("select database()")  # get db_name from cursor
# db_name = cur.fetchone()[0]
# print(db_name)
# # sql = '''
# # insert into employees(emp_no,birth_date,first_name,last_name,gender,hire_date)
# # values (%(emp_no)s,%(birth_date)s,%(first_name)s,%(last_name)s,%(gender)s,%(hire_date)s)
# # '''
# #with open('C:/Users/hanwe/Downloads/Data/1.employees.csv') as csvfile:
#   # reader = csv.reader(csvfile,delimiter = ',', quotechar='\'')
#     #for row in reader:
#
#         #sql = "INSERT INTO testSmall VALUES (%s);" % ', '.join('?' for _ in row)
#         # print('Inserting:{0}'.format(row['emp_no']))
#         # dict1 = {'emp_no':row['emp_no'], 'birth_date':row['birth_date'],'first_name':row['first_name'],'last_name':row['last_name'],'gender':row['gender'],'hire_date':row['hire_date']}
#         #cur.execute(sql, row)
# allData = csv.reader(open('C:/Users/hanwe/Downloads/Data/1.employees.csv'), delimiter=',', quotechar='\'')
# l1 = next(allData)
# sql1 = ','.join(l1)
# print('---------------')
# for row in allData:
#
# #     sql = "INSERT INTO employees VALUES (%s);" % ', '.join('?' for _ in row)
# #     sql = "insert into employees (emp_no,birth_date,first_name,last_name,gender,hire_date) values (%s, %s, %s,%s,%s,%s);"
#     #sql2 = ','.join(row)
#     sql2 = str(row).strip('[]')
#     sql = "insert into employees (" + sql1 + ")" + "values (" + sql2 + ");"
#     cur.execute(sql)
# cnx.commit()
# cur.close()
# cnx.close()
