import sys
import mysql.connector
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QTableWidgetItem
import pyqtdesign

class Connectdb(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
    def create_db(self):
        try:
            self.mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="root"
            )
            mycursor=self.mydb.cursor()
            mycursor.execute("""CREATE DATABASE IF NOT EXISTS texnomarketdb;""")
            mycursor.execute("""USE texnomarketdb;""")
            mycursor.close()
        except Exception as err: print(err)
        else: print('create db successfull')
        # Izoh: Bu funksiya market malumotlarini saqlash uchun texnomarketdb nomli malumotlar bazasini yaratadi va uni ishga tushuradi

    def adminTable(self):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute("""CREATE TABLE IF NOT EXISTS adminTable(
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    login VARCHAR(128) NOT NULL,
                    password VARCHAR(128) NOT NULL
                    );""")
        except Exception as err: print(err)
        else: print("create table successful")
        # Izoh Bu funksiya yaratilgan malumotlar bazasi ichida adminlar uchun adminTable nomli jadval yaratadi u yurda marketga kirish kodlari saqlanadi
    
    def CreateProductPhone(self):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute("""CREATE TABLE IF NOT EXISTS phones(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    brand VARCHAR(128) NOT NULL,
                    name VARCHAR(128) NOT NULL,
                    color VARCHAR(128) NOT NULL,
                    memory INT NOT NULL,  
                    ram INT NOT NULL,
                    camera INT NOT NULL,
                    price FLOAT NOT NULL
                    );""")
        except Exception as err: print(err)
        else: print('phone ok')
        # Izoh Bu funksiya malumotlar bazasida telefonlar haqidagi malumotlarni saqlash uchun phones nomli jadval yaratadi u yerda telefonlar haqidagi malumotlar uning xarakteristikalari saqlanadi 
        
    def CreateProductLaptop(self):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute("""CREATE TABLE IF NOT EXISTS laptops(
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    brand VARCHAR(128) NOT NULL,
                    name VARCHAR(128) NOT NULL,
                    color VARCHAR(128) NOT NULL,
                    memory INT NOT NULL,  
                    ram INT NOT NULL,
                    videocard VARCHAR(128) NOT NULL,
                    prossessor VARCHAR(128) Not Null,
                    price FLOAT NOT NULL
                    );""")
        except Exception as err: print(err)
        else: print("laptop ok")
        # Izoh Bu funksiya malumotlar bazasida kompyuterlar haqidagi malumotlarni saqlash uchun laptops nomli jadval yaratadi u yerda kompyuterlar haqidagi malumotlar uning xarakteristikalari saqlanadi
        
    def CreateProductSmartWatch(self):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute("""CREATE TABLE IF NOT EXISTS smartwatchs(
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    brand VARCHAR(128) NOT NULL,
                    name VARCHAR(128) NOT NULL,
                    color VARCHAR(128) NOT NULL,
                    memory INT NOT NULL,
                    battary VARCHAR(128) NOT NULL,  
                    price FLOAT NOT NULL
                    );""")
        except Exception as err: print(err)
        else: print("SmartW ok")
        # Izoh Bu funksiya malumotlar bazasida aqllisoatlar haqidagi malumotlarni saqlash uchun smartwatchs nomli jadval yaratadi u yerda aqllisoatlar haqidagi malumotlar uning xarakteristikalari saqlanadi
        
    def CreateUsersData(self):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    
                );""")
        except Exception as err: print(err)
        else:
            print("users ok")
        
    def SetLoginPassword(self,login, password, newlogin, newpassword):
        temp=self.GetLoginPassword()
        if not (login==temp[0][0] and password==temp[0][1] and newlogin!=newpassword and len(newlogin)>7 and len(newpassword)>7): return False
                
        try:
            with self.mydb.cursor() as cursor: 
                cursor.execute(f"""INSERT INTO adminTable(login,password)
                               VALUES('{newlogin}','{newpassword}')""")
                cursor.execute("")
        except: return False
        else:
            self.mydb.commit()
            return True
        # Izoh BU funksiya admin menu ga kirish parolini o'zgartirish uchun xizmat qiladi
       
    def GetLoginPassword(self):
        result=[]
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute("SELECT login,password FROM adminTable WHERE id=(SELECT MAX(id) FROM adminTable)")
                result=cursor.fetchall()
        except Exception as err: print(err)
        else: print("DaTa GiVe")
        return result
        # Izoh Bu funksiya admin menu siga kirish parolini SetLoginPassword nomli funksiyaga jo'natadi

class KirishPage(Connectdb):
    def __init__(self) -> None:
        super().__init__()
        self.create_db()
        self.adminTable()
        if self.GetLoginPassword()==[]:
            try:
                with self.mydb.cursor() as cursor:
                    cursor.execute("""INSERT INTO adminTable(login,password)
                                   VALUES('11111111','99999999')""")
            except Exception as err: print(err)
            else:
                self.mydb.commit() 
                print("Locked")
            # Izoh bu yerda agar admin menu da parol mavjud bolmasa avtomatik tarzda unga 11111111, 99999999 login paroli o'rnatiladi
            
        self.setMinimumHeight(400)
        self.setMinimumWidth(400)
        self.Ledit1=QLineEdit(self)
        self.Ledit2=QLineEdit(self)
        self.v_box=QVBoxLayout()
        self.kirish_btn=QPushButton('Enter')
        self.label=QLabel('                       Manage of TecnoMarket database')
        self.label.setFixedHeight(50)
        self.checklabel=QLabel()
        self.kirish_btn.setFixedHeight            
        self.kirish_btn.setFixedHeight(50)
        self.checklabel.setFixedHeight(50)
        
        self.Ledit1.setFixedHeight(50)
        self.Ledit1.setPlaceholderText('Login...')
        self.Ledit2.setPlaceholderText('Password...')
        self.Ledit2.setFixedHeight(50)
        
        self.v_box.addWidget(self.label)
        self.v_box.addWidget(self.Ledit1)
        self.v_box.addWidget(self.Ledit2)
        self.v_box.addWidget(self.kirish_btn)
        self.v_box.addWidget(self.checklabel)
        self.setLayout(self.v_box)
        
        self.kirish_btn.clicked.connect(self.kirish)
        
        self.show()
        
        # Izoh yuqoridagi qismda tugmalar, label, parol kiritish uchun linedit lar yartilgan va funksiyalarga bog'langan
        
    def kirish(self):
        temp=self.GetLoginPassword()
        if self.Ledit1.text() == temp[0][0] and self.Ledit2.text() == temp[0][1]:
            self.close()
            self.open=MenuPage()
            self.Ledit1.setText('')
            self.Ledit2.setText('')
            self.checklabel.setText('')
            self.open.show()
        else:
            self.Ledit1.setText('')
            self.Ledit2.setText('')
            self.checklabel.setText("wrong is password or login !")
        # Izoh bu yerda admin menu ga kirish uchun kiritilgan login va parollar tekshiriladi agar ular mos kelsa MenuPage class ishga tushadi va keyingi sahifa ochiladi
            
class MenuPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setMinimumHeight(400)
        self.setMinimumWidth(400)
        
        self.addproductbtn=QPushButton('Add Product')
        self.delproductbtn=QPushButton("Del Product")
        self.showproductbtn=QPushButton("Show Product")
        self.showusers=QPushButton("Show Users")
        self.backk=QPushButton("back")
        self.exit=QPushButton("left")
        self.newlogin=QPushButton("change password")
        self.label=QLabel('                              TexnoMarket create menu')
        self.v_box=QVBoxLayout()
        self.h_box=QHBoxLayout()
        self.lis=[self.label, self.newlogin, self.addproductbtn, self.delproductbtn, self.showproductbtn, self.showusers, self.exit, self.backk]

        for i in range(8):
            if i<6: self.v_box.addWidget(self.lis[i])
            else: self.h_box.addWidget(self.lis[i])
            if i!=0:
                self.lis[i].clicked.connect(self.eventclick)
        self.v_box.addLayout(self.h_box)
        self.setLayout(self.v_box)
        self.setteelshett(self.lis)
        
        # Izoh yuqorida MenuPage ning tugmalari, labellari, lineditlari yaratilgan va ular joylashishi keltirilib funksiyalarga ulangan
        
    def setteelshett(self, temp):
        for i in temp:
            i.setFixedHeight(50)
        # Izoh bu funksiya Button(tugmalar razmerini belgilaydi)
        
    def eventclick(self):
        if self.sender().text()=="change password":
            self.close()
            self.open=NewLoginPage()
            self.open.show()
        elif self.sender().text()=="Add Product":
            self.close()
            self.open=AddDelProduct(1)
            self.open.show()
        elif self.sender().text()=="Del Product":
            self.close()
            self.open=AddDelProduct(0)
            self.open.show()
        elif self.sender().text()=="Show Product":
            self.close()
            self.open=ShowProduct()
            self.open.show()
        elif self.sender().text()=="Show Users":
            pass
        
        elif self.sender().text()=="left":
            self.close()
        else:
            self.close()
            self.open=KirishPage()
            self.open.show()
        # Izoh Bu funksiya tugmalar bosilganda ularga mos keladigan class lar ishga tushiriladi va keyingi sahifani ochib beradi
            
                   
class NewLoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setMinimumHeight(400)
        self.setMinimumWidth(400)
        self.setFixedWidth(400)
        self.login=QLineEdit(self)
        self.password=QLineEdit(self)
        self.login.setPlaceholderText('Login...')
        self.password.setPlaceholderText('Password...')
        self.newlogin=QLineEdit(self)
        self.newpassword=QLineEdit(self)
        self.newlogin.setPlaceholderText('NewLogin...')
        self.newpassword.setPlaceholderText('NewPassword...')
        self.back_btn=QPushButton('back')
        self.chiqish_btn=QPushButton('left')
        self.tasdiqlash=QPushButton('Change')
        self.label=QLabel("                                      change password")
        self.checklabel=QLabel()
        self.h_box=QHBoxLayout()
        self.v_box=QVBoxLayout()
        self.lis=[self.label, self.login, self.password, self.newlogin, self.newpassword, self.tasdiqlash, self.chiqish_btn, self.back_btn]
        
        for i in range(8):
            if i<6: self.v_box.addWidget(self.lis[i])
            else: self.h_box.addWidget(self.lis[i])
            if 4<i: self.lis[i].clicked.connect(self.eventbtn)
        self.setteelshett(self.lis)
    
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.checklabel)
        self.setLayout(self.v_box)
        # Izoh yuqorida NewLoginPage ning tugmalari, labellari, lineditlari yaratilgan va ular joylashishi keltirilib funksiyalarga ulangan
        
    def eventbtn(self):
        if self.sender().text()=="back":
            self.close()
            self.open=MenuPage()
            self.checklabel.setText('')
            for i in self.lis[1:5]:
                i.clear()
            self.open.show()
        elif self.sender().text()=="left":
            self.close()
        else:
            temp=KirishPage()
            if temp.SetLoginPassword(self.login.text(), self.password.text(), self.newlogin.text(),  self.newpassword.text()):
                self.checklabel.setText("successfull change")
                for i in self.lis[1:5]:
                    i.clear()
            else:
                self.checklabel.setText("wrong is password or login !")
                for i in self.lis[1:5]:
                    i.clear()
        # Izoh bu funksiya admin menu sidagi login va parolni o'zgartirish uchun ishlaydi    
            
    def setteelshett(self, temp):
        for i in temp:
            i.setFixedHeight(50)


class AddDelProduct(Connectdb):
    def __init__(self, check) -> None:
        super().__init__()
        self.check=check
        
        if self.check:
            temp="                                           Add Product"
        else:
            temp="                                      Del Product"    
                                
        self.phone=QPushButton("Phone")
        self.laptop=QPushButton("Laptop")
        self.smartW=QPushButton("SmartWatch")
        self.back=QPushButton("back")
        self.left=QPushButton("left")
        self.label=QLabel(temp)
        self.v_box=QVBoxLayout()
        self.h_box=QHBoxLayout()
        self.lis=[self.label, self.phone, self.laptop, self.smartW, self.left, self.back]
        self.setMinimumWidth(400)
        
        self.setteelshett(self.lis)
        for i in range(6):
            if i<4: self.v_box.addWidget(self.lis[i])
            else: self.h_box.addWidget(self.lis[i])
            if i!=0:
                self.lis[i].clicked.connect(self.eventclick)
        self.v_box.addLayout(self.h_box)
        self.setLayout(self.v_box)
        # Izoh yuqorida AddDelProduct ning tugmalari, labellari, lineditlari yaratilgan va ular joylashishi keltirilib funksiyalarga ulangan
        
        
    def eventclick(self):
        if self.sender().text()=="Phone":
            self.close()
            if self.check:
                self.open=AddPhone()
            else:
                self.open=delProduct(1)
            self.open.show()
        elif self.sender().text()=="Laptop":
            self.close()
            if self.check:
                self.open=AddLaptop()
            else:
                self.open=delProduct(2)
            self.open.show()
        elif self.sender().text()=="SmartWatch":
            self.close()
            if self.check:
                self.open=AddSmartWatch()
            else:
                self.open=delProduct(3)
            self.open.show()
        elif self.sender().text()=="back":
            self.close()
            self.open=MenuPage()
            self.open.show()
        else:
            self.close()
        # Izoh Bu funksiya telefonni, kompyuter yoki aqqllisoatlarni biri tanlansa ularni o'chirish uchun sahifa ochib berish uchun hizmat qiladi
            
    def setteelshett(self, temp):
        for i in temp:
            i.setFixedHeight(50)
        

class AddPhone(Connectdb):
    def __init__(self) -> None:
        super().__init__()
        self.create_db()
        self.CreateProductPhone()
        self.setMinimumWidth(400)
        self.ledit1=QLineEdit()
        self.ledit2=QLineEdit()
        self.ledit3=QLineEdit()
        self.ledit4=QLineEdit()
        self.ledit5=QLineEdit()
        self.ledit6=QLineEdit()
        self.ledit7=QLineEdit()
        self.addbtn=QPushButton("Add")
        self.back=QPushButton('back')
        self.exit=QPushButton('left')
        self.v_box=QVBoxLayout()
        self.h_box=QHBoxLayout()
        self.note=QLabel("                                         Add Phone")
        self.ledit1.setPlaceholderText("brand...")
        self.ledit2.setPlaceholderText("name...")
        self.ledit3.setPlaceholderText("price...")
        self.ledit4.setPlaceholderText("color...")
        self.ledit5.setPlaceholderText("memory...")
        self.ledit6.setPlaceholderText("ram...")
        self.ledit7.setPlaceholderText("camere...")
        self.checklabel=QLabel()
        self.checklabel.setFixedHeight(50)
        
        self.lis=[self.note, self.ledit1, self.ledit2, self.ledit3, self.ledit5, self.ledit6, self.ledit7, self.ledit4, self.addbtn, self.exit, self.back]
        self.setteelshett(self.lis)
        for i in range(11):
            if i<9: self.v_box.addWidget(self.lis[i])
            else: self.h_box.addWidget(self.lis[i])
            if i>7: self.lis[i].clicked.connect(self.eventbtn)
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.checklabel)
        
        self.setLayout(self.v_box)
        # Izoh yuqorida AddPhone ning tugmalari, labellari, lineditlari yaratilgan va ular joylashishi keltirilib funksiyalarga ulangan
            
        
    def setteelshett(self, temp):
        for i in temp:
            i.setFixedHeight(50)    
            
    def eventbtn(self):
        if self.sender().text()=="Add":
            if len(self.ledit1.text())>0 and len(self.ledit2.text())>0 and len(self.ledit3.text())>0 and len(self.ledit4.text())>0 and len(self.ledit5.text())>0 and len(self.ledit6.text())>0 and len(self.ledit7.text())>0 and self.ledit3.text().isnumeric() and self.ledit5.text().isnumeric() and self.ledit6.text().isnumeric() and self.ledit7.text().isnumeric():
                try: 
                    with self.mydb.cursor() as cursor:
                        cursor.execute(f"INSERT INTO phones(brand, name, color, memory, ram, camera, price) values('{self.ledit1.text()}', '{self.ledit2.text()}', '{self.ledit4.text()}', '{self.ledit5.text()}', '{self.ledit6.text()}', '{self.ledit7.text()}', '{self.ledit3.text()}');")
                except Exception as err: print(err)
                else: 
                    self.mydb.commit()
                    print("add phone ok")
                    self.checklabel.setText('')
                finally:
                    self.ledit1.setText('') 
                    self.ledit2.setText('') 
                    self.ledit4.setText('') 
                    self.ledit5.setText('') 
                    self.ledit6.setText('') 
                    self.ledit7.setText('') 
                    self.ledit3.setText('') 
            else:
                self.checklabel.setText("wrong entered!")
                self.ledit1.setText('') 
                self.ledit2.setText('') 
                self.ledit4.setText('') 
                self.ledit5.setText('') 
                self.ledit6.setText('') 
                self.ledit7.setText('') 
                self.ledit3.setText('')
            # Izoh bu shart da marketga telefon qo'shish uchun hizmat qiladi kirtilgan malumotlar to'liqligi tekshiriladi to'liq bo'lsa u malumotlar malumotlar bazasidagi phones nomli jadval ga yoziladi
                
        elif self.sender().text()=="back":
            self.checklabel.setText('')
            self.close()
            self.open=AddDelProduct(1)
            self.open.show()
            # Izoh bu shartda joriy sahifadan orqaga qaytish uchun ishlatiladi
        else:
            self.close()
            # Izoh bu shart menu ni butunlay tark etishni bajaradi
            
        
class AddLaptop(Connectdb):
    def __init__(self) -> None:
        super().__init__()
        self.create_db()
        self.CreateProductLaptop()
        self.setMinimumWidth(400)
        self.ledit1=QLineEdit()
        self.ledit2=QLineEdit()
        self.ledit3=QLineEdit()
        self.ledit4=QLineEdit()
        self.ledit5=QLineEdit()
        self.ledit6=QLineEdit()
        self.ledit7=QLineEdit()
        self.ledit8=QLineEdit()
        self.addbtn=QPushButton("Add")
        self.back=QPushButton('back')
        self.exit=QPushButton('left')
        self.v_box=QVBoxLayout()
        self.h_box=QHBoxLayout()
        self.note=QLabel("                                         Add laptop")
        self.ledit1.setPlaceholderText("brand...")
        self.ledit2.setPlaceholderText("name...")
        self.ledit3.setPlaceholderText("price...")
        self.ledit4.setPlaceholderText("color...")
        self.ledit5.setPlaceholderText("memory...")
        self.ledit6.setPlaceholderText("ram...")
        self.ledit7.setPlaceholderText("videocard...")
        self.ledit8.setPlaceholderText("prossessor...")
        self.checklabel=QLabel()
        self.checklabel.setFixedHeight(50)
        
        self.lis=[self.note, self.ledit1, self.ledit2, self.ledit3, self.ledit5, self.ledit6, self.ledit4, self.ledit7, self.ledit8, self.addbtn, self.exit, self.back]
        self.setteelshett(self.lis)
        for i in range(12):
            if i<10: self.v_box.addWidget(self.lis[i])
            else: self.h_box.addWidget(self.lis[i])
            if i>8: self.lis[i].clicked.connect(self.eventbtn)
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.checklabel)
        
        self.setLayout(self.v_box)   
        
        # Izoh yuqorida AddLaptop ning tugmalari, labellari, lineditlari yaratilgan va ular joylashishi keltirilib funksiyalarga ulangan
         
        
    def setteelshett(self, temp):
        for i in temp:
            i.setFixedHeight(50)    
            
    def eventbtn(self):
        if self.sender().text()=="Add":
            if len(self.ledit1.text())>0 and len(self.ledit2.text())>0 and len(self.ledit3.text())>0 and len(self.ledit4.text())>0 and len(self.ledit5.text())>0 and len(self.ledit6.text())>0 and len(self.ledit7.text())>0 and self.ledit3.text().isnumeric() and self.ledit5.text().isnumeric() and self.ledit6.text().isnumeric() and len(self.ledit8.text())>0:
                try: 
                    with self.mydb.cursor() as cursor:
                        cursor.execute(f"INSERT INTO laptops(brand, name, color, memory, ram, videocard, prossessor, price) values('{self.ledit1.text()}', '{self.ledit2.text()}', '{self.ledit4.text()}', '{self.ledit5.text()}', '{self.ledit6.text()}', '{self.ledit7.text()}', '{self.ledit8.text()}', '{self.ledit3.text()}');")
                except Exception as err: print(err)
                else: 
                    self.mydb.commit()
                    print("add laptop ok")
                    self.checklabel.setText('')
                finally:
                    self.ledit1.setText('') 
                    self.ledit2.setText('') 
                    self.ledit4.setText('') 
                    self.ledit5.setText('') 
                    self.ledit6.setText('') 
                    self.ledit7.setText('') 
                    self.ledit3.setText('') 
                    self.ledit8.setText('') 
            else:
                self.checklabel.setText("wrong entered!")
                self.ledit1.setText('') 
                self.ledit2.setText('') 
                self.ledit4.setText('') 
                self.ledit5.setText('') 
                self.ledit6.setText('') 
                self.ledit7.setText('') 
                self.ledit3.setText('')
                self.ledit8.setText('')
            # Izoh bu shart da marketga kompyuter qo'shish uchun hizmat qiladi kirtilgan malumotlar to'liqligi tekshiriladi to'liq bo'lsa u malumotlar malumotlar bazasidagi laptops nomli jadval ga yoziladi
                
        elif self.sender().text()=="back":
            self.checklabel.setText('')
            self.close()
            self.open=AddDelProduct(1)
            self.open.show()
            # Izoh bu shartda joriy sahifadan orqaga qaytish uchun ishlatiladi
        else:
            self.close()
            # Izoh bu shart menu ni butunlay tark etishni bajaradi
        
class AddSmartWatch(Connectdb):
    def __init__(self) -> None:
        super().__init__()
        self.create_db()
        self.CreateProductSmartWatch()
        self.setMinimumWidth(400)
        self.ledit1=QLineEdit()
        self.ledit2=QLineEdit()
        self.ledit3=QLineEdit()
        self.ledit4=QLineEdit()
        self.ledit5=QLineEdit()
        self.ledit6=QLineEdit()
        self.addbtn=QPushButton("Add")
        self.back=QPushButton('back')
        self.exit=QPushButton('left')
        self.v_box=QVBoxLayout()
        self.h_box=QHBoxLayout()
        self.note=QLabel("                                         Add laptop")
        self.ledit1.setPlaceholderText("brand...")
        self.ledit2.setPlaceholderText("name...")
        self.ledit3.setPlaceholderText("price...")
        self.ledit4.setPlaceholderText("color...")
        self.ledit5.setPlaceholderText("memory...")
        self.ledit6.setPlaceholderText("battary...")
        self.checklabel=QLabel()
        self.checklabel.setFixedHeight(50)
        
        self.lis=[self.note, self.ledit1, self.ledit2, self.ledit3, self.ledit5, self.ledit6, self.ledit4, self.addbtn, self.exit, self.back]
        self.setteelshett(self.lis)
        for i in range(10):
            if i<8: self.v_box.addWidget(self.lis[i])
            else: self.h_box.addWidget(self.lis[i])
            if i>6: self.lis[i].clicked.connect(self.eventbtn)
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.checklabel)
        
        self.setLayout(self.v_box)  
        # Izoh yuqorida AddSmartWatch ning tugmalari, labellari, lineditlari yaratilgan va ular joylashishi keltirilib funksiyalarga ulangan  
        
    def setteelshett(self, temp):
        for i in temp:
            i.setFixedHeight(50)        
        
    def eventbtn(self):
        if self.sender().text()=="Add":
            if len(self.ledit1.text())>0 and len(self.ledit2.text())>0 and len(self.ledit3.text())>0 and len(self.ledit4.text())>0 and len(self.ledit5.text())>0 and len(self.ledit6.text())>0 and len(self.ledit7.text())>0 and self.ledit3.text().isnumeric() and self.ledit5.text().isnumeric() and self.ledit6.text().isnumeric() and len(self.ledit8.text())>0:
                try: 
                    with self.mydb.cursor() as cursor:
                        cursor.execute(f"INSERT INTO smartwatchs(brand, name, color, memory, ram, battary, price) values('{self.ledit1.text()}', '{self.ledit2.text()}', '{self.ledit4.text()}', '{self.ledit5.text()}', '{self.ledit6.text()}', '{self.ledit3.text()}');")
                except Exception as err: print(err)
                else: 
                    self.mydb.commit()
                    print("add smartw ok")
                    self.checklabel.setText('')
                finally:
                    self.ledit1.setText('') 
                    self.ledit2.setText('') 
                    self.ledit4.setText('') 
                    self.ledit5.setText('') 
                    self.ledit6.setText('') 
                    self.ledit3.setText('') 
            else:
                self.checklabel.setText("wrong entered!")
                self.ledit1.setText('') 
                self.ledit2.setText('') 
                self.ledit4.setText('') 
                self.ledit5.setText('') 
                self.ledit6.setText('') 
                self.ledit3.setText('')
                # Izoh bu shart da marketga aqllisoat qo'shish uchun hizmat qiladi kirtilgan malumotlar to'liqligi tekshiriladi to'liq bo'lsa u malumotlar malumotlar bazasidagi smartwatchs nomli jadval ga yoziladi
                
        elif self.sender().text()=="back":
            self.checklabel.setText('')
            self.close()
            self.open=AddDelProduct(1)
            self.open.show()
            # Izoh bu shartda joriy sahifadan orqaga qaytish uchun ishlatiladi
        else:
            self.close()
            # Izoh bu shart menu ni butunlay tark etishni bajaradi
        
        
class delProduct(Connectdb):
    def __init__(self,check) -> None:
        super().__init__()
        self.check=check
        
        self.create_db()
        self.setMinimumWidth(400)
        
        self.note=QLabel()
        if self.check==1:
            self.CreateProductPhone()
            self.note.setText("                        delphone")
        elif self.check==2:
            self.CreateProductLaptop()
            self.note.setText("                        dellaptop")
        elif self.check==3:
            self.CreateProductSmartWatch()
            self.note.setText("                        dellsmartwatch")
        
        self.delledit=QLineEdit()
        self.delledit2=QLineEdit()
        self.v_box=QVBoxLayout()
        self.h_box=QHBoxLayout()
        self.delledit.setPlaceholderText("id...")
        self.delete=QPushButton("delete")
        self.back=QPushButton("back")
        self.left=QPushButton("left")
        self.lis=[self.note, self.delledit, self.delete, self.left, self.back]
        self.setteelshett(self.lis)
        for i in range(5):
            if i<3: self.v_box.addWidget(self.lis[i])
            else: self.h_box.addWidget(self.lis[i])
            if i>1:
                self.lis[i].clicked.connect(self.eventclick)
        self.v_box.addLayout(self.h_box)
        self.setLayout(self.v_box)
        
        # Izoh yuqorida delProduct ning tugmalari, labellari, lineditlari yaratilgan va ular joylashishi keltirilib funksiyalarga ulangan  
        
    def eventclick(self):
        if self.sender().text()=="delete":
            try:
                with self.mydb.cursor() as cursor:
                    if self.check==1:
                        cursor.execute(f"DELETE FROM phones WHERE id='{self.delledit.text()}';")
                    elif self.check==2:
                        cursor.execute(f"""DELETE FROM laptops WHERE id="{self.delledit.text()}";""")
                    elif self.check==3:
                        cursor.execute(f"DELETE FROM smartwatchs WHERE id='{self.delledit.text()}';")
            except Exception as err: print(err)
            else:
                self.mydb.commit()
                print('del ok')
            finally:
                self.delledit.setText('')
                self.delledit2.setText('')
                                    
        elif self.sender().text()=="back":
            self.close()
            self.open=AddDelProduct(0)
            self.open.show()
        else:
            self.close()
        # Izoh bu funksiya mahsulotlarni id bo'yicha o'chirish uchun hizmat qiladi 
        
    def setteelshett(self, temp):
        for i in temp:
            i.setFixedHeight(50)
        

class ShowProduct(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.label=QLabel()
        self.label.setText("                                      Show Product")
        self.phone=QPushButton("Phones")
        self.laptop=QPushButton("Laptops")
        self.smartW=QPushButton("SmartWatchs")
        self.back=QPushButton("back")
        self.left=QPushButton("left")
        self.v_box=QVBoxLayout()
        self.h_box=QHBoxLayout()
        self.lis=[self.label, self.phone, self.laptop, self.smartW, self.left, self.back]
        self.setMinimumWidth(400)
        
        self.setteelshett(self.lis)
        for i in range(6):
            if i<4: self.v_box.addWidget(self.lis[i])
            else: self.h_box.addWidget(self.lis[i])
            if i!=0:
                self.lis[i].clicked.connect(self.eventclick)
        self.v_box.addLayout(self.h_box)
        self.setLayout(self.v_box) 
        # Izoh yuqorida ShowProduct ning tugmalari, labellari, lineditlari yaratilgan va ular joylashishi keltirilib funksiyalarga ulangan             
    
    def eventclick(self): 
        if self.sender().text()=="Phones":
            self.close()
            self.open=ShowPhones()
            self.open.show()
        elif self.sender().text()=="Laptops":
            self.close()
            self.open=ShowLaptops()
            self.open.show()
        elif self.sender().text()=="SmartWatchs":
            self.close()
            self.open=ShowSmarWatchs()
            self.open.show()
        elif self.sender().text()=="back":
            self.close()
            self.open=MenuPage()
            self.open.show()
        else:
            self.close()
        # Izoh bu funksiya da telefon, kompyuter yoki aqllisoat lardan bittasi tanlanadi va tanlanganiga mos keladigan sahifa ochilib tanlangan mahsul haqidagi malumotlar ko'rsatiladi
    
    def setteelshett(self, temp):
        for i in temp:
            i.setFixedHeight(50)    
                

class ShowPhones(QMainWindow, Connectdb):
    def __init__(self) -> None:
        super().__init__()                
        self.ui=pyqtdesign.Ui_MainWindow(1)
        self.ui.setupUi(self)
        self.create_db()
        self.CreateProductPhone()
        self.changetextlineedit()
        self.ui.pushButton_2.clicked.connect(self.eventbtn)
        self.ui.pushButton_3.clicked.connect(self.eventbtn)
        self.ui.lineEdit.textChanged.connect(self.changetextlineedit)
        # Izoh yuqorida ShowPhones ning tugmalari, labellari, lineditlari yaratilgan va ular joylashishi keltirilib funksiyalarga ulangan  
        
    def changetextlineedit(self):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute(f"""SELECT *FROM phones where name like '{self.ui.lineEdit.text()}%'""")
                answer=cursor.fetchall()
        except Exception as err: print(err)
        else:
            row=0
            self.ui.tableWidget.setRowCount(len(answer))
            for i in range(len(answer)):
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(answer[i][0])))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(answer[i][1])))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(answer[i][2])))
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(answer[i][3])))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(answer[i][4])+"GB"))
                self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(answer[i][5])+"GB"))
                self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(answer[i][6])+"MP"))
                self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(str(answer[i][7])[:-2]+"$"))
                row+=1
            print("read phones ok")
            # izoh bu funksiya telefon haqidagi malunmotlarni malumotlar bazasidagi phones nomli jadvaldan o'qib oladi va interfeysga chiqaradi
    def eventbtn(self):
        if self.sender().text()=="Left":
            self.close()
        else:
            self.ui.lineEdit.setText('')
            self.close()
            self.open=ShowProduct()
            self.open.show()
        # Izoh bu funksiya joriy sahifadan chiqib ketish uchun hizmat qiladi


class ShowLaptops(QMainWindow, Connectdb):
    def __init__(self) -> None:
        super().__init__()
        self.ui=pyqtdesign.Ui_MainWindow(2)
        self.ui.setupUi(self)
        self.create_db()
        self.CreateProductLaptop()
        self.changetextlineedit()
        self.ui.pushButton_2.clicked.connect(self.eventbtn)
        self.ui.pushButton_3.clicked.connect(self.eventbtn)
        self.ui.lineEdit.textChanged.connect(self.changetextlineedit)
        # Izoh yuqorida ShowLaptops ning tugmalari, labellari, lineditlari yaratilgan va ular joylashishi keltirilib funksiyalarga ulangan  
        
    def changetextlineedit(self):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute(f"""SELECT *FROM laptops where name like '{self.ui.lineEdit.text()}%'""")
                answer=cursor.fetchall()
        except Exception as err: print(err)
        else:
            row=0
            self.ui.tableWidget.setRowCount(len(answer))
            for i in range(len(answer)):
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(answer[i][0])))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(answer[i][1])))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(answer[i][2])))
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(answer[i][3])))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(answer[i][4])+"GB"))
                self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(answer[i][5])+"GB"))
                self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(answer[i][6])))
                self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(str(answer[i][7])))
                self.ui.tableWidget.setItem(row, 8, QTableWidgetItem(str(answer[i][8])[:-2]+"$"))
                row+=1
            print("read laptops ok")
            # izoh bu funksiya kompyuter haqidagi malunmotlarni malumotlar bazasidagi laptops nomli jadvaldan o'qib oladi va interfeysga chiqaradi
    
    def eventbtn(self):
        if self.sender().text()=="Left":
            self.close()
        else:
            self.ui.lineEdit.setText('')
            self.close()
            self.open=ShowProduct()
            self.open.show()
            # Izoh bu funksiya joriy sahifadan chiqib ketish uchun hizmat qiladi

class ShowSmarWatchs(QMainWindow, Connectdb):
    def __init__(self) -> None:
        super().__init__()
        self.ui=pyqtdesign.Ui_MainWindow(3)
        self.ui.setupUi(self)
        self.create_db()
        self.CreateProductSmartWatch()
        self.changetextlineedit()
        self.ui.pushButton_2.clicked.connect(self.eventbtn)
        self.ui.pushButton_3.clicked.connect(self.eventbtn)
        self.ui.lineEdit.textChanged.connect(self.changetextlineedit)
        # Izoh yuqorida ShowSmartWatchs ning tugmalari, labellari, lineditlari yaratilgan va ular joylashishi keltirilib funksiyalarga ulangan  
        
    def changetextlineedit(self):
        try:
            with self.mydb.cursor() as cursor:
                cursor.execute(f"""SELECT *FROM smartwatchs where name like '{self.ui.lineEdit.text()}%'""")
                answer=cursor.fetchall()
        except Exception as err: print(err)
        else:
            row=0
            self.ui.tableWidget.setRowCount(len(answer))
            for i in range(len(answer)):
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(answer[i][0])))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(answer[i][1])))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(answer[i][2])))
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(answer[i][3])))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(answer[i][4])+"GB"))
                self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(answer[i][5])+"MAH"))
                self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(answer[i][6])[:-2]+"$"))
                row+=1
            print("read smartwatchs ok")
             # izoh bu funksiya aqllisoat haqidagi malunmotlarni malumotlar bazasidagi smartwatchs nomli jadvaldan o'qib oladi va interfeysga chiqaradi
                
    def eventbtn(self):
        if self.sender().text()=="Left":
            self.close()
        else:
            self.ui.lineEdit.setText('')
            self.close()
            self.open=ShowProduct()
            self.open.show()
         # Izoh bu funksiya joriy sahifadan chiqib ketish uchun hizmat qiladi



        
app=QApplication([])        
win=KirishPage()
sys.exit(app.exec_())
