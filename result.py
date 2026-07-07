name = input("Enter student name:-")
print("Enter the mark of the subjects:-")
sub1 = int(input("Enter mark of subject 1:- "))
sub2 = int(input("Enter mark of subject 2:- "))
sub3 = int(input("Enter mark of subject 3:- "))
Total = sub1 + sub2 + sub3
percentage = (Total / 300) * 100
print("name of student is:-",name)
print("Total marks :-",Total)
print("Percentage :-",percentage)