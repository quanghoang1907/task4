from models.person import Person

class Student(Person):
    def __init__(self, MaSv, Ho, Ten, NgaySinh, Toan, Ly, Hoa):
        super().__init__(MaSv, Ho, Ten, NgaySinh)
        self.Toan = Toan
        self.Ly = Ly
        self.Hoa = Hoa
        