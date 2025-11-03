# Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
def sum_above_threshold(numbers: list[int], above: int) -> int:
    maggiori = 0
    for num in numbers: 
        if num > above: 
            maggiori += num
            
    return maggiori
