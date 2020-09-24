student = []
stu_data = {}

def asker():
    for i in range(0, 1):
        print(f"Enter 1 to ADD Student Details\nEnter 2 for UPDATE Student Details\nEnter 3 for SHOW Student Result\nEnter 4 to EXIT\nEnter 5 to Repet\n")
        choice = int(input("Enter your Choice : "))
        if (choice in range(1, 6)):
            if choice == 1:
                add_proc()
                break
            elif choice == 2:
                print("2")
                break
            elif choice == 3:
                show()
                break
            elif choice == 4:
                print("4")
                break
            elif choice == 5:
                 asker()
        else:
            print("you are done")

def add_sub(): 
    subjects = [] 
    subjects_data = {}
    def line():
        sub = input("\n Enter Subject Name                  : ").upper()
        opt = input("\n Enter the obtained Marks by Student : ")
        tot = input("\n Total No of Marks                   : ")
        subjects_data[ sub ] = opt, tot

    line()
    ask = input("Want to add more subjects Y/N : ").lower()
    if ask == 'y':
        line()
    elif ask == 'n':
        print("OKKKKK")
    subjects.append(subjects_data)
    stu_data['subjects'] = subjects



def add_proc():
    roll = input("\n\n  1. Enter Student Roll.No : ")
    name = input("\n  2. Enter Student First Name : ").upper()
    mname = input("\n  3. Enter Student Middle Name : ").upper()        
    lname = input("\n  4. Enter Student Last Name : ").upper()
    mother = input("\n  5. Enter Mother First Name : ").upper()
    mmother = input("\n  6. Enter Mother Middle Name : ").upper()
    father = input("\n  7. Enter Father First Name : ").upper()
    mfather = input("\n  8. Enter Father Middle Name : ").upper()
    date = input("\n  9. Enter the Date of Birth :")
    month = input("\n 10. Enter the Month of Birth :")
    year = input("\n 11. Enter the Year of Birth :")
    school = input("\n 12. Enter the School Name : ").upper()
    stu_data['rollno'] = roll
    stu_data['name'] = name
    stu_data['mid_name'] = mname
    stu_data['last_name'] = lname
    stu_data['mname'] = mother
    stu_data['mmid_name'] = mmother
    stu_data['fname'] = father
    stu_data['fmid_name'] = mfather
    stu_data['date'] = date
    stu_data['month'] = month
    stu_data['year'] = year
    stu_data['school'] = school

    sl = input("\n\n  Do you want to add Subjects and MARKS type Y  or go to Main Menu type M :").lower()
    if sl == 'y':
        add_sub()
    elif sl == 'm':
        print("OKKKKK")
    student.append(stu_data.copy())
    choice = int(input(" Want to Add More Students\n Enter your Choice : "))
    if choice == 1:
        add_proc()
    elif choice ==2:
        print(student)
    else:
        asker()

def show():
    s = " "
    d = "-"
    print("\n For which Student you want to print Reslt :  ")
    for g in student:
        print(f"{ s * 45}{g['name']}")
    select = input("\n Select from name avalaible Above : ").upper()
    for h in student:
        if h['name'] == select:
            print(f"\n\n|{ d * 30 } CENTRAL BOARD OF SECONDAY EDUCATION { d * 30 }|\n|{ s * 41 }MARKS STATEMENT{ s * 41 }|\n|{ s * 32 }SECONDAY SCHOOL EXAMINATION, 2020{ s * 32 }|")
            print(f"|{ s * 97 }|\n|{ s * 97 }|")
            print(f"|{ s * 10 }Name          : { s * 71 }|\n|{ s * 10 }Fathers Name  : { s * 30 }Roll.No :{ s * 32 }|\n|{ s * 10 }Mothers Name  : { s * 71 }|\n|{ s * 10 }Date of Birth : { s * 71 }|\n|{ s * 10 }School        : { s * 71 }|\n|{ s * 97 }|\n|  |{ d * 8 }|{ d * 24 }|{ d * 44 }|{ d * 12 }|{ s * 2 }|")
            print(f"|  |{ s * 8 }|{ s * 24 }|{ s * 20 }MARKS{ s * 19 }|{ s * 12 }|{ s * 2 }|\n|{ s * 2 }|  SUB   |{s * 8 }SUBJECT{ s * 9 }|{ d * 44 }| POSITIONAL |{ s  * 2 }|\n|{ s  * 2 }|  CODE  |{ s  * 24 }|  TOTAL  |  OBTAINED  |{ s  * 6 }IN WORDS{ s  * 7 }|    GRADE   |{ s  * 2 }|\n|  |{ d * 8 }|{ d * 24 }|{ d * 9 }|{ d * 12 }|{ d * 21 }|{ d * 12 }|{ s * 2 }|\n|  |{ s * 8 }|{ s * 24 }|{ s * 9 }|{ s * 12 }|{ s * 21 }|{ s * 12 }|{ s * 2 }|\n|  |{ s * 8 }|{ s * 24 }|{ s * 9 }|{ s * 12 }|{ s * 21 }|{ s * 12 }|{ s * 2 }|\n|  |{ s * 8 }|{ s * 24 }|{ s * 9 }|{ s * 12 }|{ s * 21 }|{ s * 12 }|{ s * 2 }|")
            print(f"|  |{ d * 8 }|{ d * 24 }|{ d * 9 }|{ d * 12 }|{ d * 21 }|{ d * 12 }|{ s * 2 }|\n|{ s * 97 }|\n|{ s * 97 }|\n|{ s * 34 }Result :{ s * 55 }|\n|{ s * 97 }|\n|{ d * 97 }|")
        else:  
            print("trying again")
            show()
            

asker()



















#def cre_stu(rollno, name, mid_name='', last_name='', mname, mmid_name='', fname, fmid_name='', date, month, year, school)




























'''num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

>>> def n2w(n):
        try:
            print num2words[n]
        except KeyError:
            try:
                print num2words[n-n%10] + num2words[n%10].lower()
            except KeyError:
                print 'Number out of range'

>>> n2w(0)
Zero
>>> n2w(13)
Thirteen        
>>> n2w(91)
Ninetyone
>>> n2w(21)
Twentyone
>>> n2w(33)
Thirtythree'''

'''def crate_student(sno, name, mid_name=' ',last_name='', age=18):
    student = {
        'full_name': name + mid_name + last_name,
        'sno': sno,
        'age': age > 18 and age or 18
    }
    # print (student)
    return student

print ("Enter sno")
sno = input()
# print (crate_student(sno,last_name="bod", age=24))

print (crate_student(sno, "Rani",last_name="bod", age=24))'''