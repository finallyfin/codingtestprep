tempGroup = 0;
totalGroup = 0;

group = input().split();
group.sort();

for i in range(len(group)):
  personFearLvl = int(group[i])
  if personFearLvl > tempGroup:
    tempGroup += 1
  elif personFearLvl == tempGroup:
    totalGroup += 1
    tempGroup = 1

print(totalGroup)





