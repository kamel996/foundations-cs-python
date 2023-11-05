import json

with open('data.json', 'r') as file:
    data = json.load(file)
    
    
    
with open('data2.json', 'r') as file:
    data2 = json.load(file)
        

def callChoices():
    
    print("Choose an option:")
    print("1: Get student by ID")
    print("2: Get all students")
    print("3: Get students by major")
    print("4: Add a new student")
    print("5: Get common majors")
    print("6: Remove student by ID")
    print("7: Get average GPA")
    print("8: Get top-performing students")
    print("9: Quit")
    


def getStudentById(studentsData,id):
    for student in studentsData:
        if student["ID"] == id:
            return student
    return None


def getAllStudents(studentsData):
    
     return studentsData
 
 
def getStudentsByMajor(studentsData, major):
     
     arr = []
     
     for student in studentsData:
          if student["Major"] == major:
              arr.append(student)
              
     return arr
 
 
  
def addNewStudent(studentsData,name,age,major,gpa):
    
    arr = studentsData
     
    newStudent = {
         "Name": name,
         "Age": age,
         "Major": major,
         "GPA": gpa
     }
    
    arr.append(newStudent)
    
    return arr


def getCommonMajors(studentsData1,studentsData2):
    
    set1 = set(student["Major"] for student in studentsData1)
    
    set2 = set(student["Major"] for student in studentsData2)
    
    finalSet = set1.intersection(set2)
    
    return finalSet


def getCommonMajors2(studentsData1,studentsData2):
    
    commonMajors = []
    
    for student1 in studentsData1:
         for student2 in studentsData2:
             if student1["Major"] == student2["Major"]:
               commonMajors.append(student1["Major"])
    
    commonMajorsSet = set(commonMajors)
    
    return commonMajorsSet
    

def removeStudentById(studentsData, id):
    removedDataArr = studentsData1
    for student in removedDataArr:
        if student["ID"] == id:
            removedDataArr.remove(student)
                  
    
    return removedDataArr


def averageGpa(studentsData):
    totalGpa = float(studentsData[0]["GPA"])

    for student in studentsData[1:]:
        totalGpa += student["GPA"]

    gpaAvg = float(totalGpa) / len(studentsData)

    return gpaAvg


def averageGpa2(studentsData):
    totalGpa = float(studentsData[0]["GPA"])

    for student in range(1,len(studentsData)):
        totalGpa += studentsData[student]["GPA"]

    gpaAvg = (totalGpa) / len(studentsData)

    return gpaAvg


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["GPA"] > right[j]["GPA"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
    
    


         
  
def myMiniApp():
       
        callChoices()
        
        choice = int(input("Enter your choice: "))
        
        
        if choice == 1:
         
         studentId = int(input("Enter the student ID: "))
         student = getStudentById(data,studentId)
         if student:
             print(student)
         else:
            print("Student not found.")
            
            
        elif choice == 2:
            
           students = getAllStudents(data)
        
           print(students)    
            
        elif choice == 3:
            
            studentMajor = input("Enter Major")
            
            students = getStudentsByMajor(data, studentMajor)  
            if students:
             print(students)
            else:
             print("No Students found with the selected major")
            
        elif choice == 4:
    
            studentName = input("Enter name")
            studentAge = input("Enter age")
            studentMajor = input("Enter Major")
            studentGpa = input("Enter Gpa")
            
            newStudentsArr = addNewStudent(data, studentName, studentAge, studentMajor, studentGpa)
            
            if newStudentsArr:
                print(newStudentsArr)
            else:
                print("Error adding new student")
                
                
                
        elif choice == 5:
            
             print("Common majors are", getCommonMajors2(data, data2))
             
        elif choice == 6:
                 
             studentId = int(input("Enter ID"))    
    
             print(removeStudentById(data, studentId))
             
        elif choice == 7:
            
             print(averageGpa(data2))   
             
        elif choice == 8:
            
            return     
        
            
            
                
            
                
            




myMiniApp()
