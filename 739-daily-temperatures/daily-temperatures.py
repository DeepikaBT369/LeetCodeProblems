class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        n = len(temperatures)
        answer = [0] * n

        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                day = stack.pop()
                answer[day] = i - day
            stack.append(i)
        return answer