function out = life(nbr)
%LIFE Conway's laws
%   OUT = LIFE(NBR) applies conway's laws to a pixel and its 3-by-3
%   neighborhood NBR
out = 0;
num = sum(nbr(:)) - nbr(2, 2);
if nbr(2, 2) == 1
    if num == 2 || num == 3
        out = 1;
    end
else
    if num == 3
        out = 1;
    end
end
