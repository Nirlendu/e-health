# array-rotation

Takes in a list, and rotates the array with given n

Usage

```python
import array_rotation.rotate
sample_list = [1,2,3,3,4,5,5,5,6]
rotate_n = 4
print rotate(sample_list, rotate_n)
```

**Logic**

First we caliberate the value of `n` to account for `Right Side Rotations` and cases where `n > len(array)`

Then, we split the array into two parts based on the calculated value of `n`. Then we merge the arrays again, but in reverse order.

**Time Complexity**

O(N)

**Space Complexity**

O(1)