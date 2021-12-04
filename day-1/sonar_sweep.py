input = open('input.txt').readlines()

increments = 0

for i, line in enumerate(input):
    if (i == 0):
        continue;

    if (int(line) > int(input[i - 1])):
        increments = increments + 1

print(increments)