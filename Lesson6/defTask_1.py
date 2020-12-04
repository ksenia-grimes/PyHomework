def Task(functions,input_list):
    task_results = []
    final_results = []
    for x in input_list:
        task_results.append(functions[0](x)) #выполняет F1 для каждого элемента входного списка и помещает результат в новый список task.results
    for y in task_results:
        final_results.append(functions[1](y)) #выполняет F2 для каждого элемента нового списка task.results (список с результатами F1) и помещает результат в final_results
    return max(final_results)
def F1(x):
    return x*2
def F2(x):
    return x*3

functions = [F1,F2]
input_list = [1,2,3]
print (Task(functions, input_list))
