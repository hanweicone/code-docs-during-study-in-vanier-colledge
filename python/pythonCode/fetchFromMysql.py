#http://zetcode.com/python/pymysql/

import pymysql
#import pymysql.cursors

sql = 'select * from employees'


sql2 = "SELECT `COLUMN_NAME` \
FROM `INFORMATION_SCHEMA`.`COLUMNS` \
WHERE `TABLE_SCHEMA`='employees' \
    AND `TABLE_NAME`='employees';"

sql3 = "SELECT `COLUMN_NAME` \
FROM `INFORMATION_SCHEMA`.`COLUMNS` \
WHERE `TABLE_NAME`='employees';"

# cnx = pymysql.connect(user='root', password='',
#                                host='127.0.0.1',
#                                database='employees',
# 			                    charset='utf8mb4',
#                                cursorclass=pymysql.cursors.DictCursor)#use column name to get value
cnx = pymysql.connect(user='root', password='',
                                host='127.0.0.1',
                                database='employees')
cur = cnx.cursor()

# cur.execute(sql)
# descriptions = cur.description
#
# column_names = []
# for i in range(len(descriptions)):  # get column name list
#     lens = len(descriptions[i][0][:19])
#     column_names.append('|'+' '*((20-lens)//2)+descriptions[i][0][:19]+' '*(20-(lens+((20-lens)//2))))
# print(''.join(column_names)+'|')
# rows = cur.fetchall()
#
# for row in rows:
#     row_string = []
#
#     for x in range(len(row)):
#
#         lens = len(str(row[x])[:19])
#         if str(row[x]).isnumeric():
#             row_string.append('|'+' '*(20-lens)+str(row[x])[:19])
#         else:
#             row_string.append('|'+str(row[x])[:19]+' '*(20-lens))
#     print(''.join(row_string)+'|')
#
# column_names1 = []
# format_template = ['|{:^20}']*len(descriptions)
# for i in range(len(descriptions)):
#     column_names1.append(descriptions[i][0][:19])
# print(''.join(format_template).format(*column_names1)+'|')
#
# for row in rows:
#     row_string = []
#     row_format_template = []
#     for x in range(len(row)):
#         row_string.append(str(row[x]))
#         if str(row[x]).isnumeric():
#             row_format_template.append('|{:>20}')
#         else:
#             row_format_template.append('|{:<20}')
#     print(''.join(row_format_template).format(*row_string)+'|')


# function to print table not use format string
def print_table(cursor, sql):
    cursor.execute(sql)
    descriptions = cursor.description
    column_names = []
    for i in range(len(descriptions)):  # get column name list
        lens = len(descriptions[i][0][:19])
        column_names.append(
            '|' + ' ' * ((20 - lens) // 2) + descriptions[i][0][:19] + ' ' * (20 - (lens + ((20 - lens) // 2))))
    str_headers = ''.join(column_names) + '|'
    print('_'*len(str_headers))
    print(str_headers)
    rows = cursor.fetchall()

    for row in rows:
        row_string = []

        for x in range(len(row)):

            lens = len(str(row[x])[:19])
            if str(row[x]).isnumeric():
                row_string.append('|' + ' ' * (20 - lens) + str(row[x])[:19])
            else:
                row_string.append('|' + str(row[x])[:19] + ' ' * (20 - lens))
        print('-' * len(str_headers))
        print(''.join(row_string) + '|')
    print('-' * len(str_headers))


# function to print table  use format string
def output_table(cursor, sql, filename):
    cursor.execute(sql)
    descriptions = cursor.description
    column_names1 = []
    format_template = ['|{:^20}'] * len(descriptions)
    for i in range(len(descriptions)):
        column_names1.append(descriptions[i][0][:19])
    str_headers = ''.join(format_template).format(*column_names1) + '|'
    f = open(filename, 'w')
    f.write('_' * len(str_headers)+'\n')
    f.write(str_headers+'\n')
    #print('_' * len(str_headers))
    #print(str_headers)
    rows = cursor.fetchall()

    for row in rows:
        row_string = []
        row_format_template = []
        for x in range(len(row)):
            row_string.append(str(row[x]))
            if str(row[x]).isnumeric():
                row_format_template.append('|{:>20}')
            else:
                row_format_template.append('|{:<20}')
        f.write('-' * len(str_headers)+'\n')
        f.write(''.join(row_format_template).format(*row_string) + '|'+'\n')
    f.write('-' * len(str_headers)+'\n')

sql1 = "select min(A.dept_name) as name, count(*) as total from departments" \
       " A inner join dept_emp B on A.dept_no=B.dept_no group by A.dept_no;"
print_table(cur, sql1)
ss= 'test_out_table.txt'
output_table(cur,sql1,ss)
# while len(rows) > 0:
#     count = len(rows)
#     for row in rows:
#         print("ID={0}".format(row[0])+'  '+str(row[1]))
#     print("Finished {0}".format(count))
#     rows = cur.fetchmany(100)
'''
rows = cur.fetchall()
count = len(rows)
for row in rows:
    print("ID={0}".format(row['emp_no']))
'''   
# cur.execute(sql2)
# rows =cur.fetchall()
# for row in rows:
#     print(row)
#
#
#
# #get column name list by sql,not by cur.description
# cur.execute(sql3)
# rows =cur.fetchall()
# headlist = []
# for row in rows:
#    headlist.extend(row.values())
# print(headlist)

