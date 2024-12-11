with open('data/day01data.txt') as f:
  data = f.read().splitlines()

listA = []
listB = []

for line in data:
  a, b = line.split('   ')[0], line.split('   ')[1]
  listA.append(int(a))
  listB.append(int(b))

def findSumOfDifferences(firstList, secondList):
  sum = 0
  firstList.sort()
  secondList.sort()
  for i in range(len(firstList)):
    sum += abs(firstList[i] - secondList[i])

  return sum

def findSimScore(firstList, secondList):
  simScore = 0
  for i in range(len(firstList)):
    multiplier = secondList.count(firstList[i])
    simScore += firstList[i] * multiplier

  return simScore


#Answers
print("Part One:", findSumOfDifferences(listA, listB))
print("Part Two:", findSimScore(listA, listB))
