# python3
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product
input_n = int(input("Enter the len"))
input_numbers = [int(x) for x in input().split()]
print(max_pairwise_product(input_numbers))
