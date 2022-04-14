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

print('oh im in trouble')






