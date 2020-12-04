def Task(functions,input_list):
    task_results = []
    final_results = []
    for x in input_list:
        task_results.append(functions[0](x))
    for y in task_results:
        final_results.append(functions[1](y))
    return max(final_results)
def F1(x):
    return x*2
def F2(x):
    return x*3

functions = [F1,F2]
input_list = [1,2,3]
print (Task(functions, input_list))
