
#part A
'''
c_arr = [3, 3, 6, 4]
t_arr = [8, 13, 20, 30]
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
c_arr = [2, 10, 9]
t_arr = [6, 24, 36]
'''


import math

num_task = len(c_arr)
r_iter_0 = sum(c_arr)

def calculate_iteration(prev_resp_time, idx):
    ret = 0
    for i in range(num_task):
        if i == idx:
            ret += c_arr[i]
        else:
            ret += math.ceil(prev_resp_time / t_arr[i]) * c_arr[i]
    return ret

r_arr = []
r_arr.append([])
# init r
for i in range(num_task):
   r_arr[0].append(r_iter_0)

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
