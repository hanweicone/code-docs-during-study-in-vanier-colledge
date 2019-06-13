# oracle限制查询条数-rownum用法详解

对于rownum来说它是oracle系统顺序分配为从查询返回的行的编号，返回的第一行分配的是1，第二行是2，依此类推，这个伪字段可以用于限制查询返回的总行数，且rownum不能以任何表的名称作为前缀。

## (1) rownum 对于等于某值的查询条件
如果希望找到学生表中第一条学生的信息，可以使用rownum=1作为条件。但是想找到学生表中第二条学生的信息，使用rownum=2结果查不到数据。因为rownum都是从1开始，但是1以上的自然数在rownum做等于判断是时认为都是false条件，所以无法查到rownum = n（n>1的自然数）。
SQL> select rownum,id,name from student where rownum=1;（可以用在限制返回记录条数的地方，保证不出错，如：隐式游标）
SQL> select rownum,id,name from student where rownum =2; 
    ROWNUM ID     NAME
---------- ------ ---------------------------------------------------

## （2）rownum对于大于某值的查询条件
   如果想找到从第二行记录以后的记录，当使用rownum>2是查不出记录的，原因是由于rownum是一个总是从1开始的伪列，Oracle 认为rownum> n(n>1的自然数)这种条件依旧不成立，所以查不到记录。

查找到第二行以后的记录可使用以下的子查询方法来解决。注意子查询中的rownum必须要有别名，否则还是不会查出记录来，这是因为rownum不是某个表的列，如果不起别名的话，无法知道rownum是子查询的列还是主查询的列。
SQL>select * from(select rownum no ,id,name from student) where no>2;
        NO ID     NAME
---------- ------ ---------------------------------------------------
         3 200003 李三
         4 200004 赵四

## （3）rownum对于小于某值的查询条件
rownum对于rownum<n（(n>1的自然数）的条件认为是成立的，所以可以找到记录。
SQL> select rownum,id,name from student where rownum <3;
    ROWNUM ID     NAME
---------- ------ ---------------------------------------------------
        1 200001 张一
        2 200002 王二

查询rownum在某区间的数据，必须使用子查询。例如要查询rownum在第二行到第三行之间的数据，包括第二行和第三行数据，那么我们只能写以下语句，先让它返回小于等于三的记录行，然后在主查询中判断新的rownum的别名列大于等于二的记录行。但是这样的操作会在大数据集中影响速度。
SQL> select * from (select rownum no,id,name from student where rownum<=3 ) where no >=2;
        NO ID     NAME
---------- ------ ---------------------------------------------------
         2 200002 王二
         3 200003 李三

## （4）rownum和排序   
Oracle中的rownum的是在取数据的时候产生的序号，所以想对指定排序的数据去指定的rowmun行数据就必须注意了。
SQL> select rownum ,id,name from student order by name;
    ROWNUM ID     NAME
---------- ------ ---------------------------------------------------
         3 200003 李三
         2 200002 王二
         1 200001 张一
         4 200004 赵四
可以看出，rownum并不是按照name列来生成的序号。系统是按照记录插入时的顺序给记录排的号，rowid也是顺序分配的。为了解决这个问题，必须使用子查询；
SQL> select rownum ,id,name from (select * from student order by name);
    ROWNUM ID     NAME
---------- ------ ---------------------------------------------------
         1 200003 李三
         2 200002 王二
         3 200001 张一
         4 200004 赵四
这样就成了按name排序，并且用rownum标出正确序号（有小到大）
笔者在工作中有一上百万条记录的表，在jsp页面中需对该表进行分页显示，便考虑用rownum来作，下面是具体方法(每页显示20条)： 
“select * from tabname where rownum<20 order by name" 但却发现oracle却不能按自己的意愿来执行，而是先随便取20条记录，然后再order by，后经咨询oracle,说rownum确实就这样，想用的话，只能用子查询来实现先排序，后rownum，方法如下： 
"select * from (select * from tabname order by name) where rownum<20",但这样一来，效率会低很多。 
后经笔者试验，只需在order by 的字段上加主键或索引即可让oracle先按该字段排序，然后再rownum；方法不变：    “select * from tabname where rownum<20 order by name"

取得某列中第N大的行

select column_name from 
(select table_name.*,dense_rank() over (order by column desc) rank from table_name) 
where rank = &N； 
　假如要返回前5条记录：

　　select * from tablename where rownum<6;(或是rownum <= 5 或是rownum != 6) 
假如要返回第5-9条记录：

select * from tablename 
where … 
and rownum<10 
minus 
select * from tablename 
where … 
and rownum<5 
order by name 
选出结果后用name排序显示结果。(先选再排序)

注意：只能用以上符号(<、<=、!=)。

select * from tablename where rownum != 10;返回的是前９条记录。 
不能用：>,>=,=,Between...and。由于rownum是一个总是从1开始的伪列，Oracle 认为这种条件不成立。

另外，这个方法更快：

select * from ( 
select rownum r,a from yourtable 
where rownum <= 20 
order by name ) 
where r > 10 
这样取出第11-20条记录!(先选再排序再选)

要先排序再选则须用select嵌套：内层排序外层选。 
rownum是随着结果集生成的，一旦生成，就不会变化了；同时,生成的结果是依次递加的，没有1就永远不会有2! 
rownum 是在查询集合产生的过程中产生的伪列，并且如果where条件中存在 rownum 条件的话，则:

1： 假如判定条件是常量，则： 
只能 rownum = 1, <= 大于1 的自然数， = 大于1 的数是没有结果的；大于一个数也是没有结果的 
即 当出现一个 rownum 不满足条件的时候则 查询结束 this is stop key（一个不满足，系统将该记录过滤掉，则下一条记录的rownum还是这个，所以后面的就不再有满足记录，this is stop key）；

2： 假如判定值不是常量，则：

若条件是 = var , 则只有当 var 为1 的时候才满足条件，这个时候不存在 stop key ,必须进行full scan ,对每个满足其他where条件的数据进行判定，选出一行后才能去选rownum=2的行……
