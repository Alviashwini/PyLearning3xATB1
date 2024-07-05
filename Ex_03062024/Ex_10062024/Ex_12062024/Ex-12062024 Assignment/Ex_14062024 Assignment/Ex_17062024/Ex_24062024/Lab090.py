# filter the vowels
# a,e,i,o,u
letters_list = ['a', 'b', 'c', 'd', 'e', 'i', 'o', 'u']
letters_tuple = ('a', 'b', 'c', 'd', 'e', 'i', 'o', 'u')
letters_set = ('a', 'b', 'c', 'd', 'e', 'i', 'o', 'u')
def filter_vowel(letters):
    vowel = ['a', 'e', 'i', 'o', 'u']
    return letters in vowel


# result = filter_vowel("i")
# print(result)
# to get all the vowels
filtered_words = filter(filter_vowel, letters_list)
print(list(filtered_words))
