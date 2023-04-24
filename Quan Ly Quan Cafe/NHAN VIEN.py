import datetime
class NhanVien:
    def __init__(self,MANV,HoTen,NGVL,SODT,Luong):
        self.MSNV=MSNV
        self.HoTen=HoTen
        self.Tuoi=Tuoi
        self.NgayVaoLam
        self.Luong=Luong

    def NhapThongTin(self):
        self.MANV=input("Nhập vào mã số nhân viên mới: ")
        self.HoTen=input("Nhập vào họ và tên nhân viên: ")
        self.NGVL=int(input("Nhap ngay vao lam: "))
        self.SDT=input("Nhập vào SDT: ")
        self.Luong=input("Mức lương hiện tại: ")

    def UpDateInfo(self):
        var1=int(input("Chọn mục bạn muốn update"
                       "(1): MANV"
                       "(2): HoTen"
                       "(3): NGVL"
                       "(4): SODT"
                       "(5): Luong"))
        if(var1==1):
            self.MANV=input("Nhap vao ma so nhan vien moi: ")
        if(var1==2):
            self.HoTen=input("Nhap vao ho va ten moi: ")
        if(var1==3):
            self.NGVL=input("Nhap vao ngay vao lam: ")
        if(var1==4):
            self.SDT=input("Nhap vao so dien thoi: ")
        if(var1==5):
            self.Luong=input("Nhap luong moi ")
    def getMANV(self):
        return self.MANV
    def getHoTen(self):
        return self.HoTen
    def getNGVL(self):
        return self.NGVL
    def getSDT(self):
        return self.SDT
    def getLuong(self):
        return self.Luong


