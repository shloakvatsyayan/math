#uses input function, only works with y = ax^2 + bx + c (standard form).
while True:
  a = input("a = ")
  if a.lower() == "quit":
    break
  b = input("b = ")
  if b.lower() == "quit":
    break
  c = input("c = ")
  if c.lower() == "quit":
    break
  table_len = 2
  #table_len=int(input("Table Length: "))
  print("--------")
  if a == "":
    a = 0
  if b == "":
    b = 0
  if c == "":
    c = 0
  a, b, c = int(a), int(b), int(c)

  def f(a, b, c, x):
    return (a * (x**2)) + (b * x) + c

  AoS = (-b) / (2 * a)
  if AoS == -0.0:
    AoS = 0
  vertexy = f(a, b, c, AoS)
  yint = f(a, b, c, 0)
  table = []
  for i in range(-table_len, table_len + 1):
    table.append((AoS + i, f(a, b, c, AoS + i)))
  orange = ""
  if a > 0:
    orange = f"y >= {vertexy}"
  if a < 0:
    orange = f"y <= {vertexy}"
  di = (b*b)-(4*a*c)
  print(f"AoS: x = {AoS}, Range: {orange}, Vertex: ({AoS}, {vertexy}), Y Intercept: {yint}")
  print("--------")
  print("Table of Values:")
  for i in table:
    print(i)
  print("--------")
