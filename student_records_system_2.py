while True:
    print("\n---MENU---")
    print(""
          "1.Enter Students Records")
    print("2.Exit")
    choice=input("choose option")
    if choice=="1":
        num=int(input("How many students? "))
        for i in range(num):
            print("\nstudent", i+1)
            name= input("Enter student name: ")
            student_id=input("enter student id:")
            score=float(input("Enter score:"))
            print("\n---student record---")
            print("name:,name")
            print("ID:", student_id)
            if score>=70:
                print("Grade:A")
            elif score >=60:
                 print("Grade:B")
            elif score >=50:
                print("Grade:C")
            elif choice=="2":
                print("Exiting program")
            else:
                print("Invalid choice")
        break





