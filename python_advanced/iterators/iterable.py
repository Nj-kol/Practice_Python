
num = [1,2,3,4,5]

# Two ways of getting an interator
i_num = num.__iter__()
i_num = iter(i_num)

# Simulate a for loop
while True:
    try:
        line = next(i_num)
        print(line)
    except StopIteration:
        break

# See StopIteration
print(next(i_num))