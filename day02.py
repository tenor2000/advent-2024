with open('data/day02data.txt') as f:
  data = f.read().splitlines()

reportData = []

for line in data:
  reportData.append([int(x) for x in line.split(' ')])

def checkValidity(reportX):
    diffs = [reportX[i+1] - reportX[i] for i in range(len(reportX)-1)]
    if(all(x < 0 and x in range(-3, 0) for x in diffs)) or (all(x > 0 and x in range(1, 4) for x in diffs)):
      return True
    else:
      return False

def countSafeReports(reports):
  safetyCount = 0

  for report in reports:
    if checkValidity(report):
      safetyCount += 1

  return safetyCount

def countTolerantSafeReports(reports):
  safetyCount = 0

  for report in reports:
    if checkValidity(report):
      safetyCount += 1
    else:
      for i in range(len(report)):
        tempReport = report.copy()
        tempReport.pop(i)
        if checkValidity(tempReport):
          safetyCount += 1
          break

  return safetyCount

#Answers
print("Part One:", countSafeReports(reportData))
print("Part Two:", countTolerantSafeReports(reportData))