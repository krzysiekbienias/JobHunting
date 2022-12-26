def missingNumbers(arr, brr):
    missing_container = []
    org_dic = dict()
    sub_dic = dict()
    for s in brr:
        if s in org_dic:
            org_dic[s] += 1
        else:
            org_dic[s] = 1

    for u in arr:
        if u in sub_dic:
            sub_dic[u] += 1
        else:
            sub_dic[u] = 1

    for s in org_dic:
        if s not in sub_dic.keys():
            missing_container.append(s)
        elif s in sub_dic.keys() and org_dic[s] == sub_dic[s]:
            continue
        else:
            missing_container.append(s)
    missing_container.sort()
    final = list(set(missing_container))
    return final



# ----------------
# MinimumLoss
# ---------------

# -------------
# (brute force)
# -------------
def minimumLoss(arr):
    min_loss=float("-inf")
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j]-arr[i]<0:
                min_loss=max(arr[j]-arr[i],min_loss)
            else:
                continue
    return abs(min_loss)

# -------------
# (optimal)
# -------------
def minimumLoss_optimal(arr):
    hastab=dict(zip(arr,range(len(arr)))) #only works if all prices are different
    arr.sort()
    min_loss=float("inf")

    for i in range(1,len(arr)):
        if hastab[arr[i]]<hastab[arr[i-1]]:
            min_loss=min(min_loss,arr[i]-arr[i-1])
            print(f'selling with loss possible.Loss = {min_loss}')
        else:
            print('selling with provit or Not valid.')
    return abs(min_loss)





# ----------------
# Minimumloss
# ---------------

if __name__=="__main__":

    minimumLoss_optimal(arr=[20,7,8,2,5])

