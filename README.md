# PyAoI (Python Algorithms on Iterables)

[![Join the chat at https://gitter.im/pyaoi/community](https://badges.gitter.im/pyaoi/community.svg)](https://gitter.im/pyaoi/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Build Status](https://travis-ci.com/JonasMuehlmann/pyaoi.svg?branch=master)](https://travis-ci.com/JonasMuehlmann/pyaoi) ![img](https://img.shields.io/badge/semver-2.0.0-green) [![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

This project provides a bunch of functions to interact with iterables, it is inspired by
the [algorithm header](https://en.cppreference.com/w/cpp/algorithm) from the C++ standard template library (STL for
short).

## Installation

```pip install pyaoi```

## How to use

All functions live in the ```pyaoi``` namespace, you can import it with ```import pyaoi``` and then call the functions
like this: ```pyaio.all_of()```

## Implemented functions

The following list shows planned functions and whether they are implemented yet. Feel free to make a PR for a listed
function's implementation. This list is subject to change at any time.
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

- [x] mismatch

- [x] find
- [x] find_if
- [x] find_end
- [x] find_first_of
- [x] adjacent_find


- [x] search
- [x] search_n

### Modifying sequence operations

- [ ] copy_replace
- [ ] copy_replace_if
- [ ] copy_replace_if_not
  
- [ ] copy_except
- [ ] copy_except_if
- [ ] copy_except_if_not


- [ ] fill
- [ ] fill_n


- [ ] transform


- [ ] remove
- [ ] remove_if

- [ ] replace
- [ ] replace_if


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

- [ ] max_index
- [ ] min_index
- [ ] minmax
- [ ] minmax_index


- [ ] clamp

### Comparison operations

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
2. Get in touch with other contributors
   at [gitter](https://gitter.im/pyaoi/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
2. If you think you found a bug, or documentation could be improved, please open an issue

## License
Copyright (C) 2020 [Jonas Muehlmann](https://github.com/JonasMuehlmann)
 
The project is licensed under the terms of the GPL-V3 license, you can view it [here](LICENSE.md).
