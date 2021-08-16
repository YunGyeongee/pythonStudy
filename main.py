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


# 7. Returns : 함수의 return은 오직 하나만 사용할 수 있음
def p_plus(a, b):
  print(a + b)

def r_plus(a, b) :
  return a + b

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)



# 8. Keyworded Arguments
def plus(a, b):
  return a + b

result = plus(b=30, a=1) #인자의 순서는 중요하지 않음. 단 인자명을 제대로 적어줘야함
print(result)

def say_hello(name, age):
  return f"Hello {name} you are {age} years old" #문자열이면 f를 붙여주고 변수로 지정하고 싶은 것엔 {} 괄호로 묶어줌

hello = say_hello("Rechal", "25")
print(hello)


# 9. if else
def pluss(a, b) :
  if type(b) is int or type(b) is float :
    return a + b
  else :
    return None

print(pluss(12, 1.2))


# 10. if else and or
def age_check(age) :
  print(f"you are {age}")
  if age < 18 :
    print("you cant drink")
  elif age == 18 or age == 19 :
    print("you are new to this!")
  elif age > 20 and age < 25 : # 둘 중 하나가 참이 아닐 경우엔 실행안됨 == 둘 다 참이여야 실행
    print("you are still kind of young")
  else :
    print("enjoy your drink")

age_check(19)


# 11. loop
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for i in days :
  if i is "Wed" :
    break
  else :
    print(i)
  