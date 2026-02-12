import random
l=['rock','paper','scissor']
ccount = 0
ucount = 0
while True:

    uc=int(input('''
    Game Start
    1. YES
    2. NO / EXIT
    '''))
    if uc==1:
      for a in range (1,6):
         userinput=int(input('''
         1. Rock
         2. Paper
         3. Scissor''') )
         if userinput==1:
              userchoice='rock'
         elif userinput==2:
              userchoice='paper'
         elif userinput==3:
              userchoice='scissor'
         cchoice=random.choice(l)
         if cchoice==userchoice:
             print('Computer value',cchoice)
             print(' You value',userchoice)
             print('Game Draw')
             ccount=ccount+1
             ucount=ucount+1
         elif ((userchoice=="rock" and cchoice=="scissor") or (userchoice=="paper" and cchoice=="rock")
                   or (userchoice=="scissor" and cchoice=="paper")):
                      print('Computer value',cchoice,'You value',userchoice)
                      print('You Win')
                      ucount=ucount+1
         else:
                       print('Computer value',cchoice,'You value',userchoice)

                       print('You Lose')
                       ccount=ccount+1
      if ucount==ccount:
              print("Final Game Draw")
              print('User score',ucount)
              print('computer score',ccount)


      elif ucount>ccount:
              print('Final You win')
              print('User score',ucount)
              print('computer score',ccount)
      else:
              print('Final You lose')
              print('User score', ucount)
              print('computer score', ccount)
    else:
         break
