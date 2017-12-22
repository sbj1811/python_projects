# Fill in the blanks Quiz
from copy import deepcopy
# Valid replacement dictionary for each level
# Easy list of replacements
replacement_list_easy = {'___1___': 'Apple', 
				 	     '___2___': 'publicly', 
				         '___3___': 'iPhones',
				         '___4___': 'iOS'}

# Medium list of replacements
replacement_list_medium = {'___1___': 'London', 
				           '___2___': 'Queen Elizabeth', 
				           '___3___': 'Buckingham Palace',
				           '___4___': 'The Crown', 
			               '___5___': 'Netflix'}

# Hard list of replacements
replacement_list_hard = {'___1___': 'function', 
				         '___2___': 'arguments', 
				         '___3___': 'None',
				         '___4___': 'list',
				         '___5___': 'objects'}

# String pattern to be replaced:
easy = """Steve Jobs founded ___1___ .Inc in 1976, the world's most valuable ___2___ traded companies. 
Their touch screen phones are called ___3___. They run ___4___ mobile operating system."""

medium = """The capital of UK is ___1___. The Monarch of UK is ___2___, who lives in ___3___. 
The popular TV drama - ___4___ airs on streaming service ___5___, which is based on her life."""

hard = """In Python, a ___1___ is created with the def keyword. You specify the inputs a function takes by
adding ___2___ separated by commas between the parentheses. Functions by default return ___3___ if you
don't specify the value to return. Arguments can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as ___5___ and lambda functions."""

def word_in_replacement_list(word, replacement_list):
	"""
    This function determines if word is in replacement list
    :inputs: word       - word to be checked
    		 replacement_list - the replacement list for selected game level
    :outputs: Returns the replacement string from the replacement list if found 
    		  or else returns None. 
    """
	for pos in replacement_list:
		if pos in word:
			return pos
	return None
 
def try_check(try_count):
	"""
    This function checks the remaining number of trys
    :inputs:  try_count  - No of trys remaining 
    :outputs: Returns the remaining trys. If all trys used, then ends the game.
    """
	if try_count > 0 :
		print("That's Incorrect. Lets try again. You have " + str(try_count) + " trys left")
		try_count -= 1
		return try_count
	else:
		print "----------------------\nYou have used all trys\
		\n    ** GAME OVER **   \n----------------------"
		return None

def word_replace (word, replacement_list,try_count):
	"""
    This function accepts user input to used to replace the blanks
    :inputs: word       - word from the string with blanks
    		 replacement_list - the replacement list for selected game level
    		 try_count  - No of trys allowed 
    :outputs: Returns the word. if found in replacement list then it contains 
    		  the replacement string or else it returns the same word
    """
	replace_done = ''
	replacement = word_in_replacement_list(word, replacement_list)
	if replacement != None:
		while True:
			user_input = raw_input("What to substitute for " + replacement + ": " +" ")
			if user_input != replacement_list[replacement]:
				try_count = try_check(try_count)
				if try_count != None:
					continue
				else:
					return replace_done,None
			else:
				word = word.replace(replacement, user_input)
				replace_done = 1
				break
	else:
		word  = word
	return replace_done,word

def check_if_number(try_input):
	"""
    This function checks if the string entered is a valid digit 
    and also checks if its within allowed range
    :inputs: try_input - number entered by user from command line
    :outputs: Returns the number or returns None. 
    """
	try_input_list = [1,2,3,4,5]
	if try_input and try_input.isdigit():
		if int(try_input) not in try_input_list:
			print "Error: Please enter digits between 1 and 5 ! Start Again!"
			return None
		else:
			return int(try_input) - 1
	else:
		print "Error: Not a valid number. Enter digits between 1 and 5 ! Start Again!"
		return None

	
def game (main_string, enter_level, replacement_list,try_count):
	"""
    This function proceeds through the game for selected level
    :inputs: main_string - string with blanks to be replaced
    	     enter_level - Game level selected in main
    	     replacement_list  - the replacement list for selected game level
    	     try_count   - No of trys allowed
    :outputs: Prints the string after every replacement 
    """
	print "The current paragraph for " +enter_level.upper()+ " reads as:\n"\
	 + main_string + "\n---------------------------------"
	replaced, build_string = [],[]
	main_string = main_string.split()
	build_string = deepcopy(main_string)
	for word in main_string:
		replace_done,word = word_replace (word,replacement_list,try_count)
		if word == None:
			return -1
		else:
			replaced.append(word)
			if replace_done == 1:
				offset = len(replaced)
				temp_string = replaced + build_string[offset:]
				print "--------------------------\nCORRECT! Replacement Done:\n"+ " ".join(temp_string)
	print "-----------------\n** YOU WIN !!! **\n-----------------\
	\nFINAL ANSWER:\n" + " ".join(replaced)
	return

# Main functions to start the game 
def main():
	"""
    This is the main function to start the quiz 
    :inputs: User selects desired game level and allowed number if worng guesses 
    :outputs: Runs the game if all inputs are valid 
    """
	enter_level,try_input = 0,0
	print "-------------------------------------\nLets play Fill-in-the-blanks Quiz !!!\n\
	Enter one of the following Levels: easy , medium or hard"
	enter_level = raw_input("Desired Level: ") 
	try_input = check_if_number(raw_input("Enter between 1 and 5 for the wrong guesses \
		do you want to allow before game over: " + " "))
	if try_input != None:
		if enter_level == 'easy':
			game (easy, enter_level, replacement_list_easy,try_input)
		elif enter_level == 'medium':
			game (medium, enter_level, replacement_list_medium,try_input)
		elif enter_level == 'hard':
			game (hard, enter_level, replacement_list_hard,try_input)
		else:
			print "Error: Invalid Level! Select from easy , medium or hard. Start Again!"
			return
	else:
		return

# Call to main
main()