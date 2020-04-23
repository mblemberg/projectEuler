%Project Euler problem 9

% A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

% a2 + b2 = c2
% For example, 32 + 42 = 9 + 16 = 25 = 52.

% There exists exactly one Pythagorean triplet for which a + b + c = 1000.
% Find the product abc.

pkg load symbolic

syms a b c real

f1 = a^2 + b^2 == c^2;
f2 = a + b + c == 1000;

[a, b] = solve(f1, f2, a, b)

fa = function_handle(a(1));
fb = function_handle(a(2));

for c=200:499;
  if isreal(fa(c)) && isreal(fb(c)) && (round(fa(c))^2+round(fb(c))^2 == c^2)
    display(["abc = " num2str(fa(c)*fb(c)*c)]);
  endif
endfor

% abc = 31875000