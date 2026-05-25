products_in_store = ['carrot', 'water', 'bread', 'milk', 'apple', 'butter']

word = input('What would you like to buy?  ')

for i in range(len(products_in_store)):
    if products_in_store[i] == 'word':
        print(f'Yes, we have {word}')

Guess the Secret Number
Write a program that has a secret number saved in a variable. Ask the user to enter a number. If the user guesses correctly, print a success message. If the number is wrong, print a message saying that the guess is incorrect.
Count Positive Numbers in a List
Write a program that has a list of numbers. Use a for loop to check every number in the list. Count how many numbers are positive, and print the final result.
Find the Longest Word
Write a program that has a list of words. Use a for loop to check every word in the list. Find the longest word and print it at the end.