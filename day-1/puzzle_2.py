input = open('input.txt').readlines()
input = [int(line.replace('\n', '')) for line in input]

window_increments = 0
previous = input[:2]

for x in range(1, len(input)-3):
    cur = input[x:x+3]
    if (sum(previous) < sum(cur)):
        window_increments += 1
    
    previous = cur

print(window_increments)