import pandas as pd

def incremental_backups(last_backup_time,changes):
    results=[]
    for change in changes:
        if change[0]>last_backup_time and change[1] not in results:
            results.append(change[1])
        else:
            continue
    results.sort()
    return results




if __name__=="__main__":
    incremental_backups(last_backup_time=461620205,
                        changes=[[461620203, 1],
                                   [461620204, 2],
                                   [461620205, 6],
                                   [461620206, 5],
                                   [461620207, 3],
                                   [461620207, 5],
                                   [461620208, 1]])
