class MovieCatalog: 
    '''

    attributi della classe MovieCatalog
    # self.catalog: dict[str, list[str]]
     
    '''
    
    # inizializzare un oggetto della classe MovieCatalog
    def __init__(self):
        self.setCatalog()
        
    # metodo str
    
    def __str__(self):
        return f"{self.catalog}"
    
    
    # metodi setter
    
    def setCatalog(self):
        self.catalog = {}
        
    # metodo getter    
    
    def getCatalog(self):
        return self.catalog
    
    # metodi della classe MovieCatalog
    
    # metodo che aggiunge una lista di film al catalogo
    def add_movie(self, director_name, movies):
        
        if not director_name: 
            print("Fornire un nome valido per il regista!")

        elif not movies:
            print("Fornire una lista di film che non sia vuota!")
        
        else: 
            if director_name in self.catalog:
                #  controlliamo se i film della lista movies siano gia stati inseriti dentro al catalogo
                for movie in movies:
                    if movie in self.catalog[director_name]:
                         print(f"Il film {movie} è gia presente nel catalogo!")
                    else: 
                        self.catalog[director_name].append(movie)
            
            # se il regista non è presente nel catalogo creare un nuovo record
            else: 
                self.catalog[director_name] = movies 
                
    def remove_movie(self,director_name, movie):
        if not director_name: 
            print("Fornire un nome valido per il regista!")

        elif not movie:
            print("Fornire una lista di film che non sia vuota!")
        
        else: 
            if director_name in self.catalog and movie in self.catalog[director_name]:
                
                # rimuovere il film dalla lista 
                self.catalog[director_name].remove(movie)
                
            # se la lista del film è vuota, rimuovi il regista dal catalogo     
            if not self.catalog[director_name]:
                del self.catalog[director_name]                      
                      