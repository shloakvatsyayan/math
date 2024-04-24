exit=False
def main():
  print("-------------------------------------------")
  a = input("a = ")
  b = input("b = ")
  c = input("c = ")
  try:
    a=int(a)
  except ValueError:
    a=float(a)
  try:
    b=int(b)
  except ValueError:
    b=float(b)
  try:
    c=int(c)
  except ValueError:
    c=float(c)
  d = (b**2) - (4 * a * c)
  x1 = ((-b) + (d**0.5)) / (2 * a)
  x2 = ((-b) -(d**0.5)) / (2 * a)
  print(f"\nDiscrimiant = {d}\nx1 (using +) = {x1}\nx2 (using -) = {x2}")
  print(
    f"\nUnsimplified Quadratic Equation Using Formula: \n-{b} +- √({b}^2 - 4*{a}*{c})\n---------------------------------\n               2*{a}")
  print(
      f"\nSimplified Quadratic Equation Using Formula: \n{-b} +- √({d})\n---------------\n    {2*a}")
  if int(d*1/2) == d*1/2:
    print(f"\nMostly Solved Quadratic Equation Using Formla: \n{-b} +- {d**0.5}\n---------------\n    {2*a}")
while exit == False:
  try:
    main()
  except EOFError:
    exit = True
  except ValueError:
    print("Invalid Input")