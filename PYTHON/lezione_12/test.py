from esercizio_12_1 import MovieCatalog

# creare un oggetto della MovieCatalog
catalog: MovieCatalog = MovieCatalog()

# aggiungiamo un regista e dei film al catalogo
catalog.add_movie('Steven Spielberg', ['Casper', 'Ritorno al futuro'])

# print(catalog.getCatalog())

#aggiungere un altro film di steven spielberg al catalog  
catalog.add_movie('Steven Spielberg', ['Et'])

print(catalog.getCatalog())

# aggiungere un nuovo regista 
catalog.add_movie('Mario Rssi', ['Che bel cielo', 'La tempesta pazza'] )

print(catalog.getCatalog())

# rimuovere un film "ET" dal catalogo 
catalog.remove_movie('Steven Spielberg', 'Et')
catalog.remove_movie('Steven Spielberg', 'Ritorno al futuro')
catalog.remove_movie('Steven Spielberg', 'Casper')

print(catalog.getCatalog())