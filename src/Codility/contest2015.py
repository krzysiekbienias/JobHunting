small_letter='abcdefghijklmnopqrstuvwxyz'
capital_letter=small_letter.upper()
numbers='0123456789'
special_ch='!@#$%^&*()'


# ---------
# Region Longest Password
# ---------
def find_len(password):
    letter_counter=0
    number_counter=0

    for ch in password:
        if ch not in small_letter+capital_letter+numbers:
            return None
        if ch in small_letter or ch in capital_letter:
            letter_counter+=1
        elif ch in numbers:
            number_counter+=1
    if letter_counter%2==0 and number_counter%2!=0:
        return len(password)
    else :
        return None


def LongestPassword(S):
    max_lenght=-1
    characters=S.split()
    for password in characters:
        temp_lenght=find_len(password=password)
        if temp_lenght is not None:
            max_lenght=max(max_lenght,temp_lenght)
        else:
            continue
    return max_lenght

# ---------
# Region Longest Password
# ---------


# ---------
# Region First Unique
# ---------

def firstUnique(A):
    occurance_map = {}
    for a in A:
        if a in occurance_map:
            occurance_map[a] += 1
        else:
            occurance_map[a] = 1

    unique_el = [k for k, v in occurance_map.items() if v == 1]
    if len(unique_el) > 0:
        return unique_el[0]
    else:
        return -1
# ---------
# End Region First Unique
# ---------

print(solution('zxcasdqwe123'))

print('the end')