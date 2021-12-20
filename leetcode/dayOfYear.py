# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

# Example 1:
# Input: date = "2003-03-01"
# Output: 60

# Example 2:
# Input: date = "2004-03-01"
# Output: 61

#Solution
class Solution:
    def dayOfYear(self, date: str) -> int:
        year=int(date[:4])
        month=int(date[5:7])
        day=int(date[8:])
        n=0
        if year%4 != 0:
            if month == 1:
                n=day
            if month == 2:
                n=31 + day
            if month == 3:
                n=31+ 28+ day
            if month == 4:
                n=31+ 28+ 31 + day
            if month == 5:
                n=31+ 28+ 31 + 30 + day
            if month == 6:
                n=31+ 28+ 31 + 30 + 31+  day
            if month == 7:
                n=31+ 28+ 31 + 30 + 31+ 30+ day
            if month == 8:
                n=31+ 28+ 31 + 30 + 31+ 30+ 31+ day
            if month == 9:
                n=31+ 28+ 31 + 30 + 31+ 30+ 31+ 31+ day
            if month == 10:
                n=31+ 28+ 31 + 30 + 31+ 30+ 31+ 31+ 30+ day
            if month == 11:
                n=31+ 28+ 31 + 30 + 31+ 30+ 31+ 31+ 30+ 31+ day
            if month == 12:
                n=31+ 28+ 31 + 30 + 31+ 30+ 31+ 31+ 30+ 31+ 30+ day
        else:
            if month == 1:
                n=day
            if month == 2:
                n=31 + day
            if month == 3:
                n=31+ 29+ day
            if month == 4:
                n=31+ 29+ 31 + day
            if month == 5:
                n=31+ 29+ 31 + 30 + day
            if month == 6:
                n=31+ 29+ 31 + 30 + 31+  day
            if month == 7:
                n=31+ 29+ 31 + 30 + 31+ 30+ day
            if month == 8:
                n=31+ 29+ 31 + 30 + 31+ 30+ 31+ day
            if month == 9:
                n=31+ 29+ 31 + 30 + 31+ 30+ 31+ 31+ day
            if month == 10:
                n=31+ 29+ 31 + 30 + 31+ 30+ 31+ 31+ 30+ day
            if month == 11:
                n=31+ 29+ 31 + 30 + 31+ 30+ 31+ 31+ 30+ 31+ day
            if month == 12:
                n=31+ 29+ 31 + 30 + 31+ 30+ 31+ 31+ 30+ 31+ 30+ day
        return n
