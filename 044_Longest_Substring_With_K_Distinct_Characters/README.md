# Longest Substring With K Distinct Characters

Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most k distinct characters.

For instance, given the string:
aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.

Here's a starting point:
```
def longest_substring_with_k_distinct_characters(s, k):
  # Fill this in.

print longest_substring_with_k_distinct_characters('aabcdefff', 3)
# 5 (because 'defff' has length 5 with 3 characters)
```