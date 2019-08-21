太多的if-else不太直观，难以维护。 

以下面代码为例，展示几种替代if else的方法。
```java
String input = "three";

    @Test
    public void testElse() {
        if ("one".equals(input)) {
            System.out.println("one");
        } else if ("two".equals(input)) {
            System.out.println("two");
        } else if ("three".equals(input)) {
            System.out.println("three");
        } else if ("four".equals(input)) {
            System.out.println("four");
        }
    }
```
需要引入Spring跟Guava依赖

1.Spring结合策略模式

Spring可以将一组实现了同样接口的类注入一个List
```java
/***
 * 定义接口。type用来路由具体的Handler实现
 * */
public interface Handler {
    String getType();

    void execute();
}
  /**
     * 将Handler接口的实现类注入一个List
     * */
    @Autowired
    private List<Handler> handlerList;
    @Test
    public void testAutowireList(){
    // 根据类型判断该由哪个具体实现类处理
         for(Handler handler:handlerList){
             if(input.equals(handler.getType())){
                 handler.execute();
             }
         }
    }
```
下面是几种轻量级实现.

2. 反射
通过反射动态调用相应的方法
```java
/***
 *定义每种类型所对应的方法
*/
public class ReflectTest {
    public void methodOne() {
        System.out.println("one");
    }

    public void methodTwo() {
        System.out.println("two");
    }

    public void methodThree() {
        System.out.println("three");
    }

    public void methodFour() {
        System.out.println("four");
    }

}

 /***
     *
     * 通过反射，动态调用方法。采用了Guava的工具类。
     * */
    @Test
    public void testReflect() throws Exception {
        //首字母大写，根据类型拼接方法
        String methodName = "method" + LOWER_CAMEL.to(UPPER_CAMEL, input);
        Method method = ReflectTest.class.getDeclaredMethod(methodName);
        Invokable<ReflectTest, Object> invokable =
                (Invokable<ReflectTest, Object>) Invokable.from(method);
        invokable.invoke(new ReflectTest());
    }
```
3. lambda表达式
实现同上面的反射，结合了Java 8的新特性：lambda表达式

```java
    @Test
    public void testJava8() {
        Map<String, Consumer<ReflectTest>> functionMap = Maps.newHashMap();
        functionMap.put("one", ReflectTest::methodOne);
        functionMap.put("two", ReflectTest::methodTwo);
        functionMap.put("three", ReflectTest::methodThree);
        functionMap.put("four", ReflectTest::methodThree);
        functionMap.get(input).accept(new ReflectTest());
    }
```
4. 枚举
在枚举里面定义一个抽象方法，每种类型对应各自的具体实现。
```java
/**
 * 定义枚举类，包含了所有类型
 */
public enum EnumTest {


    ONE("one") {
        @Override
        public void apply() {
            System.out.println("one");
        }
    },
    TWO("two") {
        @Override
        public void apply() {
            System.out.println("two");
        }
    }, THREE("three") {
        @Override
        public void apply() {
            System.out.println("three");
        }
    }, FOUR("four") {
        @Override
        public void apply() {
            System.out.println("four");
        }
    };

    public abstract void apply();

    private String type;

    EnumTest(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

}
  // 枚举测试
 @Test
    public void testEnum() {
        EnumTest.valueOf(input.toUpperCase()).apply();
    }
```
