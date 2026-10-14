# ContraFix DSA Bug Lab

Five intentionally buggy Python algorithms with real, deterministic tests.
Use this public repo to test imported-file debugging in ContraFix. These are
original small exercises, not copied problem statements or production code.

**Tests are supposed to fail initially.** Fix the selected implementation,
not its tests. No reference solutions are included in this repository.

## Local Setup

Python 3.10 or newer:

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux instead: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

Every source/test pair is root-level and self-contained, so it can be selected
independently. No network, credentials, external datasets or app dependencies.
Full initial suite: 31 checks, with intentional failures across all five tasks.

## Import Into ContraFix

1. Open GitHub repository in ContraFix.
2. Paste this repository's public URL and click Import repository.
3. Choose one source/test pair from the table and Use existing tests.
4. Paste that task's problem description below; click Save selection.
5. Choose two configured live agents, consent to sharing and click Analyze &
   propose fixes. Mock previews the original code; it does not generate repairs.
6. Inspect both proposals, debate and downloaded diffs/report.
7. Use Verify in sandbox only when your operator has enabled validated isolation.
   Analysis alone is not proof of a fix. Nothing is pushed back here automatically.

| Task | Source file | Test file | Difficulty |
| --- | --- | --- | --- |
| Two Sum | `two_sum.py` | `test_two_sum.py` | Easy |
| Binary Search | `binary_search.py` | `test_binary_search.py` | Easy |
| Balanced Brackets | `balanced_brackets.py` | `test_balanced_brackets.py` | Easy |
| Merge Intervals | `merge_intervals.py` | `test_merge_intervals.py` | Medium |
| Maximum Subarray | `maximum_subarray.py` | `test_maximum_subarray.py` | Medium |

### Two Sum: Problem Text

Return two different indices whose numbers add to the target, or None if no
pair exists. There is at most one valid pair. Return indices in increasing order.
Do not reuse one element or change the input. [3, 3] with target 6 returns [0, 1],
but [3] with target 6 returns None. Zero and negative values are valid.

### Binary Search: Problem Text

Find a target in a sorted list of distinct integers and return its index, or -1
if absent. Do not change input. Searching [7] for 7 returns 0. Searching
[1, 3, 5, 7, 9] for 9 returns 4. Empty input returns -1. Keep logarithmic search.

### Balanced Brackets: Problem Text

Check whether (), [] and {} are properly paired and nested. Ignore other
characters. Empty text is valid. ([]{} ) is valid, but an unfinished opening
bracket, an extra closing bracket, or crossed nesting such as ([)] is invalid.

### Merge Intervals: Problem Text

Merge overlapping closed intervals and return them sorted by start. Touching
endpoints count as overlap: [[1, 4], [4, 5]] becomes [[1, 5]]. Disjoint intervals
stay separate. Input can be unsorted; start is at most end. Do not change the
input, including inner lists. Empty input returns an empty list.

### Maximum Subarray: Problem Text

Return the largest sum of any contiguous nonempty part of the input. Empty input
returns 0. Negative-only input must return its largest element, not zero:
[-8, -3, -6] returns -3. [1, 2, 3] returns 6. Do not change input. Use linear time.

## Run One Challenge

```bash
python -m pytest test_two_sum.py -q
python -m pytest test_binary_search.py -q
python -m pytest test_balanced_brackets.py -q
python -m pytest test_merge_intervals.py -q
python -m pytest test_maximum_subarray.py -q
```

The checks cover edge cases and input preservation, not formal correctness or
runtime benchmarks. Live agent quality and sandbox availability depend on your
ContraFix backend. Do not run unrelated untrusted imports directly on your laptop.
