# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Oyun():
    def __init__(self):
        self.tahta=[["()","()","()"],["()","()","()"],["()","()","()"]]
        self.durum=True
        self.hamle=0

    def oyna(self):
        if self.hamle%2==0:
            self.p1secim()
        else:
            self.p2secim()

        self.durum=self.oyun_kontrol()

        if self.durum==False:
            self.tahta_goster()
            kazanan=""
            if self.hamle%2==0:
                kazanan="X"
            else:
                kazanan="O"
            print("Kazanan oyuncu {}".format(kazanan))
        self.hamle += 1


    def p1secim(self):
        self.tahta_goster()
        print("Birinci Oyuncu")
        satir=int(input("1-3 arsında satır değeri girniz:"))
        while satir<1 or satir>3:
            satir=int(input("1-3 arasında sayı giriniz:"))
        sutun=int(input("1-3 arasında sütun değeri giriniz:"))
        while sutun<1 or sutun>3:
            sutun = int(input("1-3 arasında sayı değeri giriniz:"))

        if self.dolu_mu(satir,sutun):
            self.p1secim()
        else:
            self.tahta[satir-1][sutun-1]="X"



    def p2secim(self):
        self.tahta_goster()
        print("İkinci Oyuncu")
        satir = int(input("1-3 arsında satır değeri girniz:"))
        while satir < 1 or satir > 3:
            satir = int(input("1-3 arasında sayı giriniz:"))
        sutun = int(input("1-3 arasında sütun değeri giriniz:"))
        while sutun < 1 or sutun > 3:
            sutun = int(input("1-3 arasında sayı değeri giriniz:"))

        if self.dolu_mu(satir, sutun):
            self.p2secim()
        else:
            self.tahta[satir - 1][sutun - 1] = "O"
    def dolu_mu(self,satir,sutun):
        if self.tahta[satir-1][sutun-1]!="()":
            return True
        else:
            return False


    def tahta_goster(self):
        for i in self.tahta:
            print(i)

    def oyun_kontrol(self):
        if [self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]]==["X","X","X"] or [self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]]==["O","O","O"]:
            return False
        if [self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]]==["X","X","X"] or [self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]]==["O","O","O"]:
            return False
        if [self.tahta[2][0], self.tahta[2][1], self.tahta[2][2]] == ["X", "X", "X"] or [self.tahta[2][0],self.tahta[2][1],self.tahta[2][2]] == ["O", "O","O"]:
            return False

        if [self.tahta[0][0], self.tahta[1][0], self.tahta[2][0]] == ["X", "X", "X"] or [self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]] == ["O", "O","O"]:
            return False
        if [self.tahta[0][1], self.tahta[1][1], self.tahta[2][1]] == ["X", "X", "X"] or [self.tahta[0][1],self.tahta[1][1],self.tahta[2][1]] == ["O", "O","O"]:
            return False
        if [self.tahta[0][2], self.tahta[1][2], self.tahta[2][2]] == ["X", "X", "X"] or [self.tahta[0][2],self.tahta[1][2],self.tahta[2][2]] == ["O", "O","O"]:
            return False

        if [self.tahta[0][0], self.tahta[1][1], self.tahta[2][2]] == ["X", "X", "X"] or [self.tahta[0][0],self.tahta[1][1],self.tahta[2][2]] == ["O", "O","O"]:
            return False
        if [self.tahta[0][2], self.tahta[1][1], self.tahta[2][0]] == ["X", "X", "X"] or [self.tahta[0][2],self.tahta[1][1],self.tahta[2][0]] == ["O", "O","O"]:
            return False

        return True
oyun=Oyun()
while oyun.durum:
    oyun.oyna()



