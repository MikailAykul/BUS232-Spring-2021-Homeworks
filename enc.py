#f = open('C:/Users/wib/Desktop/mikail/data.txt', 'r')
import pyAesCrypt
selection = int(input("What would you like to do ? \n1 - Encription\n2 - decription"))
print(selection)
if selection == 1:
  path = input("What is the file name in file ? ")
  password = input("What is the Password ? ")
  pyAesCrypt.encryptFile("C:/Users/wib/Desktop/mikail/"+path, "C:/Users/wib/Desktop/mikail/"+path+".enc", password)
elif selection == 2:
  path = input("What is the file name in file ? ")
  password = input("What is the Password ? ")
  pyAesCrypt.decryptFile("C:/Users/wib/Desktop/mikail/"+path, "C:/Users/wib/Desktop/mikail/"+path, password)
else:
  print("Wrong input")
