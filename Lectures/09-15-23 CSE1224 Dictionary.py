from statistics import mean

d = {
    "Mike": [98, 74, 78],
    "Megan": [35, 45, 91],
    "John": [12, 14, 99],
    "David": [49, 92, 72]
}

def highestGrade(di):
  result = {}
  for name, grades, in di.items():
    result[name] = max(grades)
  return result

def highestGrade2(di):
  result = {}
  for name, grades, in di.items():
    maxGrade = 0
    for x in grades:
      if x > maxGrade:
        maxGrade = x
      result[name] = maxGrade
  return result

def weightedGrade(di):
  result = {}
  for name, grades, in di.items():
    result[name] = (0.30 * grades[0]) + (0.30 * grades[1]) + (0.40 * grades[2])
  return result

# final grade=(0.30×test1 score)+(0.30×test2 score)+(0.40×test3 score)

def averageGrade(di):
  result = {}
  for name, grades, in di.items():
    result[name] = mean(grades)
  return result
