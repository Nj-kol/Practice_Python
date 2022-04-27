# Custom generator simulating the range function
def my_range(start):
    current = start
    while True:
        yield current
        current += 1


nums = my_range(1)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))