class student_data:
    def __init__(self,name,roll,age,branch,cgpa,grade):
        self.name=name
        self.roll=roll
        self.age=age
        self.branch=branch
        self.cgpa=cgpa
        self.grade=grade
    def display(name,roll,age,branch,cgpa):
        return f"name :{name},roll:{roll},age={age},branch={branch},cgpa={cgpa}"

    def grade(cgpa):
        if(cgpa>9.5):
            return "excellent"
        elif (cgpa>7 and cgpa<9):
            return "good"
        elif (cgpa>6 and cgpa<7):
            return "avg"
    def check_placements(marks_10th,marks_diploms,marks_btech):
        if(marks>60):
            return eligible
        obj =student_data
student_1 = student_data
student_2= student_data
#print(student_1.display("subhan",431,21,"ece",7.0))
#print(student_data.grade(88))
print(student_2.check_placements(10,80,90))
