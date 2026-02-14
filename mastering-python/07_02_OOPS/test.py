class UltimateDataScienceBatch:
    def __init__(self, batch_id):
        self.batch_id = batch_id
        self.students = []
        print("Initialised: ", batch_id)
    
    def add_student(self, name, email):
        self.students.append({
            "name": name,
            "email": email
        })
        print(f"Added {name} to {self.batch_id}")
    
    def print_student_names(self):
        print(f"Student list for {self.batch_id}")
        for student in self.students: 
            print(f"- {student["name"]}")
        

batch1 = UltimateDataScienceBatch("Batch 1.0")
batch2 = UltimateDataScienceBatch("Batch 2.0")

batch1.add_student("adarsh", "adarsh@gmail.com")
batch1.add_student("krish", "krish@gmail.com")

batch2.add_student("ziad", "ziad@gmail.com")

batch1.print_student_names()
batch2.print_student_names()