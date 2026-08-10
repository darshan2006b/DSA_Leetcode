class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        intervals.sort()
        start,end = intervals[0]
        interval = []
        for i in range(1,n):
            next_start,next_end = intervals[i]

            if end >= next_start:
                if  next_end > end:
                    end = next_end
                    
            else:
                interval.append([start,end])
                start = next_start
                end = next_end

        interval.append([start,end])

        return interval