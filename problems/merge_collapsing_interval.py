"""
Problem:
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

Solution:
Sort the given list by increasing order of starting time.
Push the first interval to stack.
For each interval
  if current interval does not overlap with top of stack, push it to stack
  if current interval overlaps with top of stack,
  merge the two intervals such that the starting interval is lowest and ending interval is highest.
At end, stack contains the merged intervals

"""


def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # sort list by the starting time
    intervals.sort(key=lambda x: x[0])

    # push first interval to stack
    result = [intervals.pop(0)]

    for current_interval in intervals:
        # get interval at top of stack
        t1, t2 = result[-1]
        # get current interval
        a, b = current_interval

        # check for overlap: if start of current interval is between top of stack interval
        if t1 <= a <= t2:
            # if overlap, replace the top interval with the new merged interval
            result.pop()
            result.append((t1, max(t2, b)))
        else:
            result.append(current_interval)
    return result


def test(actual, expected):
    return "OK" if actual == expected else "ERROR"


L = [(1, 3), (2, 6), (8, 10), (15, 18)]
expected_result = [(1, 6), (8, 10), (15, 18)]
actual_result = merge(L)
print(test(actual_result, expected_result))
