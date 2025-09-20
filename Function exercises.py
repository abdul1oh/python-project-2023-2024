# Rectangle perimeter
def perimeter(a, b):
    return (a + b) * 2

result = perimeter(8, 5)
print("Rectangle perimeter:", result)


# Rectangle area
def area(a, b):
    return a * b

result = area(8, 5)
print("Rectangle area:", result)


# Circle area
def circle_area(radius):
    return (radius ** 2) * 3.14

result = circle_area(20)
print("Circle area:", result)


# Circle circumference
def circle_circumference(radius):
    return (radius * 2) * 3.14

result = circle_circumference(20)
print("Circle circumference:", result)


# Fibonacci sequence (iterative version)
def fibonacci(n):
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = 10
print(f"Fibonacci number {n}:", fibonacci(n))


# Find two numbers in a list that sum to a given value
def find_two_numbers(num_list, target):
    for num in num_list:
        complement = target - num
        if complement in num_list:
            return num, complement
    return None

nums = [3, 6, 17, 23]
print("Two numbers with sum 20:", find_two_numbers(nums, 20))


# Sum of list elements (simple version)
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

numbers = [2, 8, 45, 6, 9, 3, 7, 1]
print("Sum of list:", sum_list(numbers))


# Example: ignore numbers between 6 and 7 while summing
lst = [2, 6, 1, 6, 4, 5, 7, 7]
total = 0
add_numbers = True
for num in lst:
    if num == 6:
        add_numbers = False
    elif num == 7:
        add_numbers = True
    elif add_numbers:
        total += num
print("Special sum (ignoring between 6 and 7):", total)


# Reverse a part of a list
lst = [1, 2, 3, 4, 5, 6, 7, 8]
index = 4
for i in range(index // 2):
    lst[i], lst[index - 1 - i] = lst[index - 1 - i], lst[i]
print("Partially reversed list:", lst)


# Palindrome checker
def is_palindrome(word):
    return word == word[::-1]

word = "madam"
print(f"Is '{word}' a palindrome?", is_palindrome(word))


# Reverse a part of a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
index = 4

for i in range(0, index // 2):
    saved_value = numbers[i]
    numbers[i] = numbers[index - 1 - i]
    numbers[index - 1 - i] = saved_value

print(numbers)



#reverse_around_index
list = [1,2,3,4,5,6,7,8,9]
index = 4
smallest = min(index, len(list) - index)

for i in range(index, index + smallest + 1):
    list[index - (i - index)], list[i] = list[i], list[index - (i - index)]

print(list)


# reverse the side of list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 3

if index < (len(numbers) - 1) // 2:
    for i in range(index + 1):
        numbers[i], numbers[index - i] = numbers[index - i], numbers[i]

elif index > (len(numbers) - 1) // 2:
    for i in range(index, len(numbers)):
        numbers[i], numbers[len(numbers) - 1 - (i - index)] = numbers[len(numbers) - 1 - (i - index)], numbers[i]

print(numbers)


