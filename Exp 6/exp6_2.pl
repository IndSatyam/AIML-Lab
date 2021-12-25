rle([],[]).
rle([X],[X]).
rle([X, X|REMAINING],OUTPUT) :- rle([X|REMAINING],OUTPUT).
rle([X, Y|REMAINING], [X|OUTPUT_TAIL]) :- X \= Y, rle([Y|REMAINING],OUTPUT_TAIL).
