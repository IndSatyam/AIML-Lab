el(X,[X|L],L).
el(X,[_|L],R) :- el(X,L,R).
selectN(0,_,[]) :- !.
selectN(N,L,[X|S]) :- N > 0,
el(X,L,R),
N1 is N-1,
selectN(N1,R,S).
subsets([],[],[],[]).
subsets(G,[N1|Ns],[G1|Gs],[]) :-
selectN(N1,G,G1),
subtract(G,G1,R),
subsets(R,Ns,Gs,[]).
