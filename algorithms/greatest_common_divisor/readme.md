# Greatest Common divisor of two non-negative integers (Euclidean Algorithm)
Given two non-negative integers (of which both are not 0), GCD is the largest integer that divides both of them.

There is a naive way of finding all common divisors for both integers and then find the maximum of that.

Let's consider `gcd(x, y)` to be a function that returns GCD of `x` and `y` and `x > y`.

For any given `x` and `y`, we can write `x` as `ay + b` where `a` and `b` are integers. Now whatever divides `y` will always divide `ay` as well. So to find the GCD, we can only compare `b` and `y`. Now `y` is our larger number and `b` is the smaller one. If we keep on repeating this, we end up with smaller number as 0 and the larger number as GCD.

eg. x = 1344 and y = 217

So `gcd(1344, 217) = gcd(6 * 217 + 42, 217) = gcd(217, 42) = (5 * 42 + 7, 42) = gcd(42, 7) = gcd(6 * 7 + 0, 7) = gcd(7, 0)`

In general terms, we replace the larger number with remainder obtained by dividing larger number by smaller one.

PS: In case we enter smaller number first, it takes one extra step to automatically sort this by logic that smaller number is `0` times larger number plus the smaller number. Take above example:

`gcd(217, 1344) = gcd(0 * 1344 + 217, 1344) = gcd(1344, 217)` -> which is now in order as above.

## Run it yourself
This code uses Python 3. There are two algorithms mentioned here, naive and fast. Both can be executed from terminal as:

`python3 <filename.py>`
