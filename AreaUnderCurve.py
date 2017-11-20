f = input("Please enter a function: ")

f_list = []
i = 0
while i < len(f):
    f_list.append(f[i])
    
print(f_list)

x = 3

for x in f:
    if x == 'x':
        f[f.find(x)] == x
        
print(str(eval(f)))