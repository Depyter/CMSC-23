female(scarlet).
female(white).
female(peacock).
female(orchid).

male(plum). 
male(mustard).
male(green).

hates(scarlet, green).
hates(green, scarlet).
hates(plum, white).
hates(white, plum).
hates(mustard, plum).
hates(mustard, Person) :- female(Person).

likes(scarlet, orchid).
likes(peacock, orchid).
likes(orchid, peacock).
likes(scarlet, white).
likes(scarlet, plum).
likes(plum, scarlet).

likes(plum, Person) :- hates(mustard, Person).

enemies(X, Y) :- hates(X, Y), hates(Y, X).
friends(X, Y) :- likes(X, Y), likes(Y, X).
friends(X, Z) :- enemies(X, Y), enemies(Y, Z).