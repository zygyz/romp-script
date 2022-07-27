f = open('C-CPP-Details-Oct-2021.md')
# key: tool index, value: {key: type, value: list of test}
result = {}
# key: tool index, value: tool name
tool_map = {}

IGNORE_INDEX = [24, 25, 70, 95, 98, 115, 116, 135, 136, 137,
                138, 142, 143, 144, 145, 146, 147, 148, 149, 150,
                151, 152, 153, 154, 155, 156, 157, 158, 159, 160,
                161, 162, 163, 164, 43, 44, 55, 56, 58, 65]

header = f.readline().split('|')
for i in range(5,len(header), 2):
  tool_map[i] = header[i]
  result[i] = {}
print(header)
print(tool_map)

f.readline() #skip
f.readline() #skip

for line in f:
  data = line.split('|')
  testid = data[1]
  testname = data[2]

  if int(testid) in IGNORE_INDEX:
    continue

  for tool_index in result.keys():
    tool_result = data[tool_index]
    if tool_result in result[tool_index]:
      result[tool_index][tool_result].append(testid)
    else:
      result[tool_index][tool_result] = [testid]

# print result
for tool_index in result:
  print(tool_map[tool_index])
  total = 0
  error = 0
  noshow = 0
  for result_type in result[tool_index]:
    count = len(result[tool_index][result_type])
    print(result_type + ": " + str(count))
    total += count

    if result_type in ["CSF", "CF"]:
      error += count
    if result_type == "":
      noshow += count
  print("Total: ", total)
  print("Error: ", error)
  print("No Result: ", noshow)

  tp = len(result[tool_index]["TP"])
  tn = len(result[tool_index]["TN"])
  fp = 0
  fn = 0
  if "FP" in result[tool_index]:
    fp = len(result[tool_index]["FP"])
  if "FN" in result[tool_index]:
    fn = len(result[tool_index]["FN"])

  recall = tp / (tp + fn)
  spec = tn / (tn + fp)
  precision = tp / (tp + fp)
  accuracy = (tp + tn) / (tp + fp + tn + fn)
  print("Recall: ", recall)
  print("Specificity: ", spec)
  print("Precision: ", precision)
  print("Accuracy: ", accuracy)
  print()

