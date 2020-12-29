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

### Part 1
tbc


## [Day 10: Adapter Array](https://adventofcode.com/2020/day/10)

### Part 2

A bit of reverse-engineering on the two examples to try and create a more generalised solution. Perhaps permutations come into it somehow? 

Example 1 has the adapter list [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4] and has 8 possible distinct arrangements.
Example 2 has the adapter list [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3] and has 19208 distinct arrangements.

Using the methods already developed in part 1, we find that the list of joltage differences (in ascending order, including the charging outlet and device's in-built adapter) for each example is as follows -

Example 1: [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]

Example 2: [1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 3, 1, 1, 3, 3, 1, 1, 1, 1, 3, 1, 3, 3, 1, 1, 1, 1, 3]

Yeah, nothing is immediately jumping out at me either at this point, but I've got some thoughts. It's no great stretch to tell that where there's an isolated 1 between two 3s, there's not going to be any permutations to contribute to the total distinct arrangements. We're only interested in sublists of two or more consecutive 1s. (Also, let's pretend that differences of 2 don't exist unless my puzzle input demands it later on.)

For a sublist of strictly two consecutive 1s i.e. [3, 1, 1, 3], the only valid permutation is [3, 2, 3]. Each qualifying sublist therefore has the effect of doubling the total distinct arrangements.

With three consecutive 1s i.e. [3, 1, 1, 1, 3], valid permutations are [3, 1, 2, 3], [3, 2, 1, 3] and [3, 3, 3]. That quadruples the number of arrangements!

Let's count these sublists.

For example 1, the list of lengths of sublists formed of consecutive 1s is [1, 3, 2, 1]. There are 4 sublists, of which two are of length 1, one is of length 2 and one is of length 3.

Similarly, for example 2: [4, 4, 3, 2, 4, 1, 4]. There are 7 sublists, of which four are length 4, one is length 2, one is of length 3 and one is of length 2.

I do a bit of prime factorisation on the example solutions.

8 <=> 2^3 <=> 4^1 * 2^1

19208 <=> 7^4 * 2^3 * <=> 7^4 * 2^1 * 4^1

Interesting! For example 2, the sum of the exponents is equal to the number of sublists of 1s. Not so for example 1... or is it?

4^1 * 2^1 <=> 4^1 * 2^1 * 1^2

Yes, those 1s are hiding in plain sight!

So each sublist of 4 consecutive 1s has 7 permutations all in all.

My puzzle input doesn't need anything more complicated than that, so let's leave it there.

After completing this puzzle, I found this intriguing bit on [the OEIS entry for the Tribonacci sequence](https://oeis.org/A000073):

```
a(n) = number of compositions of n-2 with no part greater than 3. Example: a(5)=4 because we have 1+1+1 = 1+2 = 2+1 = 3. - Emeric Deutsch, Mar 10 2004
```