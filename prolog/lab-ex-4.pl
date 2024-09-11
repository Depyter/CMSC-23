female('Scarlet').
female('Mrs. White').
female('Mrs. Peacock').
female('Dr. Orchid').

male('Prof. Plum'). 
male('Colonel Mustard').
male('Green').

hates('Scarlet','Green').
hates('Green','Scarlet').
hates('Prof. Plum','Mrs. White').
hates('Mrs. White','Prof. Plum').
hates('Colonel Mustard','Prof. Plum').
hates('Colonel Mustard', Person) :- female(Person).

likes('Scarlet','Dr. Orchid').
likes('Mrs. Peacock','Dr. Orchid').
likes('Dr. Orchid', 'Mrs. Peacock').
likes('Scarlet','Mrs. White').
likes('Scarlet','Prof. Plum').
likes('Prof. Plum', ' Scarlet').

likes('Prof. Plum', Person) :- hates('Colonel Mustard', Person).
enemies(X, Y) :- hates(X, Y), hates(Y, X).
friends(X, Y) :- likes(X, Y), likes(Y, X).
friends(X, Z) :- enemies(X,Y), enemies(Y,Z).