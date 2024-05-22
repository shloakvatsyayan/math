while True:
  a = input("Enter value for a: ")
  b = input("Enter value for b: ")
  if a == "" or b == "":
    c = input("Enter value for c: ")
  else:
    c = ""

  if c == "":
      answer = (float(a) ** 2 + float(b) ** 2) ** 0.5
      print(answer)
  elif b == "":
      answer = (float(c) ** 2 - float(a) ** 2) ** 0.5
      print(answer)
  elif a == "":
      answer = (float(c) ** 2 - float(b) ** 2) ** 0.5
      print(answer)