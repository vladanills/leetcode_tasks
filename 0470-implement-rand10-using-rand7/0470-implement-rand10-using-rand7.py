# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        table = [[None for _ in range(7)] for _ in range(7)]
        n = 0
        for r in range(7):
            for c in range(7):
                table[r][c] = n%10
                n+=1
        while True:
            row = rand7() - 1
            col = rand7() - 1
            if row == 6 or (row == 5 and col>=5):
                continue
            return table[row][col]+1 