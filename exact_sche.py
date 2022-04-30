
#part A
'''
c_arr = [3, 3, 6, 4]
t_arr = [8, 14, 20, 30]
'''

#part B
'''
c_arr = [2, 4, 7, 8]
t_arr = [10, 16, 30, 50]
'''

#part C
'''
c_arr = [2.5, 4, 5.5, 9]
t_arr = [12, 16, 37, 52]
'''

#part D
'''
c_arr = [2, 10, 6]
t_arr = [6, 24, 39]
'''

#part E
#c_arr = [2, 10, 1]
#t_arr = [6, 24, 6]
'''
c_arr = [1, 2, 10]
t_arr = [4, 6, 24]
'''

#c1 = 0.036
#c1 = 0.01
#c1 = 1.31
c1 = 1.25

import math

def calculate_iteration(prev_resp_time, idx):
    ret = 0
    for i in range(idx+1):
        if i == idx:
            ret += c_arr[i] + b_arr[i]
        else:
            ret += math.ceil(prev_resp_time / t_arr[i]) * c_arr[i]
    return ret

#q2
#c0 = 26
for i in range(0, 1000):
    print(c1)
    c_arr = [1, c1, 3, 4]
    t_arr = [4, 6, 10, 20]

    num_task = len(c_arr)
    r_iter_0 = []

    q2 = False

    b_arr = [0, 0, 0, 0, 0]
    d_arr = [59, 50, 135, 180]
    if q2:
        b_arr = [0, 4, 5, 0]
        delta_arr = [0, 0, 0, 0, 0]

        for i in range(len(c_arr)):
            c_arr[i] += 1
            t_arr[i] += delta_arr[i]

    iter_0_sum = 0
    for num in c_arr:
        iter_0_sum += num
        r_iter_0.append(iter_0_sum)



    r_arr = []
    r_arr.append([])
    # init r
    for i in range(num_task):
       r_arr[0].append(r_iter_0[i] + b_arr[i])

    # calculation
    iter_cnt = 1
    while True:
        all_same = True
        curr_arr = []
        prev_arr = r_arr[iter_cnt-1]
        for i in range(num_task):
            curr_resp_time = calculate_iteration(prev_arr[i], i)
            curr_arr.append(curr_resp_time)

            if curr_resp_time != prev_arr[i]:
                all_same = False

        r_arr.append(curr_arr)
        if (all_same):
            break
        iter_cnt += 1

    # display iteration
    for i in range(len(r_arr)):
        print(i, r_arr[i])

    # check schedulability
    last_row = r_arr[-1]
    for i in range(num_task):
        if last_row[i] <= t_arr[i]:
            print("Task", i+1, "scheduable")
        else:
            print("Task", i+1, "NOT scheduable")
            exit(1)
    c1 += 0.0001

