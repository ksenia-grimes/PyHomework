def Task(functions,input_list):
    copylist = input_list.copy()
    for f in functions: #input_list = map(f, input_list)
        for x in range(len(copylist)):
            copylist[x] = f(copylist[x])
    return max(copylist) 
    
def F1(x):
    return x*2 
def F2(x):
    return x*3
functions = [F1,F2]
input_list = [1,2,3]
print (Task(functions, input_list))
