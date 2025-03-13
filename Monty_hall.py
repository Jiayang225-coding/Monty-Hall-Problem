import random


possible_outcome  = ["goat", "goat", "car"]
def game(possible_out):
    ''' 
    对函数功能的描述
    函数的输入
    函数的输出是什么
    '''
    #将可能的结果打乱
    random.shuffle(possible_out)

    # 把门后放入对应的东西
    door_names = ["A", "B", "C"]
    doors_shuffle = {}
    for i in range(3):
        doors_shuffle[door_names[i]] = possible_out[i]

    #我的选择:我们从door_names 里面选
    my_choice = random.choice(door_names)
    

    #主持人的选择： 不能选我的，也不能选车
    host_choice = ""
    #这里是车对应的门
    for i in doors_shuffle:
        if doors_shuffle[i] == "car":
            car_choice = i
    
    del_list = []

    for i in door_names:
        if i == my_choice:
            del_list.append(i)
        if i == car_choice:
            del_list.append(i)

    for i in del_list:
        if i in door_names:
            door_names.remove(i)

    #print(door_names)

    host_choice = door_names[0]

    return my_choice, host_choice, car_choice
    
    
def new_choice(mine,host):
    all_choices = ["A", "B", "C"]

    del_list_1 = []
    for i in all_choices:
        if i == host:
            del_list_1.append(i)
        if i == mine:
            del_list_1.append(i)

    for i in del_list_1:
        if i in all_choices:
            all_choices.remove(i)

    return all_choices



mine, host , car = game(possible_outcome)
print(mine, host, car)

#这里是排除之后的
choice_left = new_choice(mine, host)
print(choice_left)


TOTAL_RUN = 20000
count = 0

for i in range(TOTAL_RUN):
    mine, host, car = game(possible_outcome)
    choice_left = new_choice(mine, host)

    if choice_left[0] == car:
        count+=1

result = count/TOTAL_RUN

print(result)