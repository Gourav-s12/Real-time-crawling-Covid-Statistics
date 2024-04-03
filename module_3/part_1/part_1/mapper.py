import sys
filename = sys.argv[1]
country_name = sys.argv[2]
file = open(filename)
for line in file:
    line1 = line.strip()
    if line1[0] == '#':
        print(line1)
        continue
    data = line1.split("  ")
    if data[1] ==country_name or data[1] == 'World':
        print(line)
