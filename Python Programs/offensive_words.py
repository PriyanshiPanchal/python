import re

string = open('text.txt', 'r').read()
string = string.lower();  
mystring= re.sub('-.,;', ' ', string)
# print(mystring)
input_text=mystring.split(' ')
# print(input_text)

# lines=['python', 'is', 'an', 'interpreted,', 
#         'high-level,', 'general-purpose', 'programming', 'language.',
#          'created', 'by', 'guido', 'van', 'rossum', 'and', 'first',
#           'released', 'in', '1991,', "python's", 'design', 'philosophy',
#            'shit', 'emphasizes', 'code', 'bastard', 'readability', 'with', 'its', 'notable', 'use', 'of',
#             'significant', 'whitespace', 'python', 'slut', 'is', 'the', 'emphasizes']
# lines = ['this is go:od', 
#             'that example is bad', 
#             'amp is a word']

stop_words = ['bitch', 'shit', 'slut']
for x in stop_words:
    if x not in input_text:
        stop_words.remove(x)
print(set(stop_words))

# results = []
# for text in input_text:
#     for stop_word in stop_words:
#             for x in range(0, len(input_text)):
#                if input_text[x] == stop_word:
#                   input_text[x] = ''
#                   results.append(input_text)

# print(results)