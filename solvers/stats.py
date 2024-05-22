import statistics as stats
import numpy
while True:
  numlist = []
  while True:
    num = input("Enter number in list: ")
    if num == "":
      break
    else:
      try:
        num = float(num)
        numlist.append(num)
      except TypeError:
        print("Invalid input, ending list")
        break
      except ValueError:
        print("Invalid input, ending list")
        break
  mean_avr = numpy.mean(numlist)
  madlist = []
  for i in numlist:
    madlist.append(abs(i - mean_avr))
  MAD = 0
  for i in madlist:
    MAD += i
  MAD /= len(numlist)
  q1, q3 = numpy.quantile(numlist, [0.25, 0.75])
  print("------------------")
  print("Maximum:", max(numlist))
  print("Minimum:", min(numlist))
  print("---")
  print("Median: ", numpy.median(numlist))
  print("Lower Quartile: ", q1)
  print("Uppder Quartile: ", q3)
  print("Interquartile Range: ", q3 - q1)
  print("---")
  print("Mean/Average: ", numpy.mean(numlist))
  print("Mode: ", stats.mode(numlist))
  print("Range: ", max(numlist) - min(numlist))
  print("---")
  print("Mean Absolute Deviation: ", MAD)
  print("MAD List: ", madlist)
  print("Standard Deviation: ", numpy.std(numlist))
  print("Variance: ", numpy.std(numlist)*numpy.std(numlist))
  print("------------------")
