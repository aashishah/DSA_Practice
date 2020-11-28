#CODE:
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key=lambda x:x[0])
        overlapping = [intervals[0]]
        
        for start, end in intervals:
            if overlapping[-1][1] < start:
                overlapping.append([start,end])
            else:
                overlapping[-1][1] = max(overlapping[-1][1], end)
                
        return overlapping
            
            
