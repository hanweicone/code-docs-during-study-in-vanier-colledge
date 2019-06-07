# Java 8 Lamba 表达式之方法引用 :: （双冒号）操作符

## 首先来看一段代码

```java
class MethodReferenceTest{
    /**
     * 如果提供了比较器，则使用比较器对 listOfModel 进行排序
     * @param listOfModel 需要被排序的 list
     * @param comparator 比较器，可为空
     * @return listOfModel 排序后的 list
     * */
    List<Model> sortList(List<Model> listOfModel, Comparator<Model> comparator){
        Optional<Comparator<Model>> sorter = Optional.ofNullable(comparator);
        sorter.ifPresent(x -> listOfModel.sort(x));
        // ifPresent needs a Consumer
        //sorter.ifPresent(listOfModel::sort);
        return listOfModel;
    }

    static int modelComparator(Model o1, Model o2){
        //可能有非常复杂的映射关系
        return o1.getSomeIntValue() - o2.getSomeIntValue();
    }

    public static void main(String[] args){
        List<Model> listOfModel = new ArrayList<>();
        //add some instance of Model to listOfModel
        //1. 方法引用
        List<Model> sortedModels = new MethodReferenceTest().
            sortList(listOfModel, MethodReferenceTest::modelComparator);
        //2. lambda 表达式
        //List<Model> sortedModels = new MethodReferenceTest().
        //  sortList(listOfModel, (o1, o2) -> modelComparator(o1, o2));
        //3. 匿名内部类
        /*
        List<Model> sortedModels = new MethodReferenceTest().
            sortList(listOfModel, new Comparator<Model>(){
                @Override
                public int compare(Model o1, Model o2){
                    return o1.getSomeIntValue() - o2.getSomeIntValue();
                }
            });
        */
        // forEach needs a Consumer
        sortedModels.forEach(System.out::println);
    }
}
```

我们用 lambda 表达式取代匿名内部类实现函数式接口，返回一个比较器，而方法引用则是对 lambda 一种更简化的写法，只要被引用的方法的入参和返回值和对应 lambda 表达式写法的入参和返回值一致即可。 
在注释 3. 匿名内部类处，我们可以清楚地看到它产生了一个实现了 Comparator 接口的比较器传入了 sortList 方法；对于 1. 方法引用 和 2. lambda 表达式 则由编译器负责将相应的代码转化为实现了 Comparator 接口的比较器传入 sortList 方法。

:: 方法引用有以下几种用法  
1. 引用类的静态方法，例如上面代码段中 List<Model> sortedModels = new MethodReferenceTest().   
sortList(listOfModel, MethodReferenceTest::modelComparator); 所示   
2. 引用实例方法，例如上面代码段中sorter.ifPresent(listOfModel::sort); 所示   
3. 引用类的构造方法，例如 

```java
class Data<T>{ 
T data; 
} 
// Supplier 是一个函数式接口，它不接收参数，返回一个值 
Supplier<Data<String>> dataRef = Data<String>::new; 
Data<String> Data = dataRef.get(); 
```
4. 引用构造函数创建数组，创建数组 ClassName[]::new
