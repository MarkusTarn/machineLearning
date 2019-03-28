%--------------------------- Prolog: ---------------------------
% Knowledge base in Prolog

% Author: Markus Tarn
% --------------------------------------------------------------

% -- Facts:--
date(2019).

man(marcus).
man(jaan).
man(francesco).
man(vambola).
man(hose).

lives(marcus, pompej).
lives(francesco, pompej).
lives(vambola, pompei).
lives(hose, tallinn).

born(marcus, 40).
born(jaan, 1977).
born(francesco, 1989).
born(vambola, 1920).
born(hose, 1720).


% -- Predicates:--
mortal(Person) :-
    man(Person).

deceased_by_volcano(Person) :-
    mortal(Person),
    born(Person, Year),
    lives(Person, pompej),
    Year<79.

deceased_by_age(Person) :-
    mortal(Person),
    born(Person, Year),
    date(Today),
    Year+150<Today.

deceased(Person) :-
    (   deceased_by_age(Person)
    ;   deceased_by_volcano(Person)
    ).

alive(Person) :-
    mortal(Person),
    \+ deceased(Person).


% -- Queries:--
% alive(marcus).
% alive(jaan).
% alive(francesco).
% alive(vambola).
% alive(hose).