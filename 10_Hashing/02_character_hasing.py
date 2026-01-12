'''

PROBLEM: We have given a string and we have to tell that how much time paricular element of list of alphabers are in the given string.



'''

def printOccurences(s:str, q:list[chr]) -> None:
    hash_dict = {}
    for character in s:
        if character in hash_dict:
            hash_dict[character] += 1
        else:
            hash_dict[character] = 1
    
    for character in q:
        if character in hash_dict:
            print(f'{character}: {hash_dict[character]}')
    

# printOccurences("aaaaaabcedgfws",["s","a","c","f"])


def printOccurences(s: str, q: list[chr]) -> None:
    hash_list = [0]*26
    for ch in s:
        index = ord(ch) - 97
        hash_list[index] += 1
    
    for ch in q:
        index = ord(ch) - 97
        print(f'{ch}: {hash_list[index]}')


printOccurences("aaaaaabcedgfws",["s","a","c","f"])   