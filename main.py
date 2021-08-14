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



# 4. Function
print("lalalalaa")
print(len("asdgaseasdgasdgas"))

age = "18"
print(type(age))
n_age = int(age)
print(n_age)
print(type(n_age))


# 5. Python filter
def say_hello():
  print("hello")
  print("bye")

say_hello()

# 6. Function Arguments
def say_hello(who):
  print("hello", who)

say_hello("Rachel")

def plus(a, b):
  print(a + b)

def minus(a, b=0): #defualt 값을 정의할 수 있음
  print(a - b)

plus(2,5)
minus(2)

def say_hello(name="anonymous"):
  print("hello", name)

say_hello()
say_hello("Rachel")
