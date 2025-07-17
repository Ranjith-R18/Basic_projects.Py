import random
stages=['''
  +---+
  |        |
  0       |
 /|\\    |
 / \\    |
           |
=========''', '''
  +---+
  |        |
  O      |
 /|\\    |
 /        |
           |
=========''', '''
  +---+
  |      |
  O    |
 /| \\|
         |
         |
=========''', '''
  +---+
  |        |
  O      |
 /|       |
           |
           |
=========''', '''
  +---+
  |       |
  O     |
  |       |
          |
          |
=========''', '''
  +---+
  |       |
  O     |
          |
          |
          |
=========''', '''
  +---+
  |       |
          |
          |
          |
          |
=========''']

word_list=('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
word=random.choice(word_list)
print(word)
lives=6

placeholder=""
wordlength=len(word)
for i in range(wordlength):
  placeholder+="_"
print(placeholder)

game_over=False
correct_letter=[]

while not game_over:
  print(f"***********{lives} lives left********")
  guess=input("Guess a letter:").lower()
  if guess in correct_letter:
  	print(f"you have already guessed {guess},guess other letter")
  
  display=""
  for letter in word:
    if letter == guess:
      display+=letter
      correct_letter.append(letter)
    elif letter in correct_letter:
      display+=letter
    else:
      display+="_"
  print(display)
  
  if guess not in word:
  	print(f"you guessed {guess},which is not in the word . You lost a life")
  
  if guess not in word:
      lives-=1
      if lives==0:
          game_over =True 
          print(f"you have lost. the correct word is {word}")
          
  if "_" not in display:
    game_over=True 
    print("the end")
  print(stages[lives])