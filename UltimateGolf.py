import random #Import random module to create the random generator.

#Define get_par function to check if the player inputs right number when they entering their par.
def get_par(): 
   while True:
      _par = input("What par do you want for your golf game? (The number must between 3 and 5 inclusive.)")
      if _par.isdigit() == True:
         if int(_par) >= 3 and int(_par) <= 5:
            break #Only when the par entered by the player is between 3 and 5 inclusive, the loop ends.
         else:
            print("I did not understand that response, the number must between 3 and 5 inclusive, please re-enter your par.")
      else:
         print("I did not understand that response, you can't input letters, sumbols, negative number or decimal, which means your par must be a positive integer.")
   return _par

def get_distance():
   while True:
      _distance = input("How many meters to the hole for this game do you want? (The whole number must between 195 and 250 inclusive.)")
      if _distance.isdigit() == True:
         if int(_distance) >= 195 and int(_distance) <= 250:
            break
         else:
            print("I did not understand that response. The number must between 195 and 250 inclusive, please re-enter the distance.")
      else:
         print("I did not understand that response. You can't input letters, sumbols, negative number or decimal, which means the distance must be a positive integer.")
   return int(_distance)

def get_choice():
   while True:
      _choice = input("\nGolf Menu:\n[I]nstructions\n[P]lay golf\n[Q]uit")
      if _choice == "I" or _choice == "i" or _choice == "P" or _choice == "p" or _choice == "Q" or _choice == "q":
         break
      else:
         print("I did not understand that response. Please choose either I, P or Q.")
   return _choice

def get_club():
   _club = input("\nClub selection:\nPress [D] for driver.\nPress [I] for Iron.\nPress [P] for Putter.")
   if _club == "D" or _club == "d":
      print("You choose club: D, Driver.")
   elif _club == "I" or _club == "i":
      print("You choose club: I, Iron.")
   elif _club == "P" or _club == "p":
      print("You choose club: P, Putter.")
   else:
      print("Sorry! Invalid club selection, and this shot will be an Air Swing\nPlease choose either D, I or P next shot.")
      _club = "airSwing"
   return _club

def cal_shot(_club,_distance):
   if _club == "D" or _club == "d":
      _shot = random.randint(80,120)
   elif _club == "I" or _club == "i":
      _shot = random.randint(24,36)
   elif (_club == "P" or _club == "p") and _distance < 10:
      _shot = round(random.uniform(0.8,1.2) * _distance)
   elif _club == "airSwing":
      _shot = 0
   else:
      _shot = random.randint(8,12)
   return _shot


def main():
   name = input("Dear player, what's your name?")
   print("Welcome "+name+".")
   par = get_par()
   distanceInitial = get_distance()
   holeTimes = 0
   score = 0
   parState = 0
   history = []
   while True:
      choice = get_choice()
      if choice == "P" or choice == "p":
         distance = distanceInitial
         shotTimes = 0
         parResult = 0
         print("\nThis hole is a "+str(distance)+"m par "+par+"\nYou are "+str(distance)+"m from the hole, after "+str(shotTimes)+" shot")
         while True:
            if distance == 0:
               print("Clunk! After", shotTimes, "hits your ball is in the hole!")
               if shotTimes == int(par):
                  print("And that is par!")
                  parResult = shotTimes - int(par)
                  history.append("On par")
               elif shotTimes > int(par):
                  print("Disappointing. You are", shotTimes-int(par), "over par for this hole.")
                  parResult = shotTimes - int(par)
                  parResultHistory = str(parResult)+" over par."
                  history.append(parResultHistory)
               else:
                  print("Congratulations. You are", int(par)-shotTimes, "under par for this hole.")
                  parResult = shotTimes - int(par)
                  parResultHistory = str(-parResult)+" under par."
                  history.append(parResultHistory)
               history.append(shotTimes)
               score = score + shotTimes
               parState += parResult
               holeTimes += 1
               if parState < 0:
                  if holeTimes == 1:
                     print("Your overall score is", score, "and you are", abs(parState), "under par after", holeTimes, "hole")
                  else:
                     print("Your overall score is", score, "and you are", abs(parState), "under par after", holeTimes, "holes")
               elif parState == 0:
                  if holeTimes == 1:
                     print("Your overall score is", score, "and you are just par after", holeTimes, "hole")
                  else:
                     print("Your overall score is", score, "and you are just par after", holeTimes, "holes")
               else:
                  if holeTimes == 1:
                     print("Your overall score is", score, "and you are", parState, "over par after", holeTimes, "hole")
                  else:
                     print("Your overall score is", score, "and you are", parState, "over par after", holeTimes, "holes")
               break
            else:
               shotTimes += 1
               club = get_club()
               shot = cal_shot(club, distance)
               print("Your shot went "+str(shot)+"m")
               distance = abs(distance - shot)
               if shotTimes == 1:
                  print("You are "+str(distance)+"m from the hole after "+str(shotTimes)+" shot")
               else:
                  print("You are "+str(distance)+"m from the hole after "+str(shotTimes)+" shots")
         print("You have finished round "+str(holeTimes)+", would you like to paly another round or quit the game?")
      elif choice == "I" or choice == "i":
         print("\nThis is a simple golf game in which each hole is "+str(distanceInitial)+"m game away with par "+str(par)+". You are able to choose from 3 clubs, the Driver, Iron or Putter. The Driver will hit around 100m, the Iron around 30m and the Putter around 10m. The putter is best used very close to the hole.\nPlease choose the menu.")
      else:
         print("Thanks for playing "+name+".")
         if holeTimes > 0:
            print("Your Round history is:\n")
            for i in range(holeTimes):
               print("Round "+str(i+1)+": "+str(history[i*2+1])+" shots. "+history[i*2])
            print("Your overall score is", score)
         else:
            pass
         break

main()