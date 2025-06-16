with open("PYTHON/lezione_14/example.txt", mode="w", encoding="utf-8") as file:  
    
    message: str = "Hello world!\n"
    written_char: int = file.write(message)
    print(f"Written charachters: {written_char}")