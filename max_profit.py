import pprint as pp

price = [3,4,5,3,5,2]

k = len(price) - 1

profits = [[0 for d in price] for t in range(k+1)]

for t in range(1, k+1):
  maxThusFar = float("-inf")
  for d in range(1, len(price)):
    maxThusFar = max(maxThusFar, profits[t-1][d-1] - price[d-1])
    print(t, d, maxThusFar)
    profits[t][d] = max(profits[t][d-1], maxThusFar + price[d])

pp.pprint(profits)
