'''
https://leetcode.com/discuss/post/4154082/doordash-phone-eligible-order-sequence-b-y6ti/


[3, 1, 5, 4, 2]

First iter: 3 and both 5 eligible
Take 3

After that take 5
After processing the order [1, 4, 2]


'''

import heapq
def find_eligible_numbers(order_list):
    n = len(order_list)
    result = []
    heap = []
    # 判断某个索引是否是 eligible 的
    def is_eligible(index):
        if index < 0 or index >= len(order_list):
            return False
        left = order_list[index - 1] if index - 1 >= 0 else float('-inf')
        right = order_list[index + 1] if index + 1 < len(order_list) else  float('-inf')
        return order_list[index] > left and order_list[index] > right

    for i in range(n):
        if is_eligible(i):
            heapq.heappush(heap, (order_list[i], i))
    while heap:
        min_val, index = heapq.heappop(heap) # 取最小的 eligible
        result.append(min_val)
        order_list[index] = float('-inf')# 标记为已删除

         # 重新检查相邻元素是否符合条件
        for neighbor in [index - 1, index + 1]:
            if 0 <= neighbor < n and is_eligible(neighbor):
                heapq.heappush(heap, (order_list[neighbor], neighbor))
    print(result)
    return result
find_eligible_numbers(  [3, 5, 1, 5, 1, 4, 2])