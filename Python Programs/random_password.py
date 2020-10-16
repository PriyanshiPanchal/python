import random
import string
import numpy as np

N=np.random.randint(8,16)
list1=[random.choice(string.digits) for _ in range(2)]
list2=[random.choice(string.ascii_uppercase) for _ in range(2)]
list3=[random.choice(string.ascii_lowercase) for _ in range(2)]
list4=[random.choice(string.punctuation) for _ in range(2)]
joined_list= list1 + list2 + list3 + list4
random.shuffle(joined_list)
print(''.join(joined_list))    
