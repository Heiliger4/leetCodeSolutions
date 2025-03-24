class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        busy_days = set()
        for start, end in meetings:
            for day in range(start, end + 1):
                busy_days.add(day)
        return days - len(busy_days)
