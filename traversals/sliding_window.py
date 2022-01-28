# # K = 5
# # arr = [1,3,2,6,-1,4,1,8,2]

# # def find_contiguous(arr,K):
# #     results = []
# #     windowSum = 0.0
# #     windowStart = 0
# #     _sum = 0
# #     for windowEnd in range(len(arr)):
# #         _sum += arr[windowEnd]
# #         if windowEnd>= K-1:
# #             results.append(_sum/K)
# #             _sum -= arr[windowStart]
# #             windowStart += 1
# #     return results





# from curses import window


# def contiguous_sum_max(arr,K):
#     res = 0
#     _sum = 0
#     windowStart = 0

#     for windowEnd in range(len(arr)):
#         _sum += arr[windowEnd]

#         if windowEnd>=K-1:
#             if _sum>res:
#                 res = _sum
#             _sum -= arr[windowStart]
#             windowStart += 1
#     return res

# arr1 = [2, 3, 4, 1, 5]
# k1 = 2

# print(contiguous_sum_max(arr1,k1))



def smallest_subarray(arr,S):
    min_window_length = 10000
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum>= S:
            min_window_length = min(min_window_length, window_end-window_start+1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_window_length == 10000:
        return 0
        
    return min_window_length

arr =  [2,1,5,2,8]
S = 7

print(smallest_subarray(arr,S))
