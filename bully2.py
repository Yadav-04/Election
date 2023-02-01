class process:
    def __init__(self, id):
        self.id = id
        self.active = True

pList = []
initial = int(input("Enter number of processes: "))
for i in range(initial):
    pList.append(process(i))

while True:
    print("1. Add process")
    print("2. Kill process")
    print("3. Print active processes")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        id = int(input("Enter process id: "))
        pList.append(process(id))
        print("Process ",id," added")

    elif choice == 2:
        if len(pList) == 0:
            print("No active processes")
        else:
            id = int(input("Enter process id to kill: "))
            for i in range(len(pList)):
                if pList[i].id == id:
                    pList[i].active = False
                    print("Process ",id," killed")
                    break
            spotter = int(input("Enter process id that spots the failure: "))
            spotted = False
            for i in range(len(pList)):
                
                if pList[i].id == spotter:
                    spotted = True
                if spotted:
                    for j in range(i+1,len(pList)):
                        if pList[j].active:
                            print("Election message sent from ",pList[i].id," to ",pList[j].id)
                            print("Reply message sent from ",pList[j].id," to ",pList[i].id)
                            print("\n")
            print("\n\nProcess ",pList[i].id," is elected as the new coordinator")

    elif choice == 3:
        print("Active processes are: ")
        for i in pList:
            if i.active == True:
                print(i.id, end = ", ")
        print()


    elif choice == 4:
        break
