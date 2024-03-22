import sys
count = 0
last = ""
world_data = []
country_data = []
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

for line in sys.stdin:
    line1 = line.strip()
    if len(line1)<1:
        continue
    if line1[0] == '#':
        print(line1,'\n')
        continue
    data = line1.split("  ")
    if data[1] == 'World':
        for i in data:
            world_data.append(i)
    else:
        for i in data:
            country_data.append(i)
for i in range(len(country_data)):
    country_data[i]=country_data[i].replace('+','')
    country_data[i]=country_data[i].replace(',','')
for i in range(len(world_data)):
    world_data[i]=world_data[i].replace('+','')
    world_data[i]=world_data[i].replace(',','')
for i in world_data:
    print(i,"  ",end='')
print('\n')
for i in country_data:
    print(i,"  ",end='')
print('\n')
percent = []
percent.append(country_data[0])
percent.append(country_data[1])
i=2
while i in range(len(world_data)):
    if is_float(country_data[i]) and is_float(world_data[i]):
        x = (float(country_data[i])/float(world_data[i]))*100
        percent.append(x)
    else:
        percent.append('NA')
    i+=1

print("Percent:- \n")
for i in percent:
    print(i,"  ",end='')
