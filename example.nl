3;
43 + 0.11;
"foo";


if(equals(1, 1),
{
    print("Hello!");
},
{
    print("World!");
});


print("Example!");


func = {
print("Hello ");
print("World!");
};

func();


sum = 
{:(num)
    if(equals(0, num),
    {
        0;
    },
    {
        num + sum(num - 1);
    });
};

print(sum(10));