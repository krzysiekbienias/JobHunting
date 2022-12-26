# ---------------
# Vertical sticks
# ---------------

import itertools


def len_of_rey(arr):
    n = len(arr)
    ray_container = []
    for i in range(n - 1, -1, -1):
        if i == 0:
            ray_container.append(1)
        else:
            max_ray = 1
            for j in range(i - 1, -1, -1):
                if arr[i] > arr[j]:
                    max_ray += 1
                    if j == 0:
                        ray_container.append(max_ray)
                else:
                    ray_container.append(max_ray)
                    break
    ans = ray_container[::-1]
    return ans


def per(arr):
    return list(itertools.permutations(arr))


def vertical_sticks(y):
    sum_container = []
    perm = per(y)
    perm = list(dict.fromkeys(perm))
    for el in perm:
        temp = sum(len_of_rey(el))
        sum_container.append((temp))
    return sum(sum_container) / len(sum_container)


# ---------------
# Vertical sticks
# ---------------

if __name__ == "__main__":
    # len_of_rey(arr=[2,1,3])
    vertical_sticks(y=[2, 2, 3])
