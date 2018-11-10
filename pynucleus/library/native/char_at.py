def char_at(env, num, s):
    if s[0] != "string":
        raise Exception("char_at() must take a string as its second arguement.")
    if num[0] != "number":
        raise Exception("char_at() must take a number as its first arguement.")
    n = int(num(1))
    if n < 0 or n >= len(s[1]):
        return ("none",)
    else:
        return ("string", s[1][n])
