string = open('text.txt', 'r').read()

string = string.lower();  
count=0
words = string.split(" ");  
list=[]
print("Duplicate words in a given string : ");  
for i in range(0, len(words)):  
    count = 1;  
    for j in range(i+1, len(words)):  
        if(words[i] == (words[j])):  
            count = count + 1;  
            words[j] = "0";  

    if(count > 1 and words[i] != "0"):  
         list.append(words[i])
         res=print(words[i],count);  
        
print(list)

