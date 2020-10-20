count=1
while(count<5):
    print(count)
    count=count+1
else:
    print("jj")

print(count)

x=range(10)
print(x)

y=list (range(10))
print(y)

for var in list(range(10)):
    print(var)

for var in 'Uv':
    print(var)


for var in range(2,6):
    print(var)

for var in range(2,60,3):
    print(var)

for i in range(1,11):
    for j in range(1,11):
        print("i=",i,"j",j)

for letter in 'udara':
    if letter=='r':
        continue
    print(letter)

var=10
while var>0:
    print(var)
    var=var-1
    if var==5:
        break