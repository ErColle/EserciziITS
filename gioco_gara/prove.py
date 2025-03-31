# ostacolo = [
#     "██",
#     "██\n"
# ]

# print(*ostacolo)

import time 
import random
import os

timer = 1
ambiente = ""
counter = 0

while True:
    
    print(counter)
    counter += 1
     
    """ if timer % 10 == 0:
        numero = random.randint(1, 10)
                
        if numero >= 3:
            ambiente = "Soleggiato"
            
        else:
            ambiente = "Piovoso"
    
    print(ambiente) """
    
    time.sleep(0.2)
    
    timer += 1