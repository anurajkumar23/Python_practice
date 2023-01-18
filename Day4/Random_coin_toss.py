#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

randomInteger= random.randint(0,1)

if randomInteger == 1:
    print("Heads")
else:
    print("Tails")