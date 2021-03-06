# Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules

# Both players are given the same string,S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels. 
# The game ends when both players have made all possible substrings. 

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

# Input Format
# A single line of input containing the string S. 
# Note: The string S will contain only uppercase letters:[A - Z].

# Output Format
# Print one line: the name of the winner and their score separated by a space.
# If the game is a draw, print Draw.

# Sample Input
# BANANA

# Sample Output
# Stuart 12
def minion_game(string):
    # your code goes here
    stuart=0
    kevin=0
    vowels="AEIOU"
    for i in range(len(string)):
        if string[i] in vowels:
            # kevin+=len(string[i:])
            kevin+=len(string)-i
        else:
            # stuart+=len(string[i:])
            stuart+=len(string)-i
    if kevin==stuart:
        print("Draw")
    elif stuart > kevin:
        print("Stuart",stuart)
    else:
        print("Kevin",kevin)         
    

if __name__ == '__main__':
    s = input()
    minion_game(s)