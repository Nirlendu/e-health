# lcm

Takes in a list, and calculates the lcm.

**Usage**

```python
import lcm.lcm
sample_list = [1,2,3,4,5,6]
print lcm(sample_list)
```

**Logic**

First, we itirate over the list usin the logic `lcm(a, b, c) = lcm (a, lcm(b, c))`. Eventually, we will get the final value of LCM

We need to calculate GCD, the proceed to calculate LCM using the formula `a * b = lcm(a,b) * gcd(a,b)`.

Calculation of GCD can be done using `Euclid's Algorithm`, as it is fast and efficient.

Please refer : [Euclid's Algorithm Wikipedia Link](https://en.wikipedia.org/wiki/Euclidean_algorithm)

**Time Complexity**

O(N)

**Space Complexity**

O(1)