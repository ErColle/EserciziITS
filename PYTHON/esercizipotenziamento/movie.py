class Movie: 
    def __init__(self, movie_id: str, title: str, director: str, is_rented=False):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented
        
    def rent(self):
        if self.is_rented:
            raise Exception(f"Il film '{self.title}' è già noleggiato.")
        self.is_rented = True
            
    def return_movie(self):
        if not self.is_rented:
            raise Exception(f"Il film '{self.title}' non è stato noleggiato.")
        self.is_rented = False
        
    def get_movie(self):
        return self.movie_id, self.title, self.director, self.is_rented


class Customer: 
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name 
        self.rented_movies = [] 
    
    def rent_movie(self, movie: Movie): 
        if movie in self.rented_movies:
            raise Exception(f"Il film '{movie.title}' è già stato noleggiato da questo cliente.")
        self.rented_movies.append(movie)
        
    def return_movie(self, movie: Movie): 
        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
        else: 
            raise Exception(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")
        
    def get_customer(self):
        return self.customer_id, self.name
    
    def get_rented_movies(self):
        return self.rented_movies


class VideoRentalStore:
    def __init__(self):
        self.movies: dict[str, Movie] = {}      # chiave: movie_id
        self.customers: dict[str, Customer] = {}  # chiave: customer_id
        
    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id in self.movies: 
            raise ValueError(f"Il film con ID '{movie_id}' esiste già.") 
        self.movies[movie_id] = Movie(movie_id, title, director)
    
    def register_customer(self, customer_id: str, name: str):
        if customer_id in self.customers: 
            raise ValueError(f"Il cliente con ID '{customer_id}' esiste già.") 
        self.customers[customer_id] = Customer(customer_id, name)
        
    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]        
            movie = self.movies[movie_id]
            movie.rent()
            customer.rent_movie(movie)
        else: 
            raise ValueError("Cliente o film non trovato.")
    
    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:  
            customer = self.customers[customer_id]        
            movie = self.movies[movie_id]
            customer.return_movie(movie)
            movie.return_movie()
        else: 
            raise ValueError("Cliente o film non trovato.")
        
    def get_rented_movies(self, customer_id: str):
        if customer_id in self.customers:
            customer = self.customers[customer_id] 
            return customer.get_rented_movies()
        else: 
            raise ValueError("Cliente non trovato.")
