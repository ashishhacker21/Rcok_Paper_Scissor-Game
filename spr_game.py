import random
# check winning positon

def WL(a ,b):
    if a==b:
      print("______________________________") 
      print("<< draw! >>")
    elif a=="scissor" and  b=='paper':
      print("______________________________")
      print('<< YOU WIN >>')
    elif a=="paper" and b=='scissor':
      print("______________________________")
      print('<< computer win >>')
    elif a=="paper" and b=='rock':
       print("______________________________")
       print("<< YOU WIN >>")
    elif a=="rock" and b=='paper':
       print("______________________________")
       print('<< computer win >>')
    elif a=="rock" and b=='scissor':
       print("______________________________")
       print('<< YOU WIN >>')
    elif a=="scissor " and b=='rock':
       print("______________________________")
       print('<< computer win >>')
    print("______________________________")   
          
while True:
 # quit or continue
 print('''
press 1 to continue.
press 2 to quit.
''')
 quit = input()
 if quit == "1":
    print("continue your game")
 elif quit == "2":
    print("quit successfuly")
    break
 else:
    print("Enter valid value 1 or 2 ")
    continue
    #decoration part
 print("______________________________")
 str1 = "YOU"
 str2 = "computer"
 print(str1.center(23,'*')) 
 # Take input from user    
 a = input() #enter the sezier , paper or rock , any one
 # check the input spelling
 if a == "scissor":
    print(str2.center(22,'*'))
 elif a == "paper":
    print(str2.center(22,'*'))
 elif a == "rock":
    print(str2.center(22,'*'))
 else:
    print("please enter correct spelling !")
    continue
 # computer turn
 dict = {1 : "scissor",2: "paper" , 3 : "rock"}
 n=random.randint(1,3)
 b = dict[n]
 print(b)

 WL(a,b)
 


