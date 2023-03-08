# Thong tin chung ve tai khoan
## id, password, status
class Account:
    # def __init__(self, id, password, status=)
    pass

# Tai khoan cua nguoi ben nguoi truong
# Quyen loi: Doc mot so cuon sach Free, khong muon duoc sach
class Guest(Account):
    pass

# Tai khoan danh cho sinh vien
# Quyen loi: Doc tat ca cac cuon sach, duoc muon toi da 5 cuon sach trong 1 thoi diem
class Student(Guest):
    pass

# Tai khoan danh cho giao vien
# Quyen loi: Duoc muon so sack khong gioi han, yeu cau mua, cap nhat them sach
class Teacher(Account):
    pass

# Tai khoan cua admin
class Admin(Account):
    pass

# Luu tru thong tin cua cac Account Member
## name, address, email, number phone
class Person:
    pass