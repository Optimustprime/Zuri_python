# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if(sorted(word)== sorted(anagram)):
        result=True
    else:
        result=False
    return result
word=input("Enter first word: ")
anagram=input("Enter Second word: ")
result=find_anagram(word,anagram)
print(result)
print(find_anagram("hello","check"))
print(find_anagram("below","elbow"))