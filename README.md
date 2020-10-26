# Python_std_algorithm

This project is a pure python implementation of the [algorithm header](https://en.cppreference.com/w/cpp/algorithm) from the C++ standard template library (STL for short).



## Installation
A pypi package will be available soon
## How to use

All functions live in the ```std``` namespace, you can import it with ```import std``` and then call the functions like this: ```std.all_of()```

## Implemented functions

The list of functions is taken from https://en.cppreference.com/w/cpp/algorithm

When a function's checkbox is ticked, it is implemented by this library.

When a function's checkbox is NOT ticked, it is not implemented. A comment states a reason why the function can not be implemented properly.

<details> <summary>Click to expand!</summary>
<p>

### Non-modifying sequence operations

- [x] all_of
- [x] any_of
- [x] none_of


- [x] for_each
- [x] for_each_n

- [x] count
- [x] count_if
- [x] count_if_not ***Not implemented in STL, but seems fitting***

- [x] mismatch

- [ ] find
- [ ] find_if
- [ ] find_if_not
- [ ] find_end
- [ ] find_first_of
- [ ] adjacent_find


- [ ] search
- [ ] search_n

### Modifying sequence operations

- [ ] copy
- [ ] copy_if
- [ ] copy_n
- [ ] copy_backward


- [ ] move
- [ ] move_backward


- [ ] fill
- [ ] fill_n


- [ ] transform


- [ ] generate
- [ ] generate_n


- [ ] remove
- [ ] remove_if
- [ ] remove_copy
- [ ] remove_copy_if


- [ ] replace
- [ ] replace_if
- [ ] replace_copy
- [ ] replace_copy_if


- [ ] swap
- [ ] swap_ranges
- [ ] iter_swap


- [ ] reverse
- [ ] reverse_copy


- [ ] rotate
- [ ] rotate_copy


- [ ] shift_left
- [ ] shift_right


- [ ] random_shuffle
- [ ] shuffle


- [ ] sample


- [ ] unique
- [ ] unique_copy

### Partitioning operations

- [ ] is_partitioned


- [ ] partition
- [ ] partition_copy


- [ ] stable_partition


- [ ] partition_point

### Sorting operations

- [ ] is_sorted
- [ ] is_sorted_until


- [ ] sort
- [ ] partial_sort
- [ ] partial_sort_copy
- [ ] stable_sort
- [ ] nth_element

### Binary search operations (on sorted ranges)

- [ ] lower_bound
- [ ] upper_bound


- [ ] binary_search


- [ ] equal_range

### Other operations on sorted ranges

- [ ] merge
- [ ] implace_merge

### Set operations (on sorted ranges)

- [ ] includes


- [ ] set_difference
- [ ] set_intersection
- [ ] set_symmetric_difference
- [ ] set_union

### Heap operations

- [ ] is_heap
- [ ] is_heap_until


- [ ] make_heap


- [ ] push_heap


- [ ] pop_heap


- [ ] sort_heap

### Minimum/maximum operations

- [ ] max
- [ ] max_element
- [ ] min
- [ ] min_element
- [ ] minmax
- [ ] minmax_element


- [ ] clamp

### Comparison operations

- [ ] equal


- [ ] lexicographical_compare
- [ ] lexicographical_compare_threeway

### Permutation operations

- [ ] is_permutation


- [ ] next_permutation
- [ ] prev_permutation
</p>
</details>

## Contributing

First of all, thanks a lot for your contribution, any form of contribution is very welcome and appropriated!

Please familiarise yourself with this project's [code of conduct](CODE_OF_CONDUCT.md) and [contribution guidelines](CONTRIBUTING.md).

## Getting help

1. Read the docs
2. Get in touch with other contributors at [gitter](https://gitter.im/python_std_algorithm/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
2. If you think you found a bug, or documentation could be improved, please open an issue

## License
Copyright (C) 2020 [Jonas Muehlmann](https://github.com/JonasMuehlmann)
 
The project is licensed under the terms of the GPL-V3 license, you can view it [here](LICENSE.md).