number = int(input("Enter a number: "))
tens = number // 10
ones = number % 10
power_tens = tens ** ones
power_ones = ones ** tens
print("the tens result power: ", power_tens)
print("the ones result power: ", power_ones)