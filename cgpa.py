def gpa():
    cg_sum = 0
    c_sum = 0
    n = int(input("Enter the number of subjects:"))
    for i in range(1, n + 1):
        print("Enter the credit for subject ", i)
        c = int(input())
        print("Enter the grade point for subject ", i)
        gp = int(input())
        cg_sum += c * gp
        c_sum += c

    gpa1 = format((cg_sum / c_sum), ".2f")
    return gpa1


def cgpa():
    gpa_sum = 0
    n = int(input("enter the sem no:"))
    for i in range(1, n + 1):
        print("Enter the GPA of sem ", i)
        gpa_sum += float(input())

    cgpa1 = format((gpa_sum / n), ".2f")
    return cgpa1


condition = True
while condition:
    print("1.GPA", "\n2.CGPA", "\n3.Exit")
    ch = int(input("Enter any choice"))
    if ch == 1:
        print(gpa())
    elif ch == 2:
        print(cgpa())
    elif ch == 3:
        condition = False
    else:
        print("Enter a valid choice")
