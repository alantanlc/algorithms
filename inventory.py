m = 5
requested = 218 
data = [50, 100, 50, 20]

inventory = sum(data)
balance = requested
given = 0

record = {}
for index, cls in enumerate(data):
  cls = int(cls)
  record[(cls, index)] = [cls, 0, cls] 

output = {}
for key, value in reversed(sorted(record.items())):
  cls = key[0]
  index = key[1]
  if cls <= balance:
    if inventory - cls > 1:
      output[index] = [cls, cls, 0]
      inventory -= cls
      balance -= cls
      given += cls
    else:
      output[index] = [cls, inventory - 1, cls - (inventory - 1)] 
      given += (inventory - 1)
      inventory = 1
      balance -= (inventory - 1)
  elif balance > 0:
    if inventory - balance > 1:
      output[index] = [cls, balance, cls - balance] 
      given += balance
      inventory -= balance
      balance = 0
    else:
      output[index] = [cls, inventory - 1, cls - (inventory - 1)]
      given += (inventory - 1)
      inventory = 1
      balance -= (inventory - 1) 

if given < requested:
  print('Sorry', given)
else:
  print('Thanks', given)

for key, value in sorted(output.items()):
  print(value)
