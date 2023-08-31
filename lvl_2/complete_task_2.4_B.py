# Задача 2.4.

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    i = s[len(s) - 1]
    s_1 = s[:-1]
    if i == "!":
        return s_1
    else:
        return s

print(remove_last_em("Hi!"))
print(remove_last_em("Hi!!!"))
print(remove_last_em("!Hi"))
  