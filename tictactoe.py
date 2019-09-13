board = [0,1,2,
         3,4,5,
         6,7,8]

def display():
    print(board[0],"|",board[1],"|",board[2])
    print("----------")
    print(board[3],"|",board[4],"|",board[5])
    print("----------")
    print(board[6],"|",board[7],"|",board[8])
display()

name = input("Enter first user name")
print("Welcome to Tic Tac Toe >>>",name)
name2 =input("Enter second user name")
print("Welcome to Tic Tac Toe >>>",name2) 

choice = str(input("Press X and O"))
if choice == "X" or choice =="x" or choice == "O" or choice=="o":
    print(name,">>>",choice)
else:
    print(name2,">>>",choice)

while True:
    print(name)
    choose = int(input("Choose place user1 >>> "))
    if board[choose]!="X" and board[choose]!="O":
        board[choose]= "X"
        display()
        
        
        if board[0]=="X" and board[1]=="X" and board[2]=="X": 
            print(name,"wins")
            display()
            break
        elif board[0]== "X" and board[3]=="X" and board[6]=="X":
            print(name,"wins")
            display()
            break
        elif board[0]=="X" and board[4]=="X" and board[8]=="X" :
            print(name,"wins")
            display()
            break
        elif board[1]=="X" and board[4]=="X" and board[7]=="X":
            print(name,"wins")
            display()
            break
        elif board[2]=="X" and board[5]=="X" and board[8]=="X":
            print(name,"wins")
            display()
            break
        
        elif board[2]=="X" and board[4]=="X" and board[6]=="X":
            print(name,"wins")
            display()
            break
        
        elif board[3]=="X" and board[4]=="X" and board[5]=="X":
            print(name,"wins")
            display()
            break
        
            
            
    print(name2)
    choose1 = int(input("Choose place user2 >>> "))
    if board[choose1]!="O" and board[choose1]!="X":
        board[choose1]= "O"
        display()
        
        
        
        if board[0]=="O" and board[1]=="O" and board[2]=="O": 
            print(name2,"wins")
            display()
            break
        elif board[0]== "O" and board[3]=="O" and board[6]=="O":
            print(name2,"wins")
            display()
            break
        elif board[0]=="O" and board[4]=="O" and board[8]=="O" :
            print(name2,"wins")
            display()
            break
        elif board[1]=="O" and board[4]=="O" and board[7]=="O":
            print(name2,"wins")
            display()
            break
        elif board[2]=="O" and board[5]=="O" and board[8]=="O":
            print(name2,"wins")
            display()
            break
        
        elif board[2]=="O" and board[4]=="O" and board[6]=="O":
            print(name2,"wins")
            display()
            break
        
        elif board[3]=="O" and board[4]=="O" and board[5]=="O":
            print(name2,"wins")
            display()
            break
            
############################Using Tkinter GUI#################################            
from tkinter import *
from tkinter import messagebox
root =Tk()  
root.title("TIC TAC TOE")

click = False
def TTT(button):
    global click
    
    if button['text']==' ' and click == True:
        button['text']="X"
        count+=1
        click=False
    elif button['text']==' ' and click == False:
        button['text']="O"
        count+=1
        click=True
    elif button["text"]=="O" or button["text"] == "X":
        messagebox.showinfo("Try Again","Retry")
    
    
    if (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or 
         button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
         button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
         button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
         button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
         button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
         button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
         button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        ans = ("O WIN")
        messagebox.showinfo("WINNER",ans)
    
    elif (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or 
         button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
         button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
         button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
         button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
         button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
         button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
         button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        ans = ("X WIN")
        messagebox.showinfo("WINNER",ans)

        
    
button = StringVar()
button1 = Button(root,text=" ",font=("aerial",20,"bold"),bg="white",padx=20,command=lambda:TTT(button1))
button1.grid(row=0,column=1,sticky = E+W+N+S)
button2 = Button(root,text=" ",font=("aerial",20,"bold"),bg="white",padx=20,command=lambda:TTT(button2))
button2.grid(row=0,column=2,sticky = E+W+N+S)
button3 = Button(root,text=" ",font=("aerial",20,"bold"),bg="white",padx=20,command=lambda:TTT(button3))
button3.grid(row=0,column=3,sticky = E+W+N+S)
button4 = Button(root,text=" ",font=("aerial",20,"bold"),bg="white",padx=20,command=lambda:TTT(button4))
button4.grid(row=1,column=1,sticky = E+W+N+S)
button5 = Button(root,text=" ",font=("aerial",20,"bold"),bg="white",padx=20,command=lambda:TTT(button5))
button5.grid(row=1,column=2,sticky = E+W+N+S)
button6 = Button(root,text=" ",font=("aerial",20,"bold"),bg="white",padx=20,command=lambda:TTT(button6))
button6.grid(row=1,column=3,sticky = E+W+N+S)
button7 = Button(root,text=" ",font=("aerial",20,"bold"),bg="white",padx=20,command=lambda:TTT(button7))
button7.grid(row=2,column=1,sticky = E+W+N+S)
button8 = Button(root,text=" ",font=("aerial",20,"bold"),bg="white",padx=20,command=lambda:TTT(button8))
button8.grid(row=2,column=2,sticky = E+W+N+S)
button9 = Button(root,text=" ",font=("aerial",20,"bold"),bg="white",padx=20,command=lambda:TTT(button9))
button9.grid(row=2,column=3,sticky = E+W+N+S)             
        
root.mainloop()    
    
    
        
   
    
    
    
    