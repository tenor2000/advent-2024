import re

with open('data/day03data.txt') as f:
  data = f.read().splitlines()
  data2 = ' '.join(data)

def findMul(string):
  mulArray = re.findall('mul\(\d+,\d+\)', string)
  numbers = [re.findall('\d+,\d+', phrase) for phrase in mulArray]
  numSum = 0

  for numArr in numbers:
    first = int(numArr[0].split(',')[0])
    second = int(numArr[0].split(',')[1])

    numSum += first * second
  
  return numSum

def sumOfMul(dataList):
  total = 0
  for line in dataList:
    total += int(findMul(line))

  return total

def findDosAndDonts(string):
  newString = "do()" + string

  dosArray = []
  commands = newString.split('do()')
  for command in commands:
    newCommand = command.split("don't()")[0]
    dosArray.append(newCommand)

  return dosArray

def sumOfEnabledMul(dataList):
  dosArray = findDosAndDonts(dataList)
  total = 0

  for line in dosArray:
    total += int(findMul(line))

  return total


#Answers
print("Part One:", sumOfMul(data))
print("Part Two:", sumOfEnabledMul(data2))