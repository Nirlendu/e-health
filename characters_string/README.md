# characters-string

Takes in two lists, and returns a list of common elements sorted in order of occurence in the first list. Implemented as two methods, one having linear time complexity, and one having non-linear.

**Usage**

```python
first_list = [1,2,3,3,4,5,5,5,6]
second_list = [1,6,5,5]
import characters-string.unique_elements_non_linear
print unique_elements_non_linear(first_list, second_list)
import characters-string.unique_elements_linear
print unique_elements_linear(first_list, second_list)
```

**Logic**

`unique_elements_non_linear`

First, we get a list of common elements using `sets`. Then we parse the first array, and if the current element is present is `common_elements_list`, append it to the `result_list`

`unique_elements_linear`

We use `collection.OrderedDict` for this, as this stores the dictionary keys in order of appearance. 

First we parse the `first_array`, and if `current_element` is not present as a `key` in `reference_dict`, it means the element is encountered first time. Put it as `key` in `reference_dict` and update the `value` as `False`. If `current_element` is present as `key`, then the `current_element` is duplicated and we have to skip. 

Then we parse the `second_array`, and if `current_element` is not present as a `key` in `reference_dict`, it means the element is encountered first time. Skip as we don't need elements unique to `second_array`. If `current_element` is present as `key`, then `current_element` is common to both, and update the `value` tp `True`.

At last, parse the `reference_dict` and for each `value` as `True`, append the `key` to `result_list`. Time is linear in this as we parse the `first_array`, `second_array` and `reference_dict` once each. Key search in `reference_dict` takes O(1) time.

**Time Complexity**

unique_elements_non_linear -- O(N*N)

unique_elements_linear -- O(N)

**Space Complexity**

unique_elements_non_linear -- O(N)

unique_elements_linear -- O(N)