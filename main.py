# 1. Variable
a_string = 'like this' # we called String or text
a_number = 3 # number
a_float = 3.12 # float thing ~
a_boolean = True # not text
a_none = None # undifiend, nothing is well

#print(type(a_string))

super_long_variable = True # snake case
superLongVariable = True # JS
# sequence type / sequence is like list


# 2. List
days1 =["Mon", "Tue", "Wed", "Thur", "Fri"]
print("Mon" in days1)
print(days1[2]) # computer is count start from 0

days1.append("Sat")
days1.reverse()
print(days1)



# 3. Tuples
days2 = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(type(days2))

YunGyeong = {
  "name" : "YunGyeong",
  "age" : 25,
  "korean" : True,
  "fav_food" : "gimbab"
}

print(YunGyeong)
YunGyeong["handsome"] = True
print(YunGyeong)