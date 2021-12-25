parent(pandu, arjun).
parent(pandu, bheem).
parent(pandu, nakul).

parent(kunti, arjun).
parent(kunti, bheem).
parent(madri, nakul).

parent(arjun, abhimanyu).
parent(subhadra, abhimanyu).

parent(arjun, pragati).
parent(abhimanyu, parikshit).

female(kunti).
female(madri).
female(subhadra).
female(pragati).

male(pandu).
male(parikshit).
male(arjun).
male(bheem).
male(nakul).
male(abhimanyu).

mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).

son(X, Y) :- parent(Y, X), male(X).
daughter(X, Y) :- parent(Y, X), female(X).

grandfather(X, Y) :- parent(X, A), parent(A, Y), male(X).
grandmother(X, Y) :- parent(X, A), parent(A, Y), female(X).


sister(X, Y) :- parent(A, X), parent(A, Y), female(X), X\=Y.
brother(X, Y) :- parent(A, X), parent(A, Y), male(X), X\=Y.

aunt(X, Y) :- sister(X, A), parent(A, Y).
uncle(X, Y) :- brother(X, A), parent(A, Y).

predecessor(X, Y) :- parent(X, Y).
predecessor(X, Y) :- parent(X, A), predecessor(A, Y).

successor(X, Y) :- son(X, Y), X\=Y.
successor(X, Y) :- daughter(X, Y), X\=Y.
successor(X, Y) :- son(A, X), successor(A, Y).
successor(X, Y) :- daughter(A, X), successor(A, Y).
