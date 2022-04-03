numbers=[60,61,65,63,98,99,90,95,91,96]

mean = sum(numbers)/len(numbers)
squares_sum = sum([(x-mean)**2 for x in numbers])
print((squares_sum / len(numbers))**0.5)
