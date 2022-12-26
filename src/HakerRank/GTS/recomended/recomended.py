from src.Utilities.data_loader import DataLoader

# ----------------
# Count Inversions
# ---------------

# -------------
# (brute force)
# -------------
def countInversions(arr):
    size =len(arr)
    inv_count=0
    for curr in range(size-1):
        for right in range(curr+1,size):
            if arr[curr]>arr[right]: # compare curren elements with all elemenmts to its right
                inv_count+=1
    return inv_count
# -------------
# END(brute force)
# -------------

# -------------
# (efficient)
# -------------
def inversion_count(lst, n):
    """
    Function to find inversion count
    :param lst: List of integers
    :return: The inversion count of the list
    """""
    temp = [0] * n
    return inversion_count_recursive(lst, temp, 0, n - 1)


def inversion_count_recursive(lst, temp, left, right):
    """
    This Function will use merge_sort to count inversions
    :param lst: List of integers
    :param left: Left sided index of the list
    :param right: Right sided index of the list
    :return: Inversion count of the list
    """

    inv_count = 0

    # Make a recursive call if and only if there are more than one elements

    if left < right:
        # mid is calculated to divide the lst into two sublists
        mid = (left + right) // 2

        # Inversion count calculated in the left sublstay

        inv_count += inversion_count_recursive(lst, temp,left, mid)

        # Inversion count calculated in right sublstay

        inv_count += inversion_count_recursive(lst, temp,mid + 1, right)

        # Merge two sublists in a sorted list
        inv_count += find_inversion_count(lst, temp, left, mid, right)
    return inv_count


def smallestNegativeBalance(debts):
    ballance_account_map = {}

    for i in range(len(debts)):
        borrower = debts[i][0]
        lender = debts[i][1]
        value = int(debts[i][2])
        if borrower in ballance_account_map:
            ballance_account_map[borrower] -= value
        else:
            ballance_account_map[borrower] =- value

        if lender in ballance_account_map:
            ballance_account_map[lender] += value
        else:
            ballance_account_map[lender] = value
    print(ballance_account_map)


def find_inversion_count(lst, temp, left, mid, right):
    """
    This function will find_inversion_count of two sub-lists in a single sorted sub-list
    :param lst: List of integers
    :param left: Left sided index of the list
    :param right: Right sided index of the list
    :param mid: Middle index of the list
    :return: Inversion count of the list
    """
    i = left  # Left sublist starting index
    j = mid + 1  # Right sublist starting index
    k = left  # Sorted sublist starting index
    inv_count = 0  # Store inversion counts in each recursive call

    while i <= mid and j <= right:
        print(f'left sublist {lst[i]} compare with {lst[j]}')

        # Inversion does not occur
        if lst[i] <= lst[j]:
            print('Inversion Does not occure')

            temp[k] = lst[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            print('Inversion occures')
            temp[k] = lst[j]
            inv_count += (mid - i + 1)
            print(f'Inversion increased by {inv_count}')
            k += 1
            j += 1

    # The remaining elements of left sublist into temporary lst
    while i <= mid:
        temp[k] = lst[i]
        k += 1
        i += 1

    # The remaining elements of right  sublist into temporary lst
    while j <= right:
        temp[k] = lst[j]
        k += 1
        j += 1

    # The sorted sublist copied into original list
    for index in range(left, right + 1):
        lst[index] = temp[index]

    return inv_count

# -------------
#END (efficient)
# -------------

# -------------
# Region Parking Dilema
# -------------

def parking_dilema(cars,k):
    cars.sort()
    results=float("inf")
    n=len(cars)
    for i in range(n-k+1):
        results=int(min(results,cars[i+k-1]-cars[i]+1))
    return results
# -------------
# END Region Parking Dilema
# -------------



# -------------
# Region Parking Dilema
# -------------


def lengthOfLIS(nums) -> int:
    dp=[1]*len(nums)
    n=len(nums)

    for i in range(1,n):
        for j in range(i):
            if nums[j]<nums[i] and dp[i]>=dp[j]:
                dp[i]=dp[j]+1
    return max(dp)



    # Driver code to test above functions



if __name__ == '__main__':
    balance=[['Alex', 'Blake', '2'],
             ['Blake', 'Alex', '2'],
             ['Casey', 'Alex', '5'],
             ['Blake', 'Casey', '7'],
             ['Alex', 'Blake', '4'],
             ['Alex', 'Casey', '4']]
    smallestNegativeBalance(balance)
    lengthOfLIS(nums=[10,9,2,5,3,7,101,18])
    parking_dilema(cars=[10,8,2,17],k=2)

    # -------------
    # Region Swap values without auxilary variable
    # -------------
    x = 4
    y = 8
    #################
    x = x + y
    y = x - y
    x=x-y
    #################
    # -------------
    # Region Swap values without auxilary variable
    # -------------

    data_feeder=DataLoader()
    test_input=data_feeder.feed_from_txt(file_name="/io/Input_query/count_inversions.txt",
                                         as_type='int')


