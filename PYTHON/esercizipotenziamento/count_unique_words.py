import string

def count_unique_words(text: str) -> dict:
    tokens = text.split()
    clean_tokens = []
    dizionario_tokens = {} 
    
    for token in tokens:
        parola = token.strip(string.punctuation).lower()
        
        if token: 
            clean_tokens.append(parola)
        
    for token in clean_tokens:
        
        if token in dizionario_tokens:
            dizionario_tokens[token]  += 1 
            
        else:
            
            dizionario_tokens[token] = 1 

    return dizionario_tokens
    
    
print(count_unique_words("Hello, world! Hello... PYTHON? world."))
    