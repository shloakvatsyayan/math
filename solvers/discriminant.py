while True:
  a=int(input("a = "))
  b=int(input("b = "))
  c=int(input("c = "))
  """tx1=0
  tx2=0
  rangei=int((c/2)+1)
  if a == 1:
    for i in range(rangei):
      if i == 0:
        continue
      elif i + c/i == b:
        tx1 = i
        tx2=c/i
  print(f"(x+{tx1})(x+{tx2})")"""

  bsqrd=b**2
  fourac=4*a*c
  discriminant = bsqrd - fourac
  print(discriminant)
  if discriminant < 0:
    print("No real roots")
  elif discriminant == 0:
    print("One real root")
  elif discriminant > 0:
    print("2 real roots")
