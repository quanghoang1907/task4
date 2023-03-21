import traceback
from dao.studentInterface import StudentInterface
from db import dbContext
import pandas as pd
from models.student import Student
from utils import constant

class StudentDAO(StudentInterface):
    
    def importData():
        try:
            conn = dbContext.connect()
            cursor = conn.cursor()
            df = pd.read_excel(r'C:\Users\ADMIN\Desktop\PythonBT\input.xlsx', sheet_name='MAU', usecols='A:H', skiprows=10, nrows=52)
            for row in df.iterrows():
                row_data = []
                for value in row[1]:
                    row_data.append(value)
                values = (row_data[0],row_data[1],row_data[2],row_data[3],row_data[4],row_data[5],row_data[6],row_data[7])
                cursor.execute(constant.ADD_SQL, values)
                conn.commit()
            print("importData thanh cong")
        except:
            dbContext.disconnect(conn)
            traceback.print_exc()
            print("importData that bai")
    
    def addStudent(student):
        try:
            conn = dbContext.connect()
            cursor = conn.cursor()
            values = (student.MaSV, student.Ho, student.Ten, student.NgaySinh, student.Toan, student.Ly, student.Hoa)
            cursor.execute(constant.ADD_SQL ,values)
            conn.commit()
            print("addStudent thanh cong")
        except:
            dbContext.disconnect(conn)
            traceback.print_exc()
            print("addStudent that bai")
    
    def updateStudent(student):
        try:
            conn = dbContext.connect()
            cursor = conn.cursor()
            values = (student.MaSV, student.Ho, student.Ten, student.NgaySinh, student.Toan, student.Ly, student.Hoa)
            cursor.execute(constant.UPDATE_SQL, values)
            conn.commit()
            print("updateStudent thanh cong")
        except:
            dbContext.disconnect(conn)
            traceback.print_exc()
            print("updateStudent that bai")
    
    def deleteStudent(student_id):
        try:
            conn = dbContext.connect()
            cursor = conn.cursor()
            values = (student_id,)
            cursor.execute(constant.DELETE_SQL, values)
            conn.commit()
            print("deleteStudent thanh cong")
        except:
            dbContext.disconnect(conn)
            traceback.print_exc()
            print("deleteStudent that bai")
    
    def getStudent(student_id):
        try:
            conn = dbContext.connect()
            cursor = conn.cursor()
            values = (student_id,)
            cursor.execute(constant.GET_STUDENT_SQL, values)
            result = cursor.fetchone()
            if result:
                print(result)
                return Student(*result)
            else:
                return None
        except:
            dbContext.disconnect(conn)
            traceback.print_exc()
    
    def getAll():
        try:
            conn = dbContext.connect()
            cursor = conn.cursor()
            cursor.execute(constant.GET_ALL_SQL)        
            results = cursor.fetchall()
            students = []
            for result in results:
                print(result)
                students.append(Student(*result));
        except:
            dbContext.disconnect(conn)
            traceback.print_exc()
