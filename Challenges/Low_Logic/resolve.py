import csv

output = ''

# Open input.csv
with open('hw_lowlogic/input.csv', mode='r') as infile:
    data = csv.reader(infile)
    next(data)

    # Read input from input.csv
    for lines in data:
        input1 = int(lines[0])
        input2 = int(lines[1])
        input3 = int(lines[2])
        input4 = int(lines[3])

        final_output = (input1 & input2) | (input3 & input4)  # Final OR operation

        output += str(final_output)


print(output)
