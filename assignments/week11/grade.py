"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)

สร้างระบบการประมวลผลเกรดโดยมีข้อกำหนดดังต่อไปนี้:
ตัวแปรระดับโลก passing_grade = 50
(1) ฟังก์ชัน input_students(num_students) ที่:
- สร้างและส่งกลับรายการของพจนานุกรม
- แต่ละพจนานุกรมประกอบด้วย: {'name': str, 'scores': [รายการของคะแนน 3 ค่า]}
(2) ฟังก์ชัน calculate_averages(students) ที่:
- ใช้ลูปซ้อนเพื่อตรวจสอบค่าเฉลี่ยของนักเรียนแต่ละคน- เพิ่มคีย์ 'average' ลงในพจนานุกรมของนักเรียนแต่ละคน
- แก้ไขรายการเดิม (เพื่อแสดงความสามารถในการเปลี่ยนแปลงของรายการ)
(3) ฟังก์ชัน display_results(students) ที่:
- ลูปผ่านนักเรียน
- ใช้ตัวแปร global passing_grade เพื่อกำหนดผลผ่าน/ไม่ผ่าน
- พิมพ์ชื่อของนักเรียน ค่าเฉลี่ย และสถานะ (PASS/FAIL)
"""
passing_grade = 50

def input_students():
    data_students = [
        {'name': "raphiphat", 'scores': (80, 75, 50)},
        {'name': "sadboy", 'scores': (89, 90, 100)}
    ]
    return data_students

def calculate_averages(students):
    for student in students:
        sum_score = sum(student['scores'])
        student['average'] = sum_score / len(student['scores'])
    return students

def display_results(students):
    print("Student Detail")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Average Score: {student['average']}")
        if student['average'] >= passing_grade:
            print("Status: Pass")
        else:
            print("Status: Fail")

students = input_students()
students = calculate_averages(students)
display_results(students)
