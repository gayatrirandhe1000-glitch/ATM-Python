# Write a program to Calculate Grades
marks = int (input("Enter your marks: "))
match marks:
    case marks if marks >=100:
        print("Invalid marks")
    case marks if marks >=90:
        print("Grade: A")
    case marks if marks >=80:
        print("Grade: B")   
    case marks if marks >=70:
        print("Grade: C")
    case marks if marks >60:
        print("Grade: D")
    case marks if marks < 60:
        print("Grade: F")
    case marks if marks <0:
        print("Invalid marks")
        