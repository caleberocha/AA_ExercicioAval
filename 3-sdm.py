class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "(" + str(self.start) + "," + str(self.end) + ")"

    def __lt__(self, other):
        if other == None:
            return False
        return self.end < other.end

    def __le__(self, other):
        if other == None:
            return False
        return self.end <= other.end

    def __gt__(self, other):
        if other == None:
            return False
        return self.end > other.end

    def __ge__(self, other):
        if other == None:
            return False
        return self.end >= other.end

    def __eq__(self, other):
        if other == None:
            return False
        return self.end == other.end


def sdm(intervals):
    selected = []
    intervals.sort()
    
    selected.append(intervals[0])
    last_added = intervals[0]
    for interval in intervals[1:]:
        if interval.start >= last_added.end:
            selected.append(interval)
            last_added = interval

    return selected

intervals = [
    Interval(0,6),
    Interval(1,4),
    Interval(3,5),
    Interval(4,7),
    Interval(3,8),
    Interval(5,9),
    Interval(6,10),
    Interval(8,11)
]

s = sdm(intervals)
for r in s:
    print(r)