-- tipi di dato

create Strutturato type enum (’Ricercatore’, ’Professore Associato’, ’Professore Ordinario’);

create LavoroProgetto type enum (’Ricerca e Sviluppo’, ’Dimostrazione’, ’Management’, ’Altro’);

create LavoroNonProgettuale type enum (’Didattica’, ’Ricerca’, ’Missione’, ’Incontro Dipartimentale’, ’Incontro Accademico’, ’Altro’);

create CausaAssenza type enum (’Chiusura Universitaria’, ’Maternita’, ’Malattia’);

create domain PostInteger as Integer
	check (value >= 0);

create domain StringaM as varchar(100);

create domain NumeroOre as Integer
	check (value >= 0 and value <= 8 );

create domain Denaro as real
	check (value >= 0);

-- crezione tabelle

create table Persona (
	id PostInteger not null,  
	nome StringaM not null, 
	cognome StringaM not null, 
	posizione Strutturato not null,
	stipendio Denaro not null,
	primary key(id)
);


create table Progetto (
	id PostInteger primary key, 
	nome StringaM not null, 
	inizio date not null, 
	fine date not null,
	budget Denaro not null,
	unique (nome),
	check (inizio < fine )
);

create table WP (
	progetto PostInteger not null, 
	id PostInteger, 
	nome StringaM,
	inizio date not null, 
	fine date not null,
	check ( inizio < fine ),
	unique (progetto, nome),
	foreign key (progetto) references Progetto(id),
	primary key(id)
);

create table AttivitaProgetto(
	id PostInteger primary key,
	persona PostInteger not null,
	progetto PostInteger not null,
	wp PostInteger not null,
	giorno date not null,
	tipo LavoroProgetto not null,
	oreDurata NumeroOre not null,
	foreign key (persona) references Persona(id),
	foreign key (progetto, wp) references WP(progetto, id)
);

create table AttivitaNonProgettuale(
	id PostInteger primary key,
	persona PostInteger not null,
	giorno date not null, 
	tipo LavoroNonProgettuale not null,
	oreDurata NumeroOre not null, 
	foreign key	(persona) references Persona(id)
);

create table Assenza(
	id PostInteger primary key,
	persona PostInteger not null,
	tipo CausaAssenza not null,
	giorno date not null,
	unique(persona, giorno),
	foreign key (persona) references Persona(id)
);




