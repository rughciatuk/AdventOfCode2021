
import enum


with open("./input.txt", "r") as input_file:
    lines = [int(x.strip()) for x in input_file.readlines()]

answer = 0
for index, line in enumerate(lines):
    if index == 0:
        continue
    if line > lines[index -1]:
        answer += 1

print(answer)