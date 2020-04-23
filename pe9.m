pkg load symbolic

syms a b c real

f1 = a^2 + b^2 == c^2;
f2 = a + b + c == 1000;

[a, b] = solve(f1, f2, a, b)

fa = function_handle(a(1));
fb = function_handle(a(2));


c = 1:500;

plot(c, fa(c), 'r');
hold on;
plot(c, fb(c), 'b');
plot(c, c, 'k');
plot(c, fa(c)+fb(c)+c, 'k--');

for c=200:499;
  if isreal(fa(c)) && isreal(fb(c)) && (round(fa(c))^2+round(fb(c))^2 == c^2)
    display(["abc = " num2str(fa(c)*fb(c)*c)]);
  endif
endfor

% abc = 31875000