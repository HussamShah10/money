import random 

randomNum = random.randint(1,15)
finishedThing = []
count = 1 
while count <= randomNum:
    finishedThing.append(count)
    count += 1
print(finishedThing)

x= random.randint(1, randomNum)
finishedThing.remove(x)


print(f"random num removed: {x}")
print (f"removed list: {finishedThing}")

def Missing(finishedThing):
    count1 = 0
    for i in finishedThing:
        count1 += 1
        if count1 not in finishedThing:
            finishedThing.insert(finishedThing.index(count1+1),count1)
            print("missing number: ", count1)
    if randomNum == x:
        finishedThing.append(x)
    print(finishedThing)

Missing(finishedThing)

