class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # we take stack so that we can pop and push , becuase we are working on pair and we gotta find if every opening bracket has the closing bracket
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        # so we take dictionary here to keep the pair of the brackets for reference, then we know which one is that we are popping and appending olgadege antha, okay:)
        for ch in s:
            if ch in "{([":
                stack.append(ch)
            else: 
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return len(stack) == 0