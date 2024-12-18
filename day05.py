import math

with open('data/day05data.txt') as f:
  data = f.read().splitlines()

switch = False
rules = []
updates = []

for line in data:
  if line == '':
    switch = True
  elif switch == False:
    rules.append(line)
  else:
    updates.append(line)

class Puzzle():
  def __init__(self, rulesInput, updateInput):
    self.rules = [[int(item) for item in x.split('|')] for x in rulesInput]
    self.updates = [[int(item) for item in x.split(',')] for x in updateInput]
    self.totalSum = 0
    self.updatedList = []
    self.updatedTotalSum = 0

  def matchToRules(self, lineUpdate):
    for i in range(len(self.rules)):

      first, second = self.rules[i][0], self.rules[i][1]

      if first in lineUpdate and second in lineUpdate:
        if lineUpdate.index(first) >= lineUpdate.index(second):
          return False

    return True

  def matchAndCorrect(self, lineUpdate):
    newLine = lineUpdate.copy()
    corrected = False
    failures = 0
    index = 0

    while index <= len(self.rules):
      if index == len(self.rules) and failures == 0:
        break
      elif index == len(self.rules) and failures > 0:
        index = 0
        failures = 0
        continue

      firstNum, secondNum = self.rules[index][0], self.rules[index][1]

      if firstNum in newLine and secondNum in newLine:
        # print("Rule: ", self.rules[index])
        if newLine.index(firstNum) >= newLine.index(secondNum):
          num = newLine.pop(newLine.index(firstNum))
          newLine.insert(newLine.index(secondNum), num)
          # print("Inserted: ", newLine)
          failures += 1
          corrected = True
      
      index += 1
    

    if corrected == True:      
      self.updatedList.append(newLine)


  def solvePuzzle1(self):
    for line in self.updates:
      print(line)
      if self.matchToRules(line):
        middleIndex = math.floor(len(line)/2)
        self.totalSum += line[middleIndex]

    return self.totalSum
        
  def solvePuzzle2(self):
    for line in self.updates:
      self.matchAndCorrect(line)

    for line in self.updatedList:
      middleIndex = math.floor(len(line)/2)
      self.updatedTotalSum += line[middleIndex]

    return self.updatedTotalSum

  
  

if __name__ == "__main__":
  Day5 = Puzzle(rules, updates)
  print("Part One: ", Day5.solvePuzzle1())
  print("Part Two: ", Day5.solvePuzzle2())