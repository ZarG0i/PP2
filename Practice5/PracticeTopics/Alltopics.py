import re

# RegEx Introduction
print(re.findall(r"cat", "cat dog cat bird"))
print(re.findall(r"dog", "dog dog cat"))
print(re.findall(r"hello", "hello world hello"))

# RegEx Syntax and Metacharacters (., *, +, ?, ^, $, [], |, (), \)
print(re.findall(r"a.c", "abc aac acc"))
print(re.findall(r"ab*", "a ab abb abbb"))
print(re.findall(r"(cat|dog)", "cat dog bird cat"))

# Special Sequences (\d, \w, \s, \D, \W, \S, \A, \Z)
print(re.findall(r"\d+", "Age 18 year 2026"))
print(re.findall(r"\w+", "hello_world test123"))
print(re.findall(r"\s", "a b  c"))

# Sets and Character Classes
print(re.findall(r"[aeiou]", "regular expression"))
print(re.findall(r"[A-Z]", "Hello WORLD"))
print(re.findall(r"[0-5]", "0123456789"))

# Quantifiers ({n}, {n,}, {n,m})
print(re.findall(r"\d{3}", "123 45 6789"))
print(re.findall(r"a{2,}", "a aa aaa aaaa"))
print(re.findall(r"\d{2,4}", "1 12 123 1234 12345"))

# re.search() - Find first match
print(re.search(r"\d+", "abc123def"))
print(re.search(r"cat", "dog cat bird"))
print(re.search(r"\w+", "!!! hello"))

# re.findall() - Find all matches
print(re.findall(r"\d+", "a1 b22 c333"))
print(re.findall(r"[a-z]+", "abc ABC def"))
print(re.findall(r"cat", "cat dog cat cat"))

# re.split() - Split strings
print(re.split(r"\s+", "a b   c d"))
print(re.split(r",", "apple,banana,orange"))
print(re.split(r"\d+", "word1word2word3"))

# re.sub() - Replace patterns
print(re.sub(r"\d+", "#", "a1 b22 c333"))
print(re.sub(r"cat", "dog", "cat bird cat"))
print(re.sub(r"\s+", "-", "a b   c"))

# re.match() - Match at beginning
print(re.match(r"\d+", "123abc"))
print(re.match(r"cat", "cat dog"))
print(re.match(r"\w+", "hello world"))

# Flags (re.IGNORECASE, re.MULTILINE, etc.)
print(re.findall(r"cat", "Cat cat CAT", re.IGNORECASE))
print(re.findall(r"^cat", "cat\ndog\ncat", re.MULTILINE))
print(re.findall(r"dog", "DOG dog DoG", re.IGNORECASE))