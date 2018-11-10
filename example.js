var not = (function(value) {
    return (function() {
       if(value != 0){
            return 0;
       } else {
            return 1;
       }
    })();
});
var chars_in = (function(s) {
    var impl = (function(s, i) {
        return (function() {
           if((len(s)===i ? 1 : 0) != 0){
                return null;
           } else {
                return (function(which) {
                    return (function() {
                       if((which==='f' ? 1 : 0) != 0){
                            return char_at(i, s);
                       } else {
                            return impl(s, i + 1);
                       }
                    })();
                });
           }
        })();
    });
    return impl(s, 0);
});
var pair = (function(f, s) {
    return (function(which) {
        return (function() {
           if((which==='f' ? 1 : 0) != 0){
                return f;
           } else {
                return s;
           }
        })();
    });
});
var first = (function(p) {
    return p('f');
});
var second = (function(p) {
    return p('s');
});
var list0 = (function() {
    return null;
});
var list1 = (function(a) {
    return pair(a, null);
});
var list2 = (function(a, b) {
    return pair(a, list1(b));
});
var list3 = (function(a, b, c) {
    return pair(a, list2(b, c));
});
var list4 = (function(a, b, c, d) {
    return pair(a, list3(b, c, d));
});
var list5 = (function(a, b, c, d, e) {
    return pair(a, list4(b, c, d, e));
});
var prepend = pair;
var append = (function(lst, item) {
    return (function() {
       if((lst===null ? 1 : 0) != 0){
            return list1(item);
       } else {
            return pair(first(lst), append(second(lst), item));
       }
    })();
});
var for__ = (function(xs, fn) {
    return (function() {
       if(not((xs===null ? 1 : 0)) != 0){
            fn(first(xs));
            return for__(second(xs), fn);
       } else {
       }
    })();
});
3;
43 + 0.11;
'foo';
(function() {
   if((1===1 ? 1 : 0) != 0){
        return console.log('Hello!');
   } else {
        return console.log('World!');
   }
})();
console.log('Example!');
var func = (function() {
    console.log('Hello ');
    return console.log('World!');
});
func();
var sum = (function(num) {
    return (function() {
       if((0===num ? 1 : 0) != 0){
            return 0;
       } else {
            return num + sum(num - 1);
       }
    })();
});
console.log(sum(10));
