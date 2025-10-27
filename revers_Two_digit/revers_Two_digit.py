num = int(input("Enter a two-digit number: "))
tens = num // 10
ones = num % 10
reversed_num = ones * 10 + tens
print("Reversed number:", reversed_num)