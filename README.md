# D-D-5E-character-creator

D&D Character creator
Object-Oriented program, needing a container “character” class.
A way to store information for created characters.
(or have them be re-created using a main function for simplicity)
A way to create custom parts of each character
A character has “stats”, “class”, “background”, “race”
Stats are “STR, DEX, CON, INT, WIS, CHA”
13 different character class options
Too many to count races, we can start with PHB and branch from there
Last function would be to have a “create a random character”
Would need to also specify parameters, “do they want something completely random,
or something that could function decently in the scope of the game”

Implementation 1 Design: 
1. Create a character sheet 
2. Have a randomized generator function 
3. Be able to create your own features 
4. Save - will be modeled by a main function first 
5. Create a pop up

Character 
	Race (subrace) - add a true/false flag for using specific racial bonuses (later)
	Class (subclass) - LVL
	Stats - basic stats generator. Or offer the generic stat (6 static numbers) OR the point buy system(research and ignore for now). 
	Background
	Items - dependent on background and class


Race - 8 options 
		those 8 options sometimes have 2-3 sub options. 

Class - 13 options - 3->8 sub options. 

Character holds Race and Class and Background
	Race is the parent class (empty header), all other races are child classes - subraces are handled inside of the child classes
	(same logic for class choice)

	Background start with similar logic, adjust for alternate bonuses.

## How to run this program
open up the main function and start creating characters! 
Next open up a powershell terminal and run this line: 
"python main.py" and that will start the program
***NEW INSTRUCTIONS!***
After booting up "python main.py" in your terminal you will be prompted to answer 
questions about your new character! Options are limited for now but will be updated 
with more functionality soon! It is advised to fill in the prompt fully to avoid crashes
