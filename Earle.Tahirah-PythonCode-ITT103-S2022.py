"""
Author: Tahirah Earle
Date Created: April 20, 2022
Course: ITT103
Purpose: The purpose of this program is to write a code that calulate the commission receive for a number of salespersons based on the class 
that is use to assign a rate and the amount they made is sales. Until the program is terminate by a condition.
"""

# Welcome Message in the form of a GUI.
from tkinter import* 
root=Tk()
root.title("Start Message")
root.geometry('650x300')
root.configure(bg='black')
label1=Label(root,text='Welcome, JamEx Ltd. Salesperson !', bg='black',fg='medium spring green', font=('Cambria', 22))
label1.grid(row=0, column=0, padx=5, pady=10)
label2=Label(root,text='This program will be used to calculate your commission \n The program will loop for an undetermine number of employees\n and will terminate when a class of 7 in entered.', 
             bg='black',fg='white', font=('Cambria', 12))
label2.grid(row=1, column=0, padx=5, pady=10)
label3=Label(root,text='This programme was created by Tahirah Earle \n For the course ITT103- Programming Techniques',bg='black',
fg='white', font=('Cambria', 12))
label3.grid(row=2, column=0, padx=5, pady=10)
button1=Button(root, text="Click here to start", command=root.destroy,bg='green',fg='white',font=('Cambria', 12)).grid(column=2, row=6)
root.mainloop()

# Start of main program.
count=0
"""The condtion used to test the loop is the while true do,I used this loop because there was no input thus far to test the loop againts
since it is set to true the loop that will continue to run until you explicitly breakout of it. Because True will always evaluate to True,
you have to force the loop to end when you want it to."""
while True:
  count+=1
  print('─' * 40,"Loop",count,'─' * 40) 
  sales_p_num=str(input("Enter sales person number :#"))
  sale_class=int(input("Enter sales person class: "))
  sale_amount=float(input("Enter sales amount :$"))
  
  #Function that returns the product of rate and sales amount.
  #Instead of coding a arithemtic statement for each part of the program that calcuates commission, the function can be called on.
  def class_commisssion(rate, sale_amount ):
      return rate * sale_amount
    
  # Raise a value error if a negative sale amount or less than 0 is entered. Sothat the program doesn't calculate a negative commission. 
  try:
    if sale_amount <0 :
      raise ValueError("Sorry! Commission cannot be calcuate when negative amount or less than $1.00 is entered")
  except ValueError as ve:
    print(ve)
    
  # Determine and assign commission rate to each class of salespersons and calculate commission.   
  if  sale_class == 1 and sale_amount <= 1000 and sale_amount > 0:                      
    rate=0.06
    commission=class_commisssion(rate, sale_amount)               # commission calculation 
    print("The commission is $",'%.2f'%commission)                # format commssion to only displaying 2 d.p because of how currency is wriiten.
    print('─' * 91)                                               # line to separate the code and ouput each time it loops.
  elif sale_class == 1 and sale_amount > 1000 and sale_amount < 2000: 
    rate=0.07       
    commission=class_commisssion(rate, sale_amount)
    print("The commission is $", '%.2f'%commission)
    print('─' * 91) 
  elif sale_class == 1 and sale_amount >= 2000 : 
    rate=0.10
    commission=class_commisssion(rate, sale_amount) 
    print("The commission is $", '%.2f'%commission)
    print('─' * 91)  
  elif sale_class == 2 and sale_amount < 1000 and sale_amount > 0: 
    rate=0.04
    commission=class_commisssion(rate, sale_amount) 
    print("The commission is $", '%.2f'%commission)
    print('─' * 91) 
  elif sale_class == 2 and sale_amount >= 1000: 
    rate=0.06
    commission=class_commisssion(rate, sale_amount) 
    print("The commission is $", '%.2f'%commission)
    print('─' * 91) 
  elif sale_class == 3: 
    rate=0.045
    commission=class_commisssion(rate, sale_amount) 
    print("The commission is $", '%.2f'%commission)
    print('─' * 91) 
  # If none of the conditions was true. 
  else:
    # to detect the type of error so that it can be displyed to the user where they went wrong.
    if sale_amount < 0: 
      error=("Sale Amount Error")
    else:
      error=("Sale Class Error")
    print("There was an error -".upper(), error )
    print('─' * 91) 
    
  if sale_class == 7: 
    break
  """The loop will break at 7 because when testing the program you would have to test as much data a possible
  and since the last class that has a rate is 3, anything after that will generate an error message."""
  
# Exiting Message in the form of a GUI to let users know the program has ended.
from tkinter import *
root=Tk()
root.title("Exiting Message")
root.geometry('650x300')
root.configure(bg='black')
label1=Label(root,text='TIME TO SAY GOOD-BYE !', bg='black',fg='medium spring green', font=('Cambria', 24))
label1.grid(row=0, column=0, padx=5, pady=10)
label2=Label(root,text='The end, the program has been terminate \n \n \n THANK FOR USING MY PROGRAM\n \n \n I hope that you were able to use it to do what it was intended to \n without any bugs or errors and or the need to fix any\n \n',
             bg='black',fg='white', font=('Cambria', 12))
label2.grid(row=2, column=0, padx=5, pady=10) 
button1=Button(root, text="Click here to leave", command=root.destroy, bg='red',fg='white',font=('Cambria', 12)).grid(column=3, row=8)
root.mainloop()

print("The end, the program has been terminate")                  

