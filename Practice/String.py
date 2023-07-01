a = "String test"
a = a.split()
print(a)
a = a[1]
print(a)
b = [1,2,3,4,5,6,7]
print(b[1:5]) #인덱스 1이상 5미만
dic = {'name' : 'Eric', 'age' : '16'} #딕셔너리
dic['address'] = '모니터' #딕셔너리 추가
del dic['address'] #딕셔너리 삭제
print(dic['name']) #키값으로 밸류 얻기
print(dic.keys()) #print(dic.values())
for k, v in dic.items():
    print("키 : " + k)
    print("밸류 : " + v)
print(dic.get('address','없음'))
print(1 in dic)
s1 = set([1,2,3]) #집합 s1 = {1,2,3}
s1.add(4)
s1.update([5,6,7,8])
s1.remove(7)
print(s1, type(s1))
l = [1,2,2,3,3]
newlist = list(set(l))
print(newlist,type(newlist))
s2 = set([3,4,5])
print(s1 & s2) #(s1.intersection(s2)) 교집합
print(s1 | s2) #(s1.union(s2)) 합집합
print(s1 - s2) #(s2.difference(s1)) 차집합
#pythontutor.com/live.html << 객체에 값 들어가는거 눈으로 확인가능