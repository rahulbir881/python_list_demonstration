import list_fun
names=[]
while(True):
    print("\n********************************MENU**************************************************")
    print("1.Add a student......2.Search a name......3.Display.......4.Delete a student\
        \n5.Sort the names......6.Count total students...............7.for exit")
    print("***********************************************************************************")
    user_input=int(input("Enter your choice: "))

    if user_input==1:
        name=input("Enter name: ")
        list_fun.add_names(name,names)
    elif user_input==2:
        name=input("Enter name you want to search: ")
        list_fun.search(name,names)
    elif user_input==3:
        list_fun.display(names)
    elif user_input==4:
        print("delete")
    elif user_input==5:
        print("sort")
    elif user_input==6:
        print("count")
    elif user_input==7:
        break
    else:
        print("Wrong input")

