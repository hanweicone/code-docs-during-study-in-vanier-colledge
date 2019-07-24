## recursive
```java

public class Calculation {//递归计算阶乘
    public  int calcFraction(int n){
        int result;
        if(n==1){
            result=1;
        }else{
        result = n*calcFraction(n-1);
        }
        return result;
    }


    public  int calcFarb(int n){//递归计算斐波那契数列
    int farb=0;
    if(n==0|n==1){
        farb = 1;
    }else{
    farb = calcFarb(n-2)+calcFarb(n-1);
    }
    return farb;
    }


    public  int calcFarbIter(int n){//迭代计算斐波那契数列
    int farb = 1;
    int pre=1;
        for (int i = 2; i <= n; i++) {
          
             int temp = farb;
            farb= farb+pre;
            pre = temp;      
        }
    return farb;
    }


    public int calcPlus(int n){//递归计算1+2+...+n
        int result=0;
    if(n==1){
    result =1;
    }else{
    result =n+calcPlus(n-1);
    }
    return result;
    }


    public int findMinInArray(int [] a,int n){//递归寻找数列里面的最小值
      return n == 1 ? a[0] : a[n-1] < findMinInArray(a , n-1) ? a[n-1] : findMinInArray(a , n-1);
    }


    public int calcSumofArray(int[] a,int n){//递归计算数列的和
    int result=0;
    if(n==1){
    result = a [0];
    }else{
    result=a[n-1]+calcSumofArray(a, n-1);
    }
    return result;
    }


    public boolean isPalindrome(int [] a,int n){//递归判断一个数列是否是回文数列(Palindrome)
        //if(n==1||n==0){//also works! 配合下面注释掉的n-2使用
        if(n==1){
            return true;   
        }else{
            return a[a.length-n]==a[n-1]?isPalindrome(a, n-1):false;
          //return a[a.length-n]==a[n-1]?isPalindrome(a, n-2):false;//not works!!
        }
        }
  }
```
## pseduocode of selection sort
```
input array A
output SELECTION-SORTED A
	n ← length[A]
	for j ← 1 to n - 1
		do smallest ← j
		      for i ← j + 1 to n
			   do if A[i] < A[smallest]
				   then smallest ← i
		      exchange A[j] ↔ A[smallest]
```              
## pseduocode of insertion sort 
```
INSERTION-SORT(A)
	for j ← 2 to n
		do key ← A[ j ]
		  Insert A[ j ] into the sorted sequence A[1 . . j -1]
		     i ← j - 1
		     while i > 0 and A[i] > key
			do A[i + 1] ← A[i]
			      i ← i – 1
		     A[i + 1] ← key

```
## pseduocode of binary search
```
input array A,array length n,search target T
output index of T in A
function binary_search(A, n, T):
    L := 0
    R := n − 1
    while L <= R:
        m := (L + R) / 2
        if A[m] < T:
            L := m + 1
        else if A[m] > T:
            R := m - 1
        else:
            return m
    return unsuccessful
```
## pseduocode of bubble sort
```
Alg.: BUBBLESORT(A)
	for i ← 1 to length[A]
		do for j ← length[A] downto i + 1
		          do if A[j] < A[j -1]
			        then exchange A[j] ↔ A[j-1]
```

or
```
bubblesort(A)
	for i ← 1 to length[A]
		do for j ← 1 to length[A] -i
			do if A[j] > A[j +1]
				then exchange A[j] ↔ A[j+1]
```
## ArrayList LinkedList增删查时间复杂度分析
![](https://img-blog.csdnimg.cn/20190109164948676.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODk5MDg3,size_16,color_FFFFFF,t_70)

* ArrayList是线性表（动态数组），LinkedList是链表
* get(index)  根据下标查询，顺序存储知道首个元素的地址，其他的位置很快就能确定，时间复杂度为O(1)
    链式存储，从首个元素开始查找，直到查找到第 i个位置，时间复杂度为O(n)

* add(E)  直接尾部添加，时间复杂度O(1)

* add(index,E)  顺序存储需要查找到元素然后执行插入或删除，时间复杂度为O(1)+O(n)=O(n);
链式存储同样需要先查找到元素然后在插入或删除，时间复杂度为O(n)+O(1)=O(n)

* remove(E)  顺序存储删除指定元素，后面元素要向前移动，时间复杂度O(n)

* 链式存储，直接 指针操作（找到前驱节点，再删除），时间复杂度O(1)
