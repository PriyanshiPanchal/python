        

inp = input('input a character : ');


def display(): 
    n=7; 
    for i in range(n): 
  
        for j in range((n // 2) + 1): 
            if ((j == 0 or j == n // 2) and i != 0 or
  
                i == 0 and j != 0 and j != n // 2 or
  
                i == n // 2): 
                print("*", end = "") 
            else: 
                print(" ", end = "")   
        print();

def print_pattern():
    n=6;
    for i in range(n):
        for j in range(n + 1):
            if ((j == 0 or j == n) or
                    i == 0 and j != 0 and j != n or
                    i == n - 1 or
                    i == n // 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_c():
    for row in range(7):
        for col in range(5):
            if(col==0) or ((row==0 or row==6) and (col>0)):
                print("*",end="")
            else:
                print(end="")
        print()
b ={
    'a' : display(),
    'b' : print_pattern(),
    'c' : print_c()
}
b.get(inp)


