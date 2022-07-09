[x, y] = fmincon('fun1', rand(3, 1), [], [], [], [], zeros(3, 1), [], 'fun2');
% 'fun1'代表目标函数，rand(3, 1)随机给了x初值，zeros(3, 1)代表下限为0，即x1, x2, x3>=0, 'fun2'即刚才写的约束条件