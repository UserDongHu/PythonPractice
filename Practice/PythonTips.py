a = 7
b = 5
print(*divmod(a, b)) #a//b, a%b

num = '3212'
base = 5
answer = int(num, base) #base진법으로 적힌 문자열 10진법으로 바꾸기

s = '가나다라'
n = 7
s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬

import string 
string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789

list1 = [3, 2, 5, 1]
list2 = sorted(list1) #원본을 유지한채 정렬된 리스트 구하기.

for entry in enumerate(['A', 'B', 'C']): #enumerate
    print(entry)

def myMapFunc(n):
    return n*10
my_list = [2,3,4,5,6,7,8,9]
updated_list = list(map(myMapFunc, my_list)) #map

list1 = ['1', '100', '33']
list2 = list(map(int, list1))


def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]): #zip
        answer.append(abs(number1 - number2))
    return answer

my_list = ['1', '100', '33']
answer = ''.join(my_list) #join 멤버이어붙이기

import itertools
pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 순열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 순열 만들기

import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list) #배열안에 원소가 몇번 등장하는지 카운트
print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0

mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0] #리스트 한줄안에 if랑 for문 처리

a = 3
b = 'abc'
a, b = b, a # 두 변수 값 바꾸기

# with open('myfile.txt') as file: #파일 쉽게 읽어오기
#     for line in file.readlines():
#         print(line.strip().split('\t'))