
Slip 25

#Q.1 Write a program to find and display perfect numbers from a list.


def is_perfect(number):
    if number < 1:
        return False
    sum_of_divisors = sum(i for i in range(1, number) if number % i == 0)
    return sum_of_divisors == number

numbers = [6, 28, 15, 23, 496, 12, 8128]

perfect_numbers = [num for num in numbers if is_perfect(num)]
print("Perfect numbers in the list:", perfect_numbers)

"""Output:
Perfect numbers in the list: [6, 28, 496, 8128]"""


