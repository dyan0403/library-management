# Thong tin chung ve tai khoan
## id, password, status
''''''
class Account:
    # def __init__(self, id, password, status=)
    pass


# Tai khoan cua nguoi ben nguoi truong
'''
- Log In / Sign Up / Log Out / Reset Password (function)
- Search Book: by Title, Author, Subject (function)
- Read free Book
- View/ Change Profile: Profile, Store
'''
class Guest(Account):
    pass


# Tai khoan danh cho sinh vien
'''
- Register: Borrow / Return Book
- Read full Book
'''
class Student(Guest):
    pass

# Tai khoan danh cho giao vien
'''
- Request add Book
- Download pdf file
'''
class Teacher(Account):
    pass

# Tai khoan cua admin
'''
- Edit/ Add/ Remove Book
- Edit/ Block/ Unblock/ Remove Member
'''
class Admin(Account):
    pass

# Luu tru thong tin cua cac Account Member
## name, address, email, number phone
class Person:
    pass