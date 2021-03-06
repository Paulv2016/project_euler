# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# What is the value of the first triangle number to have over five hundred divisors?


#completed
current_triangle_nums = [1, 3]

def increment_triangle_num(current_triangle_nums):
    increment_amount = current_triangle_nums[1] - current_triangle_nums[0] + 1
    current_triangle_nums[0] = current_triangle_nums[1]
    current_triangle_nums[1] = current_triangle_nums[1] + increment_amount


# This is brute forced, could be improved
def calculate_divisors(number):
    divisor_count = 0
    i = 1
    while i <= number**.5:
        if number % i == 0:
            divisor_count += 1
            if i != (number / i):
                divisor_count += 1
        i += 1
    return divisor_count

def calc_triangle_with_more_than_x_divisors(divisor_count, current_triangle_nums):
    if divisor_count < 1:
        return 0

    if divisor_count == 1:
        return 3


    divisors = calculate_divisors(current_triangle_nums[1])

    while divisors <= divisor_count:
        increment_triangle_num(current_triangle_nums)
        divisors = calculate_divisors(current_triangle_nums[1])

    return current_triangle_nums[1]


triangle_500_divisors = calc_triangle_with_more_than_x_divisors(500, current_triangle_nums)

print(triangle_500_divisors)
