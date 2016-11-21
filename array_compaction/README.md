# array-compaction

Takes in a list, and returns the compact array with no duplicates

**Usage**

```python
import array_compaction.array_compaction
sample_list = [1,2,3,3,4,5,5,5,6]
print array_compaction(sample_list)
```

**Logic**

Since the array is already sorted, we just have to parse it sequentially maintaining an element which indicates the `last_unique_element`. If the `last_unique_element` encountered is same as the `current_element`, skip, as the current element is repeated. Otherwise, insert it to the `result_list` and update the `last_unique_element` with `current_element`.

**Time Complexity**

O(N)

**Space Complexity**

O(N)