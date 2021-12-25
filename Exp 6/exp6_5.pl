huffman(Fs,Cs) :-
 initialize(Fs,Ns),
 make_tree(Ns,T),
 traverse_tree(T,Cs).
initialize(Fs,Ns) :- init(Fs,NsU), sort(NsU,Ns).
init([],[]).
init([fr(S,F)|Fs],[n(F,S)|Ns]) :- init(Fs,Ns).
make_tree([T],T).
make_tree([n(F1,X1),n(F2,X2)|Ns],T) :-
 F is F1+F2,
 insert(n(F,s(n(F1,X1),n(F2,X2))),Ns,NsR),
 make_tree(NsR,T).
insert(N,[],[N]) :- !.
insert(n(F,X),[n(F0,Y)|Ns],[n(F,X),n(F0,Y)|Ns]) :- F < F0, !.
insert(n(F,X),[n(F0,Y)|Ns],[n(F0,Y)|Ns1]) :- F >= F0, insert(n(F,X),Ns,Ns1).
traverse_tree(T,Cs) :- traverse_tree(T,'',Cs1-[]), sort(Cs1,Cs), write(Cs).
traverse_tree(n(_,A),Code,[hc(A,Code)|Cs]-Cs) :- atom(A).
traverse_tree(n(_,s(Left,Right)),Code,Cs1-Cs3) :-
 atom_concat(Code,'0',CodeLeft),
 atom_concat(Code,'1',CodeRight),
 traverse_tree(Left,CodeLeft,Cs1-Cs2),
 traverse_tree(Right,CodeRight,Cs2-Cs3).
