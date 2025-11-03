# Name: Kritarth Jhala
# Title: Gradebook analyzer


#Manually taking student details
def manual_input():
    record={}
    total=int(input("Enter total number of students: "))
    for i in range(total):
        print(f"\n--- Details for Student {i+1} ---")
        name=input("Enter student's name: ")
        marks=int(input("Enter marks obtained: "))
        record[name]=marks
    return record

#Calculating average marks
def get_average(scores):
    sum=0
    count=0
    for i in scores:
        sum+=scores[i]
        count+=1
    average=sum/count
    return average

#Calculating Median marks
def median(scores):
    sorted_scores=sorted(scores.values())
    n=len(sorted_scores)
    mid=n//2
    if n%2==0:
        return(sorted_scores[mid-1] + sorted_scores[mid])/2
    else:
        return sorted_scores[mid]

#Calculating highest score
def highest_score(scores):
    max=0
    for i in scores:
        if scores[i]>max:
            max=scores[i]
    return max

#Calculating lowest score
def lowest_score(scores):
    min=100
    for i in scores:
        if scores[i]<min:
            min=scores[i]
    return min

#Grading students by their result
def grade_assign(scores):
    grade_book={}
    for student, score in scores.items():
        if score>=90:
            grade_book[student] = "A"
        elif score>=80:
            grade_book[student] = "B"
        elif score>=70:
            grade_book[student] = "C"
        elif score>=60:
            grade_book[student] = "D"
        else:
            grade_book[student] = "F"
    return grade_book

#Summarizing grade count
def grade_summary(grade_book):
    summary={'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for g in grade_book.values():
        summary[g]+=1
    return summary

#Pass/Fail list
def result(data):
    for i in data:
        if data[i]>=40:
            print(i,'\tPASSED')
        else:
            print(i,'\tFAILED')
        

data=manual_input()
print("\n========================")
print("STUDENT PERFORMANCE DATA")
print("========================")
for student, score in data.items():
    print(f"{student:<18}: {score}")

avg_marks=get_average(data)
median_marks=median(data)
topper=highest_score(data)
lowest=lowest_score(data)

grades=grade_assign(data)
summary=grade_summary(grades)

print("\n========================")
print(" PERFORMANCE STATISTICS")
print("========================")
print(f"Average Marks  : {avg_marks:.2f}")
print(f"Median Marks   : {median_marks}")
print(f"Highest Marks  : {topper}")
print(f"Lowest Marks   : {lowest}")

print("\n========================")
print(" INDIVIDUAL GRADES")
print("========================")
for student, grade in grades.items():
    print(f"{student:<18}: Grade {grade}")

print("\n========================")
print(" GRADE SUMMARY")
print("========================")
for g, count in summary.items():
    print(f"Grade {g} : {count} student(s)")

print("\n========================")
print("Pass/Fail filter list")
print("========================")
print('NAME\tRESULT')
print('------------------------')
result(data)


print("\n Program Execution finished successfully!")