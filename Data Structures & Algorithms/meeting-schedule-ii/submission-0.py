"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_meetings = 0
        events = []
        for meeting in intervals:
            events.append((meeting.start, 1))
            events.append((meeting.end, -1))
        
        events.sort()
        curr = 0
        for event in events:
            curr += event[1]
            max_meetings = max(max_meetings, curr)
        return max_meetings


        

