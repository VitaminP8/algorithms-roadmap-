class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backTracking (operBrackets, closeBrackets):
            if operBrackets == closeBrackets == n:
                res.append("".join(stack))
                return

            if operBrackets < n:
                stack.append("(")
                backTracking(operBrackets+1, closeBrackets)
                stack.pop()

            if closeBrackets < operBrackets:
                stack.append(")")
                backTracking(operBrackets, closeBrackets+1)
                stack.pop()

        backTracking(0,0)
        return res