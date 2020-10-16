string = open('text.txt', 'r').read()

input_text=[]
words = string.lower();  
def Convert(string): 
    li = list(string.split(" ")) 
    input_text.append(li)
    return li 
Convert(words) 
print(input_text)

lines=['python', 'is', 'an', 'interpreted,', 
        'high-level,', 'general-purpose', 'programming', 'language.',
         'created', 'by', 'guido', 'van', 'rossum', 'and', 'first',
          'released', 'in', '1991,', "python's", 'design', 'philosophy',
           'shit', 'emphasizes', 'code', 'bastard', 'readability', 'with', 'its', 'notable', 'use', 'of',
            'significant', 'whitespace', 'python', 'slut', 'is', 'the', 'emphasizes']
# lines = ['this is go:od', 
#             'that example is bad', 
#             'amp is a word']

stop_words = ['bitch', 'shit', 'slut']
results = []
for text in lines:
    tmp = text.split(' ')
    for stop_word in stop_words:
            for x in range(0, len(tmp)):
               if tmp[x] == stop_word:
                  tmp[x] = ''
    results.append(" ".join(tmp))

print(results)

