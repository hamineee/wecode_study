# 파이썬에서 가변객체와 불변객체는 무엇이며, 어떠한 자료형이 있는지 공부한다.
# 파이썬 가변 객체: list, set, dict
# 파이썬 불변 객체: int, bool, float, tuple, string, unicode

# 1. BTS혹은 레드벨벳의 멤버정보를 딕셔너리로 구현해주세요. 
BTS = {'member1':'V', 'member2':'Suga','member3':'Jungkook','member4':'Jin','member5':'Jimin','member6':'RM','member7':'J-Hope'}

# 2. 스트링, 리스트, 딕셔너리를 반복문으로 돌면서 인자를 출력하는 함수를 작성해보세요.
# 1) 스트링
string = "hello world"
[print(i) for i in string]

# 2) 리스트
lst = [1,2,3,4,5]
[print (i) for i in lst]

#3) 딕셔너리
# key값만 출력
[print(i) for i in BTS]

# value값만 출력
value = BTS.values()
[print(i) for i in value]

# key와 value 모두 출력
key_value = BTS.items()
[print(i) for i in key_value]

# 3. for in 반복문을 작성해보고, break, continue의 쓰임새도 알아보세요.
for i in range(10):
    if i%2 == 0:
        continue
    print(i)

for i in range(10):
    if i == 7:
        break
    print(i)

# 4. if와 else를 이용해 조건문을 작성해보세요
for i in range(10):
    if i%2 == 0 and i != 0:
        print(i,"   even")
    elif i == 0:
        print(i,"   zero")
    else:
        print(i,"   odd")

# 5. list method 중 append, pop, sort 을 활용한 함수를 작성해보세요
# append
even = []
for i in range(10):
    if i%2 == 0:
        even.append(i)
print("Even:",even)

# pop
even.pop(3)
print("Even:",even)

#sort
lst = [9,4,0,3,0,4]
lst.sort()
print(lst)

