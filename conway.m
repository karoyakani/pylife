function out = conway(nhood)
live = nhood(2,2) == 1;
P = sum(nhood(:)) - nhood(2,2);  % number of live neighbors
out = (live && ((2 <= P) && (P <= 3))) || (~live && (P == 3));

