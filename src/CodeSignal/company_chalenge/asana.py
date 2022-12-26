

def taskTypes(deadlines,day):
    diffs=[deadline -day for deadline in deadlines ]
    today=0
    upcoming=0
    later=0
    for d in diffs:
        if d<=0:
            today+=1
        elif d>=1 and d<=7:
            upcoming+=1
        else:
            later +=1
    return [today,upcoming,later]

def smartAssigning(names, statuses, projects, tasks):
    together = list(zip(names, statuses, projects, tasks))
    together.sort(key=lambda x: (x[1],x[3], x[2]))
    return together[0][0]

if __name__=="__main__":
    smartAssigning(names=["John","Martin"],
                   statuses=[False,False],
                   projects=[2,1],
                   tasks=[6,5])
    print(taskTypes(deadlines=[1, 2, 3, 4, 5],day=2))


