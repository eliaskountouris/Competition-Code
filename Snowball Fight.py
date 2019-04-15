h1,w1 = input().split()
h2,w2 = input().split()

if (int(h1) - 1)*int(w2) > (int(h2) - 1)*int(w1):
  print(1)
else:
  if (int(h1) - 1)*int(w2) < (int(h2) - 1)*int(w1):
    print(2)
  else: 
      print(-1)
