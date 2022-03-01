"""
 @param intervals: an array of meeting time intervals
@return: if a person could attend all meetings
"""

def can_attend_meetings(self, intervals: List[Interval]) -> bool:
    intervals.sort(key=lambda x:x.start)

    if len(intervals) == 0 :
        return True

    lastMeeting = intervals[0]

    for curr in intervals[1:]:
        if lastMeeting.end > curr.start:
            return False

        lastMeeting = curr


    return True
