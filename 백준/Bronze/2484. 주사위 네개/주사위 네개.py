n = int(input())
dice_num = [list(map(int, input().split())) for _ in range(n)]
dice_list = [0]*6
max_first = -1
max_second = -1
result = 0
max_result = 0
for i in range(len(dice_num)):
    for j in range(len(dice_num[0])):
        dice_list[dice_num[i][j]-1] += 1
    for j in range(len(dice_list)):
        if dice_list[j] >= 3:
            max_first = j
            break
        elif dice_list[j] == 2:
            if len(list(set(dice_num[i]))) == 3:
                max_first = j
                break
            else:
                max_first = list(set(dice_num[i]))[0]-1
                max_second = list(set(dice_num[i]))[1]-1
    if max_first == -1:
        result = max(dice_num[i])*100
    elif dice_list[max_first] == 4:
        result = 50000 + (max_first+1) * 5000
    elif dice_list[max_first] == 3:
        result = 10000 + (max_first+1) * 1000
    elif dice_list[max_first] == dice_list[max_second] and max_second != -1:
        result = 2000 + (max_first+1)*500 + (max_second+1)*500
    elif dice_list[max_first] == 2:
        result = 1000 + (max_first+1)*100
    if max_result < result: 
        max_result = result
    dice_list = [0] * 6
    max_first = -1
    max_second = -1
    result = 0
print(max_result)

