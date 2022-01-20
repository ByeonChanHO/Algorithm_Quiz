#Sw Expert Academy 5550. 나는 개구리로소이다


T = int(input())

for test_case in range(1, T + 1):
  case = input()
  index = {'c': 0, 'r': 1,'o': 2,'a': 3, 'k': 4}
  list_croak = [[],[],[],[],[]]
  num_shout = [0,0,0,0,0]
  perfect_coak = 0
  least_frog = 0

  for c in case :

    #croak 가 순서대로 list에 들어간다.
    if c == 'c' or len(list_croak[index[c]-1]) > len(list_croak[index[c]]) :
      list_croak[index[c]].append(c)

    #각 문자 카운트
    num_shout[index[c]] += 1

    #최소 개구리 값
    if least_frog < len(list_croak[0]) : 
      least_frog = len(list_croak[0])

    #croak 가 완성될 경우 list 에 완성된 croak 삭제
    if len(list_croak[4]) == 1 :
      for i in range(5) : del list_croak[i][0]
      perfect_coak += 1

  #각 문자 카운트한 수 체크 및 list에 문자열이 체크
  if len(list_croak[0]) == 0 and max(num_shout) == perfect_coak:
    print(f'#{test_case} {least_frog}')
    continue

  print(f'#{test_case} -1')
  
