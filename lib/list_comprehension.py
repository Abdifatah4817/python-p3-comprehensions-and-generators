#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if num % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]


# Example usage:
numbers = [0,1,2,3,4,5,6,7,8]
print(return_evens(numbers)) 
# Output: [0, 2, 4, 6, 8] 

sentences = ["Hello", "I'm doing great", "Python is fun"]
print(make_exclamation(sentences))
# Output: ['Hello!', "I'm doing great!", 'Python is fun!']
