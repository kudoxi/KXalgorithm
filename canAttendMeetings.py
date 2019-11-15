"""
Definition of Interval.
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals:
            return True
        n = 0
        new_intervals = []
        for i in intervals:
            s = i.start
            e = i.end
            new_intervals.append((s, e))
        new_intervals = sorted(new_intervals)
        new_intervals.append(('end', 'end'))
        for i in new_intervals:
            if i[0] != 'end' and new_intervals[n + 1][0] != 'end' and i[1] > new_intervals[n + 1][0]:
                return False
            n += 1
        return True


if __name__ == "__main__":
    print(Solution().canAttendMeetings([Interval(465,497),Interval(386,462),Interval(354,380),
                                        Interval(134,189),Interval(199,282),Interval(18,104),
                                        Interval(499,562),Interval(4,14),Interval(111,129),Interval(292,345)]))
