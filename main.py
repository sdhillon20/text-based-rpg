# Text-Based RPG: Aliens of Akrabar
# Ask use for name and greet use.
name = input("Welcome to Aliens of Akrabar! What is your name? ")
print(f"Welcome to the game {name}!")

# Start the game
print("You wake up on a spaceship after a long journey. You don't know how long you have been here for.")
print("[G]et out of bed.")
print("go back to [s]leep.")

ans1 = input("Choice: ").lower().strip()

if ans1 == "g":
   print( "You get up and look around. There are 3 other beds. There are people in them.")
   print("Try to [w]ake the others.")
   print("[L]eave the room.")

 ans2 = input("Choice: ").lower().strip()
 
 if ans2 == "w":
     print("......")
     print("Go get a [m]op to clean up the mess.")
     print("[R]un away.")
     
  elif ans2 == "1" :
      print("....")

 

elif ans1 == "s":
    print("You hypersleep for 50 years and die in your sleep.")
    
print(f"Thanks for playing the game {name}!")