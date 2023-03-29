# Thong tin chung ve tai khoan
## id, password, status
'''
'''
class Account:
    # def __init__(self, id, password, status=True). Them self cua cac add_info duoi dang None
    def __init__(self, email, password, status=None, type=None):
        pass
    
    # Them cac noi dung: Ten, dia chi, phone. Luu y Address la 1 class, khoi tao bang cach Address(province, district, ward, street="")
    def add_info(self, name, Address, phone):
        pass


# Tai khoan cua nguoi ben nguoi truong
'''
- Log In / Sign Up / Log Out / Reset Password (function)
- Search Book: by Title, Author, Subject (function)
- Read free Book
- View/ Change Profile: Profile, Store
'''
class Guest(Account):
    def __init__(self, email, password, status=None, type=None):
        super().__init__(email, password, status, type)
    
    def info(self)
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
    def __init__(self) -> None:
        super().__init__()
        pass

    ## BOOK
    # add Book. + Add to database
    def add_book(self, Book):
        pass

    # remove Book + Delete in database
    def remove_book(self, Book):
        pass

    # sua noi dung sach. Parameters: id/name/... , nội dung edit + Edit in database
    def edit_book(self, Book, feature, edit):
        pass
    
    ## MEMBER
    # edit member. Parameters: id/name/... , nội dung edit + Edit in database
    def edit_member(self, Member, features, edit):
        pass

    # remove member + Delete in database
    def remove_member(self, Member):
        pass

    # sua noi dung member. Parameters: id/name/... , nội dung edit + Update in database
    def block_member(self, Member):
        pass

    # sua noi dung member. Parameters: id/name/... , nội dung edit + Update in database
    def unblock_member(self, Member):
        pass

# Luu tru thong tin cua cac Account Member
## name, address, email, number phone.
class Person:
    pass
