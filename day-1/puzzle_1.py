input = open('input.txt').readlines()
input = [int(line.replace('\n', '')) for line in input]

increments = 0

for i, line in enumerate(input):
    if (i == 0):
        continue;

    if (int(line) > int(input[i - 1])):
        increments += 1

print(increments)