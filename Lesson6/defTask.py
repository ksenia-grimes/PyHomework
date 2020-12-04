input_list = [1,2,3]    
def Task(x):
    def F1(x):
        return x*2
    y = F1(x)
    def F2(y):
        return y*3
    return F2(y)
task_result=[]
for x in input_list:
    task_result.append(Task(x))
print (max(task_result))
