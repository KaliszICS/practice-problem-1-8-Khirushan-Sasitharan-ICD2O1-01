
def q1():
  bool1 = True
  bool2 = False 
  print (bool1 and bool2)
  print (bool1 or bool2)

def q2():
  bool1 = int(input("Enter an integer: "))
  print (not(not(bool1)))

def q3():
  bool1 = int(input("Enter a number: "))
  print (bool1 > 0 and bool1 < 10)


def q4():

  bool1 = input("Input food: ")
  bool2 = input("Input drink: ")
  print (bool1 == "pizza" or "pop" and bool2 == "pizza" or "pop")



def q5():
  #Ask the user, “Enter an integer: ” Input the user’s response from the keyboard, 
  #test the integer to see if it is even (use the modulus operator % and 2 to do this), and then output the result as shown below (several runs are shown):
  skib = int(input("Enter an integer: "))
  if skib % 2 == 0: 
    doop = (f"The integer {skib} is True")
    print (doop)
  else: 
    no = (f"The integer {skib} is False")
    print (no)

#Do not edit code after this
#Comment out the followwing code when running tests

q1()
q2()
q3()
q4()
q5()
