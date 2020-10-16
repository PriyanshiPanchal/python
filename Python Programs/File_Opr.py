file1 = open("text.txt","r")  
print (file1.readlines()) 

def Check_Vow(string, vowels): 
    count = {}.fromkeys(vowels,0)
    # count the vowels
    for char in string:
        if char in count:
             count[char] += 1
    print(count)

    final = [each for each in string if each in vowels] 
    print(len(final)) 
      
# Driver Code 

string = open('text.txt', 'r').read()
vowels = "AeEeIiOoUu"
Check_Vow(string, vowels);