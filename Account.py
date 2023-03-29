# Thong tin chung ve tai khoan
from function import *
from constant import *
## id, password, status
'''
'''
class Account:
    # def __init__(self, id, password, status=True). Them self cua cac add_info duoi dang None
    def __init__(self, email, password, status=None, type=None):
        self.email = email
        self.__password = password
        self.status = status
        self.type = type
        #add_infor
        self.name = None
        self.Address = Address(None, None, None, None)
        self.phone = None
    # Them cac noi dung: Ten, dia chi, phone. Luu y Address la 1 class, khoi tao bang cach Address(province, district, ward, street="")
    def set_info(self, name, Address, phone):
        self.name = name
        self.Address = Address
        self.phone = phone
    ### DO DONE

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
    
    # Log In / Sign Up / Log Out / Reset Password
    def log_in(self):
        return log_in()

    def sign_up(self):
        return sign_up()
    
    def log_out(self):
        return log_out()
    
    def reset_password(self):
        return reset_password()
    
    # SEARCH
    def search_by_title(self):
        return search_by_title()
    
    def search_by_author(self):
        return search_by_authors()
    
    def search_by_subject(self):
        return search_by_subject()
    
    # Read book: Doc mot so cuon sach Free.
    # print("ban da them cuon sach ... vao thu vien. Doc sach tai...")
    def read_book(self):
        pass

    # View/ Change Profile: Profile, Store
    def info(self):
        pass
    
    # show Store. Thong tin cac cuon sach pdf va sach giay muon tu thu vien
    def info_store(self):
        pass

    # edit account. Parameters: id/name/... , nội dung edit + Edit in database
    def edit_info(self, parameter, edit):
        pass


# Tai khoan danh cho sinh vien
'''
- Register: Borrow / Return Book
- Read full Book
'''
class Student(Guest):
    def __init__(self, email, password, status=None, type=None):
        super().__init__(email, password, status, type)
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
## name, address, email, number phone
class Person:
    pass