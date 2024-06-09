% Part a
normal_random_numbers = normrnd(5.0, 2.0, [1, 100000]);

% Part b
uniform_random_numbers = rand(1, 100000) * 10;

% Part c
mean_normal = mean(normal_random_numbers);
std_normal = std(normal_random_numbers);

mean_uniform = mean(uniform_random_numbers);
std_uniform = std(uniform_random_numbers);

fprintf('Normal: mean = %.2f, std = %.2f\n', mean_normal, std_normal);
fprintf('Uniform: mean = %.2f, std = %.2f\n', mean_uniform, std_uniform);

% Part d
figure;
subplot(1, 2, 1);
hist(normal_random_numbers, 50);
title('Histogram of Normally Distributed Random Numbers');

subplot(1, 2, 2);
hist(uniform_random_numbers, 50);
title('Histogram of Uniformly Distributed Random Numbers');

saveas(gcf, 'random_numbers_histograms.png');

