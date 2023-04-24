class SANPHAM:
    def __inint__(self,MASP,TENSP,DVT,NUOCSX,GIA):
        self.MASP=MASP
        self.TENSP=TENSP
        self.DVT=DVT
        self.NUOCSX=NUOCSX
        self.GIA=GIA

    def NhapThongTin(self):
        self.MASP=input("Nhap ma san pham: ")
        self.TENSO=input("Nhap vao ten san pham: ")
        self.DVT=input("Nhap vao don vi tinh: ")
        self.NUOCSX=input("Nhap vao nuoc san xuat: ")
        self.GIA=input("Nhap vao don gia san pham: ")
    def UpDateInfo(self):
        var1 = int(input("Chọn mục bạn muốn update"
                         "(1): MASP"
                         "(2): TENSP"
                         "(3): DVT"
                         "(4): NUOCSX"
                         "(5): GIA"))
        if (var1 == 1):
            self.MASP = input("Nhap vao ma san pham moi: ")
        if (var1 == 2):
            self.TENSP = input("Nhap vao ten san pham moi: ")
        if (var1 == 3):
            self.DVT = input("Nhap vao ngay don vi tinh moi: ")
        if (var1 == 4):
            self.NUOCSX = input("Nhap vao nuoc san xuat: ")
        if (var1 == 5):
            self.GIA = input("Nhap gia: ")
    def getMASP(self):
        return self.MASP
    def getTENSP(self):
        return self.TENSP
    def getDVT(self):
        return self.DVT
    def getNUOCSX(self):
        return self.NUOCSX
    def getGIA(self):
        return self.GIA