import random

fakeDBList = ["Chowmein","Chicken tandoori roll",'Shawarma roll',"Sandwich"]
newfakeDBList = []
print("==========================================================================")
i = 0
k = 0
for singlefakeDBList in fakeDBList:
    i += 1
    print("       No.",i," ", singlefakeDBList)
print("       Do you wanna select from existing menu?")
print("       Type Y/N")
choiceFlag = input("       ")
try:
    if(choiceFlag == 'y' or choiceFlag == 'Y'):
        randomNum = random.randint(1, 4)
        print("       Machine have chossed ~",fakeDBList[randomNum-1],"~ for you")

    elif(choiceFlag == 'n' or choiceFlag == 'N'):
        print("       How many item you wanna add?")
        try:
            newFakeDBListLength = int(input("       "))
            if type(newFakeDBListLength) is int:
                for j in range(newFakeDBListLength):
                    properInputFlag = False
                    while(properInputFlag is False):
                        print("            Enter no. ",j+1,"item")
                        newItemBuffer = str(input("            "))
                        if (len(newItemBuffer) > 20):
                            print("       Sorry item name too long")
                        elif(len(newItemBuffer) < 3):
                            print("       Sorry item name too short")
                        else:
                            newfakeDBList.append(newItemBuffer)
                            properInputFlag = True
                print("       ----You have listed below item----")
                for singleNewfakeDBList in newfakeDBList:
                    k += 1
                    print("       No.",k," ", singleNewfakeDBList)
                randomNum = random.randint(1, newFakeDBListLength)
                print("       Machine have chossed ~",newfakeDBList[randomNum-1],"~ for you")

            else:
                print("       !!!!!!!!!!!!!!!  Wrong input !!!!!!!!!!!!!!!")

        except:
            print("       !!!!!!!!!!!!!!!  Wrong input !!!!!!!!!!!!!!!")

    else:
        print("       !!!!!!!!!!!!!!!  Wrong selection !!!!!!!!!!!!!!!")
        
except:
    pass