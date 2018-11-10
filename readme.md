## 准备工作

在程序的根目录下分别执行下面的命令即可运行程序

```
$ chmod +x nucleus

$ ./nucleus example.nl

$ ./nucleus example.nl -o example.js
```

## 语言的语法

### 基础数据类型

```
>>> 3;
3
>>> 43 + 0.11;
43.11
>>> "foo"
... ;
'foo'
>>> 
```

### 判断与循环

```
>>> if(equals(1, 1),
... {
...     print("Hello!");
... },
... {
...     print("World!");
... });
Hello!
None
>>> for(chars_in("Hello"),
... {:(ch)
...     print(ch);
...     print(ch);
... });
H
H
e
e
l
l
l
l
o
o
None
>>> 
```

### 函数调用

```
>>> print("Example!");
Example!
None
>>> print("Example!")
... ;
Example!
None
>>> 
```

### 匿名函数

```
>>> {
... print("Hello ");
... print("World!");
... };
<function>
>>> 
```

匿名函数可以直接调用

```
>>> {
... print("Hello ");
... print("World!");
... }();
Hello 
World!
None
>>> 
```

### 命名函数

```
>>> func = {
... print("Hello ");
... print("World!");
... };
<function>
>>> func();
Hello 
World!
None
>>> 
```

### 为函数定义返回值

```
>>> add = {
... a = 1;
... b = 2;
... a + b;
... };
<function>
>>> add();
3
>>> 
```

### 为函数定义参数

```
>>> mul = {:(x, y)
... ret = x * y;
... ret;
... };
<function>
>>> mul(100, 100);
10000
>>> 
```

### 递归

```
>>> sum = {:(num)
...     if(equals(0, num),
...     {
...         0;
...     },
...     {
...         num + sum(num - 1);
...     });
... };
<function>
>>> sum(10);
55
>>> 
```

### 函数本身还可以作为函数的参数

```
>>> f1 = {
... print("I am f1");
... };
<function>
>>> f2 = {
... print("I am f2");
... };
<function>
>>> both_call = {:(x, y)
... x();
... y();
... };
>>> both_call(f1, f2);
I am f1
I am f2
None
>>> both_call(f2, f1);
I am f2
I am f1
None
>>> 
```

### 类和对象

利用函数、闭包……的特性来构造对象的语法

```
>>> person = {
...     {
...         age = 0;
...         {:(method_name)
...             if(equals("add", method_name),
...             {{:(num)
...                 set("age", age + num);
...             }},
...             {
...                 if(equals("sub", method_name),
...                 {{:(num)
...                     set("age", age - num);
...                 }},
...                 {
...                     if(equals("wrong", method_name),
...                         {bal;},
...                         {print("Unknown method!");}
...                     );
...                 });
...             })
...         };
...     }();
... };
<function>
>>> p1 = person();
<function>
>>> p2 = person();
<function>
>>> p1("add")(1);
1
>>> p2("add")(10);
10
```

