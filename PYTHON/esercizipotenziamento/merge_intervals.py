def merge_intervals(intervals: str) -> str:
    for couple in intervals:
        
        indice = intervals[couple].index()
        new_list = []  
        
        if couple[1] == intervals[indice][0]:        
    
intervals = [[1, 4], [4, 5]]
merge_intervals(intervals) # restituisce [[1, 5]]