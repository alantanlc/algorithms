from sys import stdin

data = [line.strip().split() for line in stdin.readlines()]
num_tests = int(data[0][0])
index = 2
for test in range(num_tests):
  num_items = int(data[index][0])
  items = {}
  for i in range(index+1, index+1+num_items):
    food = data[i][0]
    price = int(data[i][1])
    if food not in items.keys():
      items[food] = [price]
    else:
      items[food].append(price)

  print('Case #%d:' % (test+1))

  # Find min, max and average
  for food, prices in sorted(items.items()):
    minimum = min(prices)
    maximum = max(prices)
    average = sum(prices) // len(prices)
    print(food, minimum, maximum, average) 

  if test < num_tests - 1: 
    print()

  # Update index
  index = index + num_items + 2
