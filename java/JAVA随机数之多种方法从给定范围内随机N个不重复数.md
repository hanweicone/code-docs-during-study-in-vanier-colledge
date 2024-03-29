# JAVA随机数之多种方法从给定范围内随机N个不重复数
# #一、JAVA中生成随机数的方式

1、在j2se中使用Math.random()令系统随机选取一个0-1之间的double类型小数，将其乘以一个数，比如25，就能得到一个0-25范围内的随机数，这个在j2me中没有；    
Java代码 

        int randomNumber = (int) Math.round(Math.random()*(max-min)+min);  
 

2、在System类中有一个currentTimeMillis()方法，这个方法返回从1970年1月1号0点0分0秒到目前的一个long型的毫秒 数，可作为一个随机数，还可以将其对某些数取模，就能限制随机数的范围；此方式在循环中同时产生多个随机数时，会是相同的值，有一定的局限性！  

Java代码

        long randomNum = System.currentTimeMillis();  
        int randomNumber = (int) randomNum%(max-min)+min;  
 

3、使用java.util.Random类来产生一个随机数发生器，这个也是我们在j2me的程序里经常用的一个取随机数的方法。它有两种形式的构造函 数，分别是Random()和Random(long seed)。Random()使用当前时间即System.currentTimeMillis()作为发生器的种子，Random(long seed)使用指定的seed作为发生器的种子。随机数发生器(Random)对象产生以后，通过调用不同的method：nextInt()、 nextLong()、nextFloat()、nextDouble()等获得不同类型随机数。 如果两个Random对象使用相同的种子（比如都是25），并且以相同的顺序调用相同的函数，那它们返回值完全相同。    

Java代码  

        Random random = new Random();  
        int randomNumber =  random.nextInt(max)%(max-min+1) + min;  
 

 

## 二、随机给定范围内N个不重复的数

 

1、方法一：最简单最易理解的两重循环去重  


Java代码 

```java
/** 
 * 随机指定范围内N个不重复的数 
 * 最简单最基本的方法 
 * @param min 指定范围最小值 
 * @param max 指定范围最大值 
 * @param n 随机数个数 
 */  
public static int[] randomCommon(int min, int max, int n){  
    if (n > (max - min + 1) || max < min) {  
           return null;  
       }  
    int[] result = new int[n];  
    int count = 0;  
    while(count < n) {  
        int num = (int) (Math.random() * (max - min)) + min;  
        boolean flag = true;  
        for (int j = 0; j < n; j++) {  
            if(num == result[j]){  
                flag = false;  
                break;  
            }  
        }  
        if(flag){  
            result[count] = num;  
            count++;  
        }  
    }  
    return result;  
}  
```

2、方法二：利用HashSet的特征，只能存放不同的值  

Java代码 

        /** 
         * 随机指定范围内N个不重复的数 
         * 利用HashSet的特征，只能存放不同的值 
         * @param min 指定范围最小值 
         * @param max 指定范围最大值 
         * @param n 随机数个数 
         * @param HashSet<Integer> set 随机数结果集 
         */  
           public static void randomSet(int min, int max, int n, HashSet<Integer> set) {  
               if (n > (max - min + 1) || max < min) {  
                   return;  
               }  
               for (int i = 0; i < n; i++) {  
                   // 调用Math.random()方法  
                   int num = (int) (Math.random() * (max - min)) + min;  
                   set.add(num);// 将不同的数存入HashSet中  
               }  
               int setSize = set.size();  
               // 如果存入的数小于指定生成的个数，则调用递归再生成剩余个数的随机数，如此循环，直到达到指定大小  
               if (setSize < n) {  
                randomSet(min, max, n - setSize, set);// 递归  
               }  
           }  


 3、方法三：排除已随机到的数  

Java代码  

            /** 
             * 随机指定范围内N个不重复的数 
             * 在初始化的无重复待选数组中随机产生一个数放入结果中， 
             * 将待选数组被随机到的数，用待选数组(len-1)下标对应的数替换 
             * 然后从len-2里随机产生下一个随机数，如此类推 
             * @param max  指定范围最大值 
             * @param min  指定范围最小值 
             * @param n  随机数个数 
             * @return int[] 随机数结果集 
             */  
            public static int[] randomArray(int min,int max,int n){  
                int len = max-min+1;  

            if(max < min || n > len){  
                return null;  
            }  

            //初始化给定范围的待选数组  
            int[] source = new int[len];  
               for (int i = min; i < min+len; i++){  
                source[i-min] = i;  
               }  

               int[] result = new int[n];  
               Random rd = new Random();  
               int index = 0;  
               for (int i = 0; i < result.length; i++) {  
                //待选数组0到(len-2)随机一个下标  
                   index = Math.abs(rd.nextInt() % len--);  
                   //将随机到的数放入结果集  
                   result[i] = source[index];  
                   //将待选数组中被随机到的数，用待选数组(len-1)下标对应的数替换  
                   source[index] = source[len];  
               }  
               return result;  
        }  


    调用实例：

Java代码  

        public static void main(String[] args) {  
        int[] reult1 = randomCommon(20,50,10);  
        for (int i : reult1) {  
            System.out.println(i);  
        }  

        int[] reult2 = randomArray(20,50,10);  
        for (int i : reult2) {  
            System.out.println(i);  
        }  

        HashSet<Integer> set = new HashSet<Integer>();  
        randomSet(20,50,10,set);  
           for (int j : set) {  
            System.out.println(j);  
        }  
        }  
