# Advent of Code 2020

## [Day 1: Report repair](https://adventofcode.com/2020/day/1)
### Part 1
We're given a list and told to find the pair of values that sum to `2020`, and then provide the product of that pair.

Simplest approach is to look at each pair as follows:
- take our unsorted list (let's call it `num_list`)
- consider the very first item on the list, which we can represent as `num_list[0]`
- check this the sum of this number and every other item on the list, that is `num_list[1]` to `num_list[n-1]`
- if we haven't found the pair yet, we can rule out `num_list[0]` as being part of that pair. We then take `num_list[1]` as our first number and check it with `num_list[2]`, `num_list[3]`... `num_list[n-1]`.

Worst case scenario is `n*(n-1)/2` comparisons, making it `O(n^2)` runtime.

### Part 2
tbc

## [Day 2: Password Philosophy](https://adventofcode.com/2020/day/2)

# Part 1
tbc