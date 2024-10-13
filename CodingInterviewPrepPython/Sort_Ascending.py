from typing import List

from Basics.RangeFunctions import number

"""
Challenge
Implement the following functions:

sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns a new list of words sorted in ascending order.
sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns a new list of numbers sorted in ascending order.
sort_decimals(numbers: List[float]) -> List[float] - This function accepts a list of decimal numbers and returns a new list of decimal numbers sorted in ascending order.
Time and Space Complexity
The time complexity of the .sort() method is 
O(nlogn) O(nlogn), where n is the number of elements in the list.
The space complexity is O(n) O(n), where n is the number of elements in the list.
Note: Python uses the Timsort algorithm for sorting lists. Timsort is a hybrid sorting algorithm derived from merge sort and insertion sort. To learn more about sorting, check out the Data Structures and Algorithms for Beginners course.
"""

def sort_words(words: List[str]) -> List[str]:
     words.sort()
     return words
     pass

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort()
    return numbers
    pass

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort()
    return numbers
    pass



print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554,]))

"""Now if you want to use it in the desxending order we need to use the reverse key function """

from typing import List


def sort_words(words: List[str]) -> List[str]:
     words.sort(key= None, reverse=True)
     return words
     pass

def sort_numbers(numbers: List[int]) -> List[int]:
     numbers.sort(key=None, reverse=True)
     return numbers
     pass

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort(key=None, reverse=True)
    return numbers
    pass



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
