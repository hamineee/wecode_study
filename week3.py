# 1. 변수를 선언하고 수정하기

#가변객체
mutable_var = ["Tom", "Jerry"]
mutable_var[1] = "Tim"

#불변객체
immutable_var = "Tom"
immutable_var = "Jerry"
immutable_var[0] = "H" # TypeError: 'str' object does not support item assignment

# 2. 프로그래머스 알고리즘 문제
# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서
# 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = []                             
    i = 0                                 
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            print(i,j)
            arg = numbers[i] + numbers[j]   
            if arg not in answer:           
                answer.append(arg)         
    answer.sort()                           
    return answer