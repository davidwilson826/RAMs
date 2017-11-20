f = input("Please enter a function: ")
int_start = int(input("Please enter an interval start: "))
int_stop = int(input("Please enter an interval stop: "))
n_shapes = int(input("Please enter the number of shapes: "))

def f_fun(x):
    global f
    
    f_list = []
    i = 0
    
    while i < len(f):
        f_list.append(f[i])
        i += 1
    
    while 'x' in f_list:
        f_list[f_list.index('x')] = x
    
    print(f_list)
    
    f = ''.join(str(x) for x in f_list)
    print(f)
    
    return eval(f)
    
l = (int_stop-int_start)/n_shapes

x_values = [int_start+l*n for n in range(n_shapes)]

print(x_values)
    
print(f_fun(3))
    
'''    
print(f_list)

x = 3

for x in f:
    if x == 'x':
        f[f.find(x)] == x
        
print(str(eval(f)))
'''