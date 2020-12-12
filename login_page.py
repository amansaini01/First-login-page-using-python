import numpy as np


print("*** WELCOME *** \n")

while(True):
  username = input("\nUsername - ")
  password = input("\nPassword - ")

  if (username == "student" and password == "student12"):
    num = np.random.randint(1,10)
    print("\nKey for human - ", num)
    num1 = int(input("\nNot a Bot(enter key) - "))
    if(num   == num):
      print("\nLogin Succesful!!!")
      break
  else:
    print(username + "is Wrong username. \nEnter Again.")


