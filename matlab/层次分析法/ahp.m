%解决层次化分析
function [CR, w, m] = ahp(A)
    RI = [0 0 0.58 0.90 1.12 1.24 1.32 1.41 1.45 1.49 1.51];

    A = [1 1/2 4 3 3; 2 1 7 5 5; 1/4 1/7 1 1/2 1/3; 1/3 1/5 2 1 1; 1/3 1/5 3 1 1];
    [n, n] = size(A)
    [V, D] = eig(A);

    % 寻找最大特征值
    pos = 1;
    max = D(1, 1);

    for i = 1:n

        if (D(i, i) > max)
            max = D(i, i);
            pos = i
        end

    end

    %最大特征值对应的特征向量
    w = V(:, i);
    %归一化求权向量
    w = w / sum(w)

    %一致性检验

    CI = (max - n) / (n - 1);

    CR = CI / RI(n);
    m = max;

end
