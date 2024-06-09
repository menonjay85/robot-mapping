x = -10:0.1:10;
y = x.^2;
plot(x, y);
title('Plot of f(x) = x^2');
xlabel('x');
ylabel('f(x)');
saveas(gcf, 'plot_f.png');
