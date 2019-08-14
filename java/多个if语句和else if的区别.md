## 多个if是所有的if都会进行判断

if else if是只要有满足条件的，就不再对之后的else if进行判断

比如
``
a = 2;
if(a==1) c=1;
if(a==2) c=2;
if(a%2==0) c=3;
``
最终结果c=3
a=2;
if(a==1) c=1;
else if(a==2) c=2;
else if(a%2==0) c=3;
最终结果c=2
追问
else if是不是和switch有点差不多
追答
也不是，那要看你怎么用switch case了
比如
switch( a ）{
    case 1：
    case 2：
    case 3：
    case 4：
        break;
}
这样就是 if if了，所有的1,2,3,4满足条件的都会执行一次
switch( a ）{
    case 1：
        break;
    case 2：
        break;
    case 3：
        break;
    case 4：
        break;
}
这样就是else if了，只要满足条件就跳出了
