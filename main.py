tempGroup = 0;
totalGroup = 0;

group = input().split();
group.sort();


for i in range(len(group)):
  personFearLvl = int(group[i])
  if personFearLvl > tempGroup:
    tempGroup += 1
    if personFearLvl == tempGroup:
      totalGroup += 1
      tempGroup = 0
      


print(totalGroup)




#아래는 모범답안
#import sys

#n = int(input())
#phobia = list(map(int, input().split()))
#phobia.sort()

#group = 0  # 그룹에 포함되는 모험가 수 세기
#count = 0  # 형성되는 그룹 수 세기

#for p in phobia:
#    group += 1
#    if group >= p:
#        count += 1
#        group = 0

#print(count)

# dkvmwlak




