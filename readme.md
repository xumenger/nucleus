# 下面展示语言的语法

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

