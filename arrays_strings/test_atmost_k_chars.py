import pytest

from atmost_k_chars import find_longest_substring


def test_example():
    assert find_longest_substring("eceba", 2) == 3

def test_another_example():
    assert find_longest_substring("aa", 1) == 2

def test_k_larger_than_distinct_chars():
    assert find_longest_substring("abc", 10) == 3

def test_k_equals_one():
    assert find_longest_substring("aabbbc", 1) == 3

def test_all_same_chars():
    assert find_longest_substring("aaaaa", 2) == 5

def test_all_distinct_chars():
    assert find_longest_substring("abcdef", 3) == 3

def test_longest_at_end():
    assert find_longest_substring("abcddddd", 2) == 6

def test_single_char():
    assert find_longest_substring("a", 1) == 1

def test_empty_string():
    assert find_longest_substring("", 2) == 0

def test_k_zero():
    assert find_longest_substring("abc", 0) == 0


def test_longest_at_start():
    assert find_longest_substring("aaabcd", 2) == 4

def test_longest_in_middle():
    assert find_longest_substring("xyaabbbbcz", 2) == 6

def test_window_shrinks_and_reuses_chars():
    assert find_longest_substring("abaccc", 2) == 4

def test_is_case_sensitive():
    assert find_longest_substring("aAaA", 1) == 1
    assert find_longest_substring("aAaA", 2) == 4

def test_non_letter_characters():
    assert find_longest_substring("1 1 2", 2) == 4

def test_k_equals_distinct_count():
    assert find_longest_substring("abcabc", 3) == 6

def test_matches_brute_force():
    import random

    def brute(s, k):
        best = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(set(s[i:j + 1])) <= k:
                    best = max(best, j - i + 1)
        return best

    rng = random.Random(0)
    for _ in range(200):
        s = "".join(rng.choice("abcd") for _ in range(rng.randint(0, 12)))
        k = rng.randint(0, 5)
        assert find_longest_substring(s, k) == brute(s, k), (s, k)
