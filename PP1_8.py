
def q1():
  bool1 = True
  bool2 = False 
  print (bool1 and bool2)
  print (bool1 or bool2)

def q2():
  bool1 = int(input("Enter an integer: "))
  print (not(not(bool1)))

def q3():
  bool1 = float(input("Enter a number: "))
  print (bool1 >= 0 and bool1 <= 10)


def q4():

  dddd=input("Input food: ")
  aa=input("Input drink: ")
  if dddd=='pizza' and aa=='pop':
    print(False)
  else:
    print(True)

def q5():
  skib = int(input("Enter an integer: "))
  print(f"The integer {skib} is {skib % 2 == 0}.")

#Do not edit code after this
#Comment out the followwing code when running tests

#q1()
#q2()
#q3()
#q5()
