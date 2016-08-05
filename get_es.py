import sys

# Return the "equivalent skill" of a equipment
def get_es(arr):
  result = arr[0] * 0.55 + arr[1] * 0.8 + arr[2] * 0.85 + arr[3] + arr[4] * 1.1 + arr[5] * 1.5
  if (arr[6] == 3):
    result += 4
  elif (arr[6] == 2):
    result += 2.5
  elif (arr[6] == 1):
    result += 1
  return result

arr = [int(i) for i in sys.argv[1:]]
print get_es(arr)
