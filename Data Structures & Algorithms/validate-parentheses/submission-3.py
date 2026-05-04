class Solution:
    def isValid(self, s: str) -> bool:

        valid =True

        stack=[]

        opens = {"(":1,"{":2,"[":3}
        closes = {")":1,"}":2,"]":3}

        for char in s:
            if char in opens.keys():
                stack.append(opens[char])
            elif char in closes.keys():
                if stack:
                    top=stack.pop()
                    if top != closes[char]:
                        valid=False
                else:
                    valid=False
            else:
                valid=False

        if stack:
            valid=False

        return valid

        