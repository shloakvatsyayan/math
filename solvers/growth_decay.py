#very old and broken code imported from an old laptop, need to be fixed
while True:
  initial_val = input("Please enter the inital value: ")
  initial_val = int(initial_val)
  growth=input("Is it a growth or decay? ")
  growth=str(growth.strip())
  growth=growth.lower()
  if growth == "growth":
    growth=float(-1)
  if growth == "decay":
    growth=float(1)
  rate=input("Please enter the rate (without the percent   sign): ")
  rate=float(rate)
  rate=rate*0.01*growth
  gval=1-rate
  x=0
  while True:
    x=input("input x val: ")
    if x=="exit" or "stop":
      break
    x=int(x)
    answer=initial_val*(gval**x)
    print (answer)