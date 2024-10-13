"""
Here the key thing is that the word key is explained, key basically means the key needs to be reached out with
individual values from the list and we can sort the thing in the basis of the value of key, which can be the length of the word
or the absoulte value, it can also be  alot of different things here in the4 two examples we have written the key function
for 1) representing a group of string in the descending order according to the length of word present int the given list
for 2) The second group is based in the value of their absolute numbers, so the key basically takes account of the value and
it just does not care what is in the list rather with the help of the function that we make it takes account value of each
values in the list that changes from the function we create, it takes the value and it gives certain output from that value
which will be considered for sorting. This phenomenon of sorting is Called CUSTOM SORTv :) Happy coding
"""

from typing import List

def get_word_length(word:str) -> int:
    return len(word)

def get_abs_value(number: int)->int:
    return abs(number)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key = get_word_length, reverse =True)
    return words
    pass



def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key = get_abs_value, reverse=False)
    return numbers
    pass


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
