# Java高级系列——枚举（Enums）
## 一、介绍

本系列文章的这一部分我们将会介绍Java 5版本之后引入的除泛型之外的另外一个强大特性：枚举。可以将枚举看成一种特殊的类，并且可以将注解看成一种特殊的接口。

枚举的思想很简单，也很方便：它代表了一组固定的常量值。实际上，枚举经常用来设计一些状态常量。比如，星期几就是枚举的一个最好例子，因为他们被限制在周一、周二、周三、周四、周五、 周六和周日。

## 二、枚举作为特殊的类

在枚举被引入Java语言之前，在Java中模拟一组固定值的常规方法是通过声明一组常量。例如：

```java
public class DaysOfTheWeekConstants {
    public static final int MONDAY = 0;
    public static final int TUESDAY = 1;
    public static final int WEDNESDAY = 2;
    public static final int THURSDAY = 3;
    public static final int FRIDAY = 4;
    public static final int SATURDAY = 5;
    public static final int SUNDAY = 6;
}
```
虽然这种方法有效，但远非理想的解决方案。主要是因为常量本身只是int类型的值，而代码中需要这些常量（而不是任意的int值）的每一个地方都应该被一直明确地记录和断言。从语义上来讲，比如下面的这个方法演示所表现出来的就不符合类型安全的概念：

```java
public boolean isWeekend( int day ) {
    return( day == SATURDAY || day == SUNDAY );
}
```
从逻辑角度去看，day参数应该是在DaysOfTheWeekConstants类中声明的值之一。然而，如果没有编写额外的说明文档（给后来的一些人阅读），就不可能猜测到这一点。对于Java编译器来说类似于isWeekend(100)的这种调用看起来完全是正确的并且不会引起任何顾虑。

此时枚举就能解决这些问题。枚举允许用类型化的值替换常量并在任何地方使用这些类型。让我们使用枚举重写上面的方案。

```java
public enum DaysOfTheWeek {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
}
```
这里将关键字class改成了enum并且这些可能的值在枚举定义时被列举出来。有区别的一部分就是被声明在枚举类（在我们的例子中是DaysOfTheWeek ）中的每一个单独的值都是一个实例。因此，每当枚举被使用，Java编译器都能够进行类型检查。比如：

```java
public boolean isWeekend(DaysOfTheWeek day) {
    return(day == SATURDAY || day == SUNDAY);
}
```
请注意枚举中的大写命名法的使用是一个约定，但是如果你不这样做也没有谁能够阻止你，但是最好还是遵守约定，这样更有利于代码的维护。

## 三、枚举与实例字段（Enums and instance fields）

枚举是一个特殊的类，因此它是可拓展的。这意味着他们可以有实例字段、构造器和方法（默认无参构造器不能够被声明并且所有的构造器必须被private修饰）。让我们使用枚举的实例和构造器添加一个isWeekend属性。

```java
public enum DaysOfTheWeekFields {
    MONDAY(false),
    TUESDAY(false),
    WEDNESDAY(false),
    THURSDAY(false),
    FRIDAY(false),
    SATURDAY(true),
    SUNDAY(true);

    private final boolean isWeekend;

    private DaysOfTheWeekFields( final boolean isWeekend ) {
        this.isWeekend = isWeekend;
    }

    public boolean isWeekend() {
        return isWeekend;
    }
}
```
我们看到，枚举值只是简单的调用了构造器而并没有要求使用new关键字。isWeekend()方法可以用来确定是否枚举值代表工作日或者周末。比如：

```java
public boolean isWeekend( DaysOfTheWeek day ) {
    return day.isWeekend();
}
```
Java中枚举的实例字段有很大的用处。在常规的类声明规则中，它们经常用来将一些额外的细节与每个值相关联。

## 四、枚举与接口（Enums and interfaces）

另外一个强大的特性，我们再次确认一下枚举是是一个特殊的类，所以它能够实现接口（然而枚举不能够继承任何类）。比如，让我们引入接口DayOfWeek。

    interface DayOfWeek {
        boolean isWeekend();
    }

然后使用接口实现代替常规实例字段的方式重写前面的枚举例子。

```java
public enum DaysOfTheWeekInterfaces implements DayOfWeek {
    MONDAY() {
        @Override
        public boolean isWeekend() {
            return false;
        }
    },
    TUESDAY() {
        @Override
        public boolean isWeekend() {
            return false;
        }
    },
    WEDNESDAY() {
        @Override
        public boolean isWeekend() {
            return false;
        }
    },
    THURSDAY() {
        @Override
        public boolean isWeekend() {
            return false;
        }
    },
    FRIDAY() {
        @Override
        public boolean isWeekend() {
            return false;
        }
    },
    SATURDAY() {
        @Override
        public boolean isWeekend() {
            return true;
        }
    },
    SUNDAY() {
        @Override
        public boolean isWeekend() {
            return true;
        }
    };
}
```
我们实现接口的这种方式显得代码有些冗长，然而合并实例字段和接口实现可以解决这个问题，比如：

```java
public enum DaysOfTheWeekFieldsInterfaces implements DayOfWeek {
    MONDAY( false ),
    TUESDAY( false ),
    WEDNESDAY( false ),
    THURSDAY( false ),
    FRIDAY( false ),
    SATURDAY( true ),
    SUNDAY( true );

    private final boolean isWeekend;

    private DaysOfTheWeekFieldsInterfaces(final boolean isWeekend){
        this.isWeekend = isWeekend;
    }

    @Override
    public boolean isWeekend() {
        return isWeekend;
    }
}
```
通过支持实例字段和接口，枚举可以以更加面向对象的方式使用，从而带来一定程度的抽象。

## 五、枚举与泛型

在Java中，虽然咋一看并看不出来枚举和泛型的关系，但是他们之间存在一种关系。Java中的每一个单独的枚举自动继承自泛型类Enum<T>，在这里T就是枚举类型本身。Java编译器在编译时代表开发者做了这个转换，拓展一下枚举声明public enum DaysOfTheWeek 如下：

    public class DaysOfTheWeek extends Enum< DaysOfTheWeek > {
        // Other declarations here
    }

这也就说明了为什么枚举可以实现接口但不能继承其他类：因为它隐式的继承自Enum<T>并且我们在使用对象的公共方法时已经讨论过，Java中不支持多继承。

实际上每一个继承自Enum<T>的枚举允许定义泛型类、接口和方法，通过这种方式可以让枚举类型的实例参数化或者类型参数化。比如：

    public<T extends Enum< ? >> void performAction(final T instance) {
        // Perform some action here
    }

在上面的方法声明中，类型T被约定为任意枚举类型的实例并且Java编译器将会对其做验证。

## 六、枚举方法

基础类 Enum<T>为自动继承它的枚举实例提供了一些非常有用的方法。

方法	描述
String name()	返回枚举声明声明的枚举常量的名称
int ordinal()	返回枚举常量的次序（即枚举声明时的位置，初始常量分配的位置是0）
此外，Java编译器为每个枚举类型自动生成两个更有用的静态方法（让我们将这个特殊的枚举类型假设为T）。

方法	描述
T[] values()	返回枚举T所声明的所有常量
T valueOf(String name)	返回指定名称的枚举常量
在代码中使用枚举还有一个好处：可以使用switch/case语法。例如：

```java
public void performAction( DaysOfTheWeek instance ) {
    switch( instance ) {
    case MONDAY:
        // Do something
    break;

    case TUESDAY:
        // Do something
    break;

    // Other enum constants here
    }
}
```
## 七、专用集合：EnumSet和EnumMap

和所有其他类一样，枚举的实例也可以和标准Java集合库一起使用。然而，某些集合类型针对枚举做了优化，并且在大多数情况下推荐使用这些优化过后的集合代替通用的集合。

本节我们简单了解一下两个专用的集合：EnumSet<T>和EnumMap<T, ?>。这两个集合都非常容易使用。

我们首先来看一下EnumSet<T>集合。EnumSet<T>集合是常规的集合优化过后高效存储枚举类型的一个集合，EnumSet<T>不能够使用构造器进行实例化，但是它提供了很多非常有用的工厂方法。

比如，allOf工厂方法创建的EnumSet<T>实例就包含了所有枚举类型所枚举的常量：

    final Set<DaysOfTheWeek> enumSetAll = EnumSet.allOf(DaysOfTheWeek.class);

noneOf工厂方法创建的是一个空的EnumSet<T>实例：

    final Set<DaysOfTheWeek> enumSetNone = EnumSet.noneOf(DaysOfTheWeek.class);

使用of工厂方法，可以指定枚举类型中那些枚举常量应该包含在EnumSet<T>中：

    final Set< DaysOfTheWeek > enumSetSome = EnumSet.of(
        DaysOfTheWeek.SUNDAY,
        DaysOfTheWeek.SATURDAY
    );

EnumMap<T, ?>是最接近于一般的map的，唯一的不同就是EnumMap<T, ?>的key是枚举类型的枚举常量。比如;

    final Map<DaysOfTheWeek, String> enumMap = new EnumMap<>(DaysOfTheWeek.class);
    enumMap.put(DaysOfTheWeek.MONDAY, "Lundi");
    enumMap.put(DaysOfTheWeek.TUESDAY, "Mardi");

注意，和大多数集合实现一样，EnumSet<T>和EnumMap<T, ?>不是线程安全的所以不能在多线程环境下使用。

八、何时使用枚举

自Java 5发布以来，在解决一些固定常量集合的问题上枚举成为唯一首选和推荐的一种方式。不仅是因为它们是强类型，同时它们是可拓展并被当前的很多库和框架所支持。
--------------------- 
作者：RonTech 
来源：CSDN 
原文：https://blog.csdn.net/zyhlwzy/article/details/79045066 
版权声明：本文为博主原创文章，转载请附上博文链接！
