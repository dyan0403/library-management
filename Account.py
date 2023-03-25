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
  def __init__(self, email, ID, password, status=None, account_type="student"):
    super().__init__(email, password, status, account_type)
    self.ID = ID
    self.archives = {}

  def view_info(self):
    print(f"Name: {self.email}")
    print("Password: " + "*" * len(self.password))
    print(f"Status: {self.status}")
    print(f"Type: {self.account_type}")
    print(f"Archives: {self.archives}")

  def borrow_book(self, book: Book):
    if self.account_type not in ["student", "teacher"]:
      print('Bạn không đủ level mượn sách')
    elif self.status == "block":
      print(f"Tài khoản {self.email} của bạn đã bị chặn quyền mượn sách.")
    elif self.status == "cancel":
      print("Tài khoản của bạn đã bị xóa.")
    elif len(self.archives) >= 5:
      print("Bạn đã mượn tối đa số lượng sách có thể mượn.")
    elif book.number_of_book <= 0:
      print("Sách đã hết, vui lòng chọn sách khác.")
    else:
      print("Bạn có thể đọc quyển sách này bây giờ.")
      choice = input("Bạn muốn mượn quyển sách này chứ ? (y/n) ")
      if choice.lower() == "y" and book not in self.archives:
          ngay_muon = date.today()
          self.archives[book] = ngay_muon
          book.number_of_book -= 1
          print("Đã thêm sách thành công, bạn có thể đến thư viện mượn sách")
      else:
        print("Đã hủy thao tác")
    
  def return_book(self, book: Book):
    if self.account_type not in ["student", "teacher"]:
      print("Bạn không thể thực hiện chức năng này")
    elif book not in self.archives:
      print("Không tìm thấy thông tin sách muốn trả")
    else:
      ngay_tra = date.today()
      thoi_diem_tra = datetime.combine(ngay_tra, datetime.time.min)
      ngay_muon = self.archives[book]
      tinh_trang = "đúng hạn" if thoi_diem_tra <= ngay_muon + timedelta(days=30) else "quá hạn"
      print(f"Bạn đã trả sách {tinh_trang}")
      del self.archives[book]
      book.number_of_book += 1


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
