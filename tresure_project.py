print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choosing_side = input('\nYou\'re at a crossroad. Where do you want to go? Type "left" or "right": ').lower()

if choosing_side == "left":
    print("\nIt is a trap! Game over.")
    print('''
                                       _.-'
                                  _.-'
                 _____________.-'________________
                /       _.-'   O                /|
               /  i====_======O           _____/ /
              /  /    _.-   'O          /     /|/
             /  /     | p   o          / (   / /
            /  /           O         /___   / /
           /  L===========O                /|/
          /______________O________________/ /
         |________________________________|/
	''')

if choosing_side == "right":
		lake_part = input('\nYou\'ve come to a lake. There is an Island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
	
		if lake_part == "swim":
			print("\nYou got attacked by a crocodile.")
			print('''
					.-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  ' - '   '  '  '  '  '  '  '  '-.
         '.___ '    .   .--_'- '   '-'      '-'    _'-' '._
          V: V 'vv-'   '_   '.               .'   _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.           : :
                    (((____.-'               '-.  /   : :
                                            (((-'\\ .'  /
                                          _____..'  .'
                                        '-._____.-' ''')
		else:
			print("\nYour boat is here!")
			print('''
                    _
                  / | \\
                 / _|_ \\
                 ___|____
                \_o_o_o_/
                ~~ |  ~~~~~
    ''')
			
			door_colours = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()

			if door_colours == "red":
				print("\nIt's a room full of fire. Game Over.")
				print('''	
    ,.     (   .      )        .      "
   ("      )  )'     ,'        )  . (`     '`
 .; )   ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..jb
''')
			elif door_colours == "yellow":
				print("\nYou entered in a room of beasts. Game Over.")
				print('''
                    (        )
                  ( (( ( ( ) ))
                  | o \ / o) |
                  (  (   _ ' )
                   (._.      /\__
                  ,\___,/ '        ')
    '.,_,,       (  .- .   .           )
     \   \\     ( '            )(        )
      \   \\    \.  _.__ __  (    .  |
       \  /\\   .(   .'  /\        '.    )
        \(  \\.-' ( /    \/           \)
         '  ())     _'.- | /\/\/\/\/\ |
             '\\ .(       | \/\/\/\/\/ |
               '((  \    /\    /
               ((((  '.      __\/__.')
                ((,) /          ((()   )
                 "..-,          (()("   /
                    _//.        ((()   ."
          _____ //,/"___ (((    ', ___
                                   ((   )
                                    /  /
                                _/, /'
                              /,  /,"

''')
			else:
				print("\nYou found the treasure! You Win!")
				print('''
                                   ,"  ".
             _      .---.    _ /#     
           ,' `.  ,'     `  .." ".       ,--.
           |#   `/ #        (#     )     /)
            `.   |           )   (`.__/    /
              `. \          (     ) /'/   /
                `.\         /)   ( ( /   /
                   `.    .'(     )  y   /
                     >_<\  `._.'(  /
                     /   ) /'-`.  ->,-'
                    (   ( (   (
                     )     )   )
                          (
''')
