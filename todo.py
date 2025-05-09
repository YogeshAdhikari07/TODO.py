#Hello so here we coding a simple todo list not graphical todo list 
#first making design of main
def main():
    pas(0,3)
#function to to the menu of todo list
def menu(l):
    print("""
.....................................................Welcome to the todo list program.............................................
Here  Select an operation to perform :
1.Add task to the todo list.
2.Remove task from the todo list.
3.See the whole todo list.
4.Exit the program.""")
    try:#This will allow user to input string but did not show the error just print the warning
        n=int(input("Enter the Task number:"))
    except ValueError:
        print("""
              Type task number not a string""")
        menu(l)
    if(n==1): #This if use to add task 
        t=str(input("Enter the task:"))
        d={"task":t}
        l.append(d)
        menu(l)
    elif(n==2):#This if use to remove task 
        print("\n")
        j = str(input("Copy & Paste the task: "))
        index_to_remove = None
        for i, task in enumerate(l):#here task is a variable which containing the value of dict inside the the list " l " and i keeping  the track of index
            if task.get("task") == j:
                index_to_remove = i
                break
        print("\n")
        if index_to_remove is not None:
            removed_task = l.pop(index_to_remove)
            print(f"{removed_task} task has been removed.")
            print("\n")
        else:
            print(f"No task found matching: {j}")
            print("\n")
        menu(l)
    elif(n==3):#This if use to see task 
        print("\n")
        if l:
            print("Here is the  all task:")
            for task in l:
                print(task.get("task"))
        else:
            print("No tasks in the todo list.")
        menu(l)
    elif(n==4):#This if use to end program
        exit()
#function to check password
def pas(count,r):
    l=[]
    print("     ")
    if(count<3):
        try:#This will allow user to input string but did not show the error just print the warning
            n=int(input("Enter the password :"))
        except ValueError:
                count+=1#this will count the number of try you have done
                r-=1#thsi will show the number of try remaining
                print(f"Try again(Try remain {r})\n.............................................")
                pas(count,r)
        if(n==4545):
            print("Password is correct\n\n")
            menu(l)
        else:
            count+=1
            r-=1
            print(f"Try again(Try remain {r})\n.............................................")
            pas(count,r)
    else:
        exit()
main()