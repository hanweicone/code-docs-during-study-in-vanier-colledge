Oracle Cursor用法总结
cursor分为三种，一是直接声明为cursor变量，二是首先声明类型再声明变量，三是声明为sys_refcursor。

（1）直接声明

declare

 cursor emp_cur  is select *  from emp;

 emp_record emp%rowtype;

begin 

 open emp_cur;

 loop 

  fetch emp_cur  into emp_record;

  exit when  emp_cur%notfound;

  dbms_output.put_line('name is:' || emp_record.ename ||' and sal is:' || emp_record.sal);

 end loop;

 close emp_cur;

end;

/

(2)ref cursor:分为强类型（有return子句的）和弱类型，强类型在使用时，其返回类型必须和return中的类型一致，否则报错，而弱类型可以随意打开任何类型。

例如：

强类型

declare

 type emp_cur_type  is ref cursor return emp%rowtype;

 emp_cur emp_cur_type;

 emp_record emp%rowtype;

begin

 open emp_cur  for select *  from  emp;

 loop

  fetch emp_cur  into emp_record;

  exit when emp_cur%notfound;

  dbms_output.put_line('name is:' ||  emp_record.ename || ' and sal is:' || emp_record.sal);

 end loop;

 close emp_cur;

 --open emp_cur for select * from dept; 错误的，类型不一致。

 --close emp_cur;

end;

/

弱类型：

declare

 type emp_cur_type is ref cursor;

 emp_cur emp_cur_type;

 emp_record emp%rowtype;

 dept_record dept%rowtype;

begin

 open emp_cur for select *  from emp;

 loop

  fetch emp_cur into emp_record;

  exit when emp_cur%notfound;

  dbms_output.put_line('name is:' || emp_record.ename || ' and sal is:' || emp_record.sal);

 end loop;

 close emp_cur;

 

 open emp_cur  for select *  from dept; --可再次打开，不同类型的

 loop

  fetch emp_cur  into dept_record;

  exit when emp_cur%notfound;

  dbms_output.put_line('dname is:' || dept_record.dname);

 end loop;

 close emp_cur;

end;

/

（3）sys_refcursor:可多次打开，直接声明此类型的变量，不用先定义类型再声明变量。

declare

 emp_cur sys_refcursor;

 emp_record emp%rowtype;

 dept_record dept%rowtype;

begin

 open emp_cur for select *  from emp;

 loop

  fetch emp_cur  into emp_record;

  exit when emp_cur%notfound;

  dbms_output.put_line('name is:' || emp_record.ename || ' and sal is:' || emp_record.sal);

 end loop;

 close emp_cur;

 

 open emp_cur  for select *  from dept; --可再次打开，不同类型的

 loop

  fetch emp_cur  into dept_record;

  exit when emp_cur%notfound;

  dbms_output.put_line('dname is:' || dept_record.dname);

 end loop;

 close emp_cur;

end;

/

其他总结：

1、游标可以用for循环，但只限于cursor cur_var is ……这种类型，用在其他的里面都是错误的；for本身就包含了打开、关闭游标，此时再显示打开关闭都是错误的。

declare

cursor emp_cur is select *  from emp;

begin

--open emp_cur; 是错误的，因为for本身就包含了打开、关闭

for emp_record in emp_cur

loop

   dbms_output.put_line('name is:' ||  emp_record.ename || ' and sal is:' || emp_record.sal);

end loop;

--close emp_cur; 是错误的，for本身包含了关闭。

end;

 

--是不是表示：ref cursor变量不支持for打开并循环？

declare

type emp_cur_type  is ref cursor return emp%rowtype;

emp_cur emp_cur_type;

begin

open emp_cur  for select *  from emp;--怎么都是错，for已经打开了。

for emp_record  in emp_cur -- 不管前面有没有打开语句，for都不承认这种类型

loop

   dbms_output.put_line('name is:' ||  emp_record.ename || ' and sal is:' || emp_record.sal);

end loop;

end;

2、游标可以带参数

DECLARE

  CURSOR c1 (job VARCHAR2, max_wage NUMBER) IS

    SELECT * FROM employees  WHERE job_id = job  AND salary > max_wage;

BEGIN

  FOR person  IN  c1('CLERK', 3000)

  LOOP

     DBMS_OUTPUT.PUT_LINE('Name = ' || person.last_name || ', salary = ' ||

                         person.salary || ', Job Id = ' || person.job_id );

  END LOOP;

END;

3、bulk collect批量赋值

declare

 type emp_cur_type  is ref cursor;

 emp_cur emp_cur_type;

 type name_list is table of emp.ename%type;

 type sal_list  is table of emp.sal%type;

 names name_list;

 sals sal_list;

begin

 open emp_cur for select ename,sal from emp;

 fetch emp_cur bulk collect into names,sals;

 close emp_cur;

 

 for i  in names.first .. names.last

 loop

  dbms_output.put_line('name is:'||names(i)||' and sal is:'||sals(i));

 end loop;

end;

/

4、cursor变量的位置

CREATE PACKAGE emp_data AS

  TYPE EmpCurTyp IS REF CURSOR RETURN employees%ROWTYPE;

-- emp_cv EmpCurTyp; -- not allowed

  PROCEDURE open_emp_cv;

END  emp_data;

/

CREATE PACKAGE BODY emp_data  AS

-- emp_cv EmpCurTyp; -- not allowed

PROCEDURE open_emp_cv  IS

  emp_cv EmpCurTyp; -- this is legal

  BEGIN

    OPEN emp_cv  FOR SELECT *  FROM  employees;

  END  open_emp_cv;

END  emp_data;

/

5、嵌套cursor

打开父cursor时，子cursor隐含打开；当

语法格式:cursor(subquery)

A   nested  cursor  is  implicitly  opened when  the  containing  row  is  fetched from  the  parent  cursor.

The  nested  cursor  is  closed  only  when:

The  nested  cursor  is  explicitly  closed by  the  user

The  parent  cursor  is  reexecuted

The  parent  cursor  is  closed

The  parent  cursor  is  canceled

示例；
declare

 type emp_cur_type  is ref cursor ;

 type dept_cur_type is ref cursor ;

 v_ename emp.ename%type;

 v_dname dept.dname%type;

 emp_cur emp_cur_type;

 dept_cur dept_cur_type;

begin

 open dept_cur  for

 select d.dname,

  cursor(select  e.ename  from  emp  e  where e.deptno=d.deptno )emps

 from dept d;

 loop

  fetch dept_cur into v_dname,emp_cur;

  exit when dept_cur%notfound;

  dbms_output.put_line('dname is : '||v_dname);

  loop

   fetch emp_cur into  v_ename;

   exit when emp_cur%notfound;

   dbms_output.put_line('--ename is : '||v_ename);

  end  loop;

 end  loop;

 close  dept_cur;

end;

If opportunity doesn’t knock, build a door
