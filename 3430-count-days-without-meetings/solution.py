class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # Sort meetings by start day
        free_days = 0
        last_end = 0

        for start, end in meetings:
            if start > last_end + 1:  # There is a gap
                free_days += start - (last_end + 1)
            last_end = max(last_end, end)  # Update last meeting end

        # Count remaining free days after the last meeting
        if last_end < days:
            free_days += days - last_end

        return free_days

