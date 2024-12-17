with open('data/day04data.txt') as f:
  data = f.read().splitlines()

class FindWord():
  def __init__(self, dataInput, word):
    self.dataInput = dataInput
    self.word = word
    self.total = 0

  def recursiveCheck(self, x, y, dx, dy, wordIndex=0):
    if x+dx < 0 or y+dy < 0 or y+dy >= len(self.dataInput) or x+dx >= len(self.dataInput[0]):
      return False

    if self.dataInput[y+dy][x+dx] == self.word[wordIndex]:
      if wordIndex == len(self.word)-1:
        self.total += 1
        return
      else:
        self.recursiveCheck(x+dx, y+dy, dx, dy, wordIndex+1)
    else:
      return False

  def checkDiagonals(self, x, y):
    directionals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    count = 0

    for dirX, dirY in directionals:
      if x+dirX < 0 or y+dirY < 0 or y+dirY >= len(self.dataInput) or x+dirX >= len(self.dataInput[0]):
        continue
      elif x-dirX < 0 or y-dirY < 0 or y-dirY >= len(self.dataInput) or x-dirX >= len(self.dataInput[0]):
        continue

      if self.dataInput[y+dirY][x+dirX] == 'M':
        if self.dataInput[y-dirY][x-dirX] == 'S':
          count += 1

    if count == 2:
      return True
    return False

  
  def findResultPart1(self):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for y in range(len(self.dataInput)):
      for x in range(len(self.dataInput[0])):
        if self.dataInput[y][x] == self.word[0]:
          for dirX, dirY in directions:
            self.recursiveCheck(x, y, dirX, dirY, 1)
        else:
          continue
    return self.total

  def findResultPart2(self):
    for y in range(len(self.dataInput)):
      for x in range(len(self.dataInput[0])):
        if self.dataInput[y][x] == 'A':
          if self.checkDiagonals(x, y):
            self.total += 1
    return self.total


if __name__ == "__main__":
  Puzzle1 = FindWord(data, 'XMAS')
  Puzzle2 = FindWord(data, 'XMAS')
  print('Part One: ', Puzzle1.findResultPart1())
  print('Part Two: ', Puzzle2.findResultPart2())