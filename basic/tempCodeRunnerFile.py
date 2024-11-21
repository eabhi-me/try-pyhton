result = []
while True:
    line = input()
    if line.endswith("."):
        result.append(line[::2])
        break
    else:
        result.append(line[::2])
print(" ".join(result))