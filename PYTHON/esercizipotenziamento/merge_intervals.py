def merge_intervals(intervals):
    
    couple: list = [] 
    new_list = [] 
    
    for i in range(len(intervals) - 1):
        
        if intervals[i]  != intervals[-1]:
            
            if intervals[i][1] >= intervals[i + 1][0]:
                
                couple = [intervals[i][0], intervals[i +1][1]]
                
                del intervals[i], intervals[i + 1]  
                
                new_list.append(couple) 
            
            else:
                new_list.append(intervals[i]) 
        
        return new_list
            
                    
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(merge_intervals(intervals)) # restituisce [[1, 5]]