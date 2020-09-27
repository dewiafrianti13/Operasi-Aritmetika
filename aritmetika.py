

# fungsi penjumlahan
def jumlah(x, y):
   return x + y

# fungsi pengurangan
def kurang(x, y):
   return x - y

# fungsi perkalian
def kali(x, y):
   return x * y

# fungsi pembagian
def bagi(x, y):
   return x / y

#fungsi Pangkat (eksponen)
def pangkat(x,y):
    return x**y

#fungsi modulus
def modulus(x,y):
    return x%y

#fungsi floor division
def floor(x,y):
    return x//y

# menu operasi
print("Program Kalkulator Sederhana")
print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
print("5.Pangkat")
print("6.Modulus")
print("7.Floor Division")
print("*Note : Floor division adalah pembulatan hasil bagi")

# Meminta input dari user
choice = input("Masukkan pilihan(1/2/3/4/5/6/7): ")

num1 = float(input("Masukkan bilangan pertama: "))
num2 = float(input("Masukkan bilangan kedua: "))

if choice == '1':
   print(num1,"+",num2,"=", jumlah(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", kurang(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", kali(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", bagi(num1,num2))

elif choice == '5':
   print(num1,"**",num2,"=", pangkat(num1,num2))

elif choice == '6':
   print(num1,"%",num2,"=", modulus(num1,num2))

elif choice == '7':
   print(num1,"//",num2,"=", floor(num1,num2))
else:
   print("Input salah")