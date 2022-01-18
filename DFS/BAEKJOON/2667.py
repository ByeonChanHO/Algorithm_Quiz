#2667번 단지번호붙이기

def make_structure(F,entire):
  flore = []
  for num in F:
    flore.append(int(num))
  entire.append(flore)

def dls(x,y,N,entire,count):
  if  x >= N or x < 0 or y >=N or y <0 or entire[y][x] == 0:
    return count
  
  entire[y][x] = 0
  count += 1

  count = dls(x+1, y, N, entire, count)
  count = dls(x, y-1, N, entire, count)
  count = dls(x-1, y, N, entire, count)
  count = dls(x, y+1, N, entire, count)
  
  return count

N = int(input())
entire = []

for _ in range(N):
  F = input()
  make_structure(F,entire)

num_house = 0
list_count = []
for y in range(N):
  for x in range(N):
    if entire[y][x] == 1 : 
      count = 0
      count = dls(x,y,N,entire,count)
      num_house += 1
      list_count.append(count)

print(num_house)
list_count.sort()
for num in list_count :
  print(num)
