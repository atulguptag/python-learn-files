# Write a program to find whether a student is pass or fail, if it requires total 40% and at least 33% in each subject
# to pass. Assume 3 student and take marks as an input from user.

sub1 = int(input("Enter first subject marks:\n"))
sub2 = int(input("Enter second subject marks:\n"))
sub3 = int(input("Enter third subject marks:\n"))

# It means if the numbers in sub1, sub2 and sub3 are less than 33% then print you are fail.
if sub1 < 33 or sub2 < 33 or sub3 < 33:
    print("You are fail because you have less than 33% in one of the subjects")

# It means if the total numbers in sub1, sub2 and sub3 are less than 40 then print you are fail due to total % less
# than 40.
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total percentage less than 40")

# It means if the total numbers in sub1, sub2 and sub3 are greater than 40 then print
# congratulations ! you passed the exam.
else:
    print("Congratulations! you passed the exam")
