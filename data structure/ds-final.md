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
