number = int(input("Enter any number:\n"))
even = sum([num for num in range(number) if num % 2 == 0])
odd = sum([num for num in range(number) if num % 2 == 1])

print(f"sum of even is {even}")
print(f"sum of odd is {odd}")

numbers = list(range(number))
print(f"Sum of even numbers: {sum(filter(lambda x: x % 2 == 0, numbers))}")
print(f"Sum of odd numbers: {sum(filter(lambda x: x % 2 == 1, numbers))}")