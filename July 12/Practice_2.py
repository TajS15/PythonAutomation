number = int(input("Enter a number to print its multiplication table: \n"))

# Create the table using string formatting and join method
table = "\n".join([f"{number} x {i} = {number * i}" for i in range(1, 11)])

print(table)