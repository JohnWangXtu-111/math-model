f = [-1; -1]

A = [14 9;-6 3]
b = [51; 1]

lb = [0; 0]
ub = [Inf, Inf]

[x, fval] = intlinprog(f, [1, 2], A, b, [], [], lb, ub)