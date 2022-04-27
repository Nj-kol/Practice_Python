
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

file_name="C:\\Users\\Nilanjan\\Workspaces\\derby.log"

# Decalare a generator comprehension
csv_gen = (row for row in open(file_name))

while True:
    try:
        line = next(csv_gen)
        print(line)
    except StopIteration:
        break

