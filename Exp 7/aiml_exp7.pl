city(C) :-
    length(C,5),
    % CITY NAMES
    member(h('Last Stand',_,_),C),
    member(h('Mile City',_,_),C),
    member(h('New Town',_,_),C),
    member(h('Olliopolis',_,_),C),
    member(h('Polberg',_,_),C),
   
    % CITY REGIONS
    member(h(_,'mountains',_),C),
    member(h(_,'forest',_),C),
    member(h(_,'coast',_),C),
    member(h(_,'desert',_),C),
    member(h(_,'valley',_),C),
   
    % RAINFALL AMOUNTS
    member(h(_,_,12),C),
    member(h(_,_,27),C),
    member(h(_,_,32),C),
    member(h(_,_,44),C),
    member(h(_,_,65),C),
   
    % FACTS
   
    % The city in the desert got the least rain;
    % the city in the forest got the most rain.
    member(h(_,'desert',12),C),
   
    % New Town is in the mountains.
    member(h('New Town','mountains',_),C),
   
    % Last Stand got more rain than Olliopolis.
    member(h('Last Stand',_,A),C),
    member(h('Olliopolis',_,B),C),
    A>B,
   
    % Mile City got more rain than Polberg,
    % but less rain than New Town.
    member(h('Mile City',_,D),C),
    member(h('Polberg',_,E),C),
    member(h('New Town',_,F),C),
    D>E,
    D<F,
   
    % Olliopolis got 44 inches of rain.
    member(h('Olliopolis',_,44),C),
   
    % The city in the mountains got 32 inches of rain;
    % the city on the coast got 27 inches of rain.
    member(h(_,'mountains',32),C),
    member(h(_,'coast',27),C).

get_city_rain(City, Rainfall):-
    city(C),
    member(h(City,_,Rainfall),C),
    write(City),write(" has received "),write(Rainfall),write(" inches"),nl.

get_city_region(City, Region):-
    city(C),
    member(h(City,Region,_),C),
    write(City),write(" is in "),write(Region),write(" region"),nl.