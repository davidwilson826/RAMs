from math import sin, cos, tan, pi, e

f_string = input("Please enter function \nf(x) = ") #Gathers function input
domain = input("Please enter a closed interval for the domain (ex. -1,1) ") #Gathers domain input
domain = [int(domain[:domain.index(',')]),int(domain[domain.index(',')+1:])] #Converts domain input to list form
step = int(input('Please enter a "step" value to control the precision of calculations '))

"""
Define f(x)
"""

fl_orig = [] #Defines fl_orig, which will contain items representing the various "pieces" (numbers, x, operations, etc.) of the function

n_test = ['0','1','2','3','4','5','6','7','8','9','10','.'] #List for testing for numbers

i = 0

while i < len(f_string): #Looks through string, examines each item, and adds it to list in the appropriate form
    if f_string[i] in n_test: #Adds multi-digit numbers (ex. 101) as list items
        num = ''
        while i < len(f_string) and f_string[i] in n_test:
            num += f_string[i]
            i += 1
        fl_orig.append(float(num))
    elif f_string[i] in ['s','c','t']: #Adds three-letter representations of trig functions (ex. sin) as list items
        tf = ''
        for x in range(3):
            tf += f_string[i]
            i += 1
        fl_orig.append(tf)
    elif f_string[i] == 'p': #Replaces letter p with decimal representation of pi, adds it to list
        fl_orig.append(pi)
        i += 1
    elif f_string[i] == 'e': #Replaces letter e with decimal representation of Euler's number, adds it to list
        fl_orig.append(e)
        i += 1
    else: #Adds items not in the above categories to list (includes 'x' and operation symbols)
        fl_orig.append(f_string[i])
        i += 1
        
#print(fl_orig) #Delete the hashtag at the beginning of this line if you would like to see the list representing the function

def f(x): #Defines function f
    global fl_orig
    f_list = fl_orig[:] #Creates f_list, a copy of fl_orig (This is done so that the original list remains "intact" and can be reused)
    i = 0
    while i < len(f_list): #Replaces 'x' with numerical value of x
        if f_list[i] == 'x':
            f_list[i] = x
        i += 1
            
    return evaluate(f_list) #Calls the evaluate function to calculate the result - returns this result
    
def evaluate(f_list): #Defines evalute function, which can compute any list using proper order of operates 
    while '_' in f_list: #Eliminates '_' and makes the number immediately after it negative
        i_neg = f_list.index('_')
        f_list = f_list[:i_neg]+[-1*f_list[i_neg+1]]+f_list[i_neg+2:]
    while '(' in f_list: #Searches for parentheses (loops until all parentheses have been eliminated)
        i_open = f_list.index('(')
        i_close = f_list.index(')')
        group = f_list[i_open+1:i_close] #Creates "group," which is a new list consisting of the contents of parentheses
        f_list = f_list[:i_open]+[evaluate(group)]+f_list[i_close+1:] #Calls the evaluate function for "group," and inserts the result into the list where the parentheses and their contents orginally were
    for tf in ['sin','cos','tan','csc','sec','cot']: 
        while tf in f_list: #Looks for trig functions and evaluates all of them until none are left
            t_i = f_list.index(tf)
            if tf == 'sin': #Determines if function is sin - if so, evaluates the sin of the number following the function
                result = sin(f_list[t_i+1])
            elif tf == 'cos': #Repeates for cos and other trig functions
                result = cos(f_list[t_i+1])
            elif tf == 'tan':
                result = tan(f_list[t_i+1])
            elif tf == 'csc':
                result = 1/sin(f_list[t_i+1])
            elif tf == 'sec':
                result = 1/cos(f_list[t_i+1])
            elif tf == 'cot':
                result = 1/tan(f_list[t_i+1])
            f_list = f_list[:t_i]+[result]+f_list[t_i+2:] #Inserts result of trig calculate into list and eliminates original function and number
    while '^' in f_list: #Evaluates all exponents
        op_i = f_list.index('^')
        result = f_list[op_i-1]**f_list[op_i+1] 
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:] #Inserts calculated result and eliminates base, exponent symbol, and power
    while '/' in f_list: #Replaces division with multiplication by the recipricol
        i = f_list.index('/')
        f_list[i+1] = 1/f_list[i+1]
        f_list[i] = '*'
    while '*' in f_list: #Evaluates all multiplication (same method as exponents)
        op_i = f_list.index('*')
        result = f_list[op_i-1]*f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
    while '-' in f_list: #Replaces subtraction with addition of the opposite
        i = f_list.index('-')
        f_list[i+1] *= -1
        f_list[i] = '+'
    while '+' in f_list: #Evaluates all addition (same method as exponents and multiplication)
        op_i = f_list.index('+')
        result = f_list[op_i-1]+f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
    return f_list[0] #List should now contain only one number, which represents the calculated result - function returns this number