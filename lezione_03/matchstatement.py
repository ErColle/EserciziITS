#MATCH STATEMENT

posizione = int(input("Inserisci la posizione: "))

# if posizione == 1:
#     print(f"{posizione}st")
# elif posizione == 2:
#     print(f"{posizione}nd")
# elif posizione == 3:
#     print(f"{posizione}rd")
# else:
#     print(f"{posizione}th")
    

match posizione:
    case 1:
        print(f"{posizione}st")
    case 2:
        print(f"{posizione}nd")
    case 3:
        print(f"{posizione}rd")
    case _:
        print(f"{posizione}th")

