class KHACHHANG:
    def __init__(self,MAKH,HOTEN,DCHI,SODT,NGSINH,DOANHSO,NGDK):
        self.MAKH=MAKH
        self.HOTEN=HOTEN
        self.DCHI=DCHI
        self.SODT=SODT
        self.NGSINH=NGSINH
        self.DOANHSO=DOANHSO
        self.NGDK=NGDK

    def NhapThongTin(self):
        self.MAKH=input("Nhap vao MAKH: ")
        self.HOTEN=input("Nhap vao Ho ten khach hang: ")
        self.DCHI=input("Nhap vao dia chi khach hang: ")
        self.SODT=input("Nhap vao so dien thoai khach hang: ")
        self.NGSINH=input("Nhap vao ngay thang nam sinh khach hang")
        self.NGDK=input("Nhap vao NGDK: ")

    def UpDateInfo(self):
        var1=int(input("Chọn mục bạn muốn update"
                       "(1): MAKH"
                       "(2): HOTEN"
                       "(3): DCHI"
                       "(4): SODT"
                       "(5): NGSINH"
                       "(6)DOANHSO"
                       "(7)NGDK"))
        if(var1==1):
            self.MAKH=input("Nhap vao ma so khach hang: ")
        if(var1==2):
            self.HoTen=input("Nhap vao ho va ten moi: ")
        if(var1==3):
            self.DIACHI=input("Nhap vao dia chi khach hang: ")
        if(var1==4):
            self.SDT=input("Nhap vao so dien thoi: ")
        if(var1==5):
            self.NGSINH=input("Nhap vao ngay sinh khach hang: ")
        if(var1==6):
            self.DOANHSO=input("Nhap vao doanh so khach hang: ")
        if(var1==7):
            self.NGDK=input("Nhap vao ngay dang ki cua khach hang: ")
    def getMAKH(self):
        return self.MAKH
    def getHoTen(self):
        return self.HOTEN
    def getDCHI(self):
        return self.DCHI
    def getSDT(self):
        return self.SDT
    def getNGSINH(self):
        return self.NGSINH
    def getDOANHSO(self):
        return self.DOANHSO
    def getNGDK(self):
        return self.NGDK

