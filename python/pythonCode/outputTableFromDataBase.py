# works on python 3.8

import pymysql
cnx = pymysql.connect(user='root', password='',
                                host='127.0.0.1',
                                database='employees')
cur = cnx.cursor()


# function to print table without using format string
def print_table(cursor, sql):
    cursor.execute(sql)
    descriptions = cursor.description
    column_names = []
    for i in range(len(descriptions)):  # get column name list
        lens = len(descriptions[i][0][:19])
        column_names.append(
            '|' + ' ' * ((20 - lens) // 2) + descriptions[i][0][:19] + ' ' * (20 - (lens + ((20 - lens) // 2))))
    str_headers = ''.join(column_names) + '|'
    print('='*len(str_headers))
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
    print('=' * len(str_headers))


# function to output table  use format string
def output_table(cursor, sql, filename):
    cursor.execute(sql)
    descriptions = cursor.description
    column_names1 = []
    format_template = ['|{:^20}'] * len(descriptions)
    for i in range(len(descriptions)):
        column_names1.append(descriptions[i][0][:19])
    str_headers = ''.join(format_template).format(*column_names1) + '|'
    f = open(filename, 'w')
    f.write('=' * len(str_headers)+'\n')
    f.write(str_headers+'\n')
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
    f.write('=' * len(str_headers)+'\n')
    f.close()


sql = "select * from employees limit 5;"
sql1 = "select min(A.dept_name) as name, count(*) as total from departments" \
       " A inner join dept_emp B on A.dept_no=B.dept_no group by A.dept_no;"
print_table(cur, sql)
print_table(cur, sql1)
ss= 'test_out_table.txt'
ss1 = 'test_out_table1.txt'
output_table(cur, sql, ss)
output_table(cur, sql1, ss1)
cnx.close()
