# ContraFix: Basic DSA Bug Lab

Five beginner-friendly Python questions with intentionally buggy solutions and
30 real pytest checks. Fix the solution, not the tests. No correct solutions are
published here. These are original small exercises, with no external services.

## Questions and File Selections

| Question | Source file | Test file |
| --- | --- | --- |
| Linear Search | `linear_search.py` | `test_linear_search.py` |
| Binary Search | `binary_search.py` | `test_binary_search.py` |
| Bubble Sort | `bubble_sort.py` | `test_bubble_sort.py` |
| Largest Element in an Array | `largest_element.py` | `test_largest_element.py` |
| Reverse a Linked List | `reverse_linked_list.py` | `test_reverse_linked_list.py` |

Each pair is root-level, self-contained and has six checks. Tests are expected
to fail before fixing the bugs. Edge cases include empty/single-element inputs,
negative numbers, duplicates and correct linked-list connections.

## Test Using ContraFix

1. Import `https://github.com/EPIC-SID/contrafix-dsa-demo` in GitHub repository.
2. Select one source/test pair above and choose Use existing tests.
3. Paste the matching problem text below and click Save selection.
4. Select your two configured agents, give sharing consent, then Analyze &
   propose fixes. Inspect the debate, proposed code and downloaded report/diffs.
5. Verification requires the backend operator's enabled, validated sandbox.
   Analysis alone does not prove correctness. Mock retains the buggy source;
   it tests the interface without spending API quota, not the repair ability.

Already imported an older version? Create a fresh import of this URL: saved
imports are pinned to a Git commit and will not automatically get new files.

## Problem Text to Paste

### 1. Linear Search

Find a number in an array and return its first index, or -1 if missing. Check
every element, including the last one. [4, 2, 8] searching for 8 returns 2.
[7] searching for 7 returns 0. Empty input returns -1. Do not change input.

### 2. Binary Search

Find a target in a sorted array of distinct integers and return its index, or -1
if missing. [1, 3, 5, 7, 9] searching for 9 returns 4. [7] searching for 7 returns
0. Empty input returns -1. Do not change input. Keep the binary search approach.

### 3. Bubble Sort

Sort an array of integers from smallest to largest using bubble sort. Return a
new list and leave the original unchanged. [3, 2, 1] becomes [1, 2, 3]. Include
negative values and duplicates. Empty input returns a new empty list.

### 4. Largest Element in an Array

Return the largest number in an array, or None for empty input. [3, 9, 2] returns
9. [-8, -3, -6] returns -3, not zero. A single-element array returns that element.
Do not change input.

### 5. Reverse a Linked List

Reverse a singly linked list in place and return its new head. Each Node has
value and next fields. 1 -> 2 -> 3 -> None becomes 3 -> 2 -> 1 -> None. Reuse
the original nodes, do not change their values, and do not create cycles. None
returns None; a single node stays the same node. Inputs are acyclic lists.

## Run Locally

Python 3.10 or newer:

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux instead: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

Run just one exercise, for example:

```bash
python -m pytest test_linear_search.py -q
```

The checks verify examples and edge cases, not formal correctness or runtime
benchmarks. ContraFix does not automatically push fixes back into this repo.
