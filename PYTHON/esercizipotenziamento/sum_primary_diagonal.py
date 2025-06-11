def sum_primary_diagonal(matrix:list ) ->int:
    
    elements_addict = 0
    i = 0
    
    for list in matrix: 
        
        elements_addict += list[i] 
        i += 1        

    
    return elements_addict

def sum_secondary_diagonal(matrix:list ) ->int:
    
    elements_addict = 0
    i = -1
    
    for list in matrix: 
        
        elements_addict += list[i] 
        i += 1        

    
    return elements_addict

print(sum_primary_diagonal([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]))

print(sum_secondary_diagonal([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]))
        