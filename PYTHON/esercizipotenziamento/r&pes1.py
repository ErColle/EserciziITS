def calculateChanges(ore: float) -> float:
    costo: int = 0
    
    if ore <= 3: 
        
        costo = 2 
        return f"Hours: Charge:\n  {ore}    {costo}$"       
      
    elif ore >= 24:
        
        costo = 10 
        return f"Hours: Charge:\n  {ore}    {costo}$" 
        
    elif int(ore) - ore > 0: 
        
        costo += 1
        
    costo += ((int(ore) - 3)* 0.50) + 2     
    
    return f"Hours: Charge:\n  {ore}     {costo}$"   

print(calculateChanges(2))
        
    
     
    