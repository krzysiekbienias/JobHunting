from collections import Counter


# -------------------
# Incorrect Passcode Attempts (Eeasy)
# --------------------
def incorrectPasscodeAttempts(passcode,attempts):
    status =False
    trails=10
    while trails>0:
        for attempt in attempts:
            if attempt!=passcode:
                trails-=1
            else:
                trails=10
    else:
        status=True

    return status
# -------------------
# END Incorrect Passcode Attempts (Easy)
# --------------------


# -------------------
# Campus Cup (Medium)
# --------------------
def split_email(email):
    return email.split("@")[-1]

def get_bonus_space(points):
    # TO DO  Fix intervals
    if points<100:
        return 0
    if points>=100 and points<200:
        return 3
    if points >= 200:
        return 8
    if points >= 300:
        return 15
    if points >= 500:
        return 25



def campusCup(emails):
    domains=list(map(split_email,emails))
    a_dic=dict(Counter(domains))
    a_dic.update((key,value*20) for key, value in a_dic.items())
    space_dict={k:get_bonus_space(points) for k,points in a_dic.items()}
    sorted_dict_values_then_keys={k:v for k, v in sorted(space_dict.items(),key=lambda item:(item[1]))}
    sorted_keys=list(sorted_dict_values_then_keys.keys())
    return sorted_keys
# -------------------
# End Campus Cup (Medium)
# --------------------




if __name__=="__main__":
    # few tests does not pass

    campus=campusCup(emails=["b@rain.ifmo.ru",
                             "c@rain.ifmo.ru",
                             "d@rain.ifmo.ru",
                             "e@rain.ifmo.ru",
                             "f@rain.ifmo.ru",
                             "g@rain.ifmo.ru",
                             "h@rain.ifmo.ru",
                             "i@rain.ifmo.ru",
                             "j@rain.ifmo.ru",
                             "k@rain.ifmo.ru",
                             "l@rain.ifmo.ru",
                             "m@rain.ifmo.ru",
                             "n@rain.ifmo.ru",
                             "o@rain.ifmo.ru",
                             "p@rain.ifmo.ru",
                             "q@rain.ifmo.ru",
                             "r@rain.ifmo.ru",
                             "s@rain.ifmo.ru",
                             "t@rain.ifmo.ru",
                             "u@rain.ifmo.ru",
                             "v@rain.ifmo.ru",
                             "w@rain.ifmo.ru",
                             "x@rain.ifmo.ru",
                             "y@rain.ifmo.ru",
                             "a@mit.edu.ru",
                             "b@mit.edu.ru",
                             "c@mit.edu.ru",
                             "d@mit.edu.ru",
                             "e@mit.edu.ru",
                             "f@mit.edu.ru",
                             "g@mit.edu.ru",
                             "h@mit.edu.ru",
                             "i@mit.edu.ru",
                             "j@mit.edu.ru",
                             "k@mit.edu.ru",
                             "l@mit.edu.ru",
                             "m@mit.edu.ru",
                             "n@mit.edu.ru",
                             "o@mit.edu.ru"])


    incorrectPasscodeAttempts(passcode="1234",
                          attempts=["9999",
                                     "9999",
                                     "9999",
                                     "9999",
                                     "9999",
                                     "9999",
                                     "9999",
                                     "1234",
                                     "9999",
                                     "9999",
                                     "9999",
                                     "9999"])

