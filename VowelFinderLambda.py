## Author: Feras
## Problem: Lambda Expression to return vowels in a string

vowelFinder = lambda string : [i for i in string if i in "aeoiuAEIOU"]
print(vowelFinder("azcbobAuIobegghakl"))