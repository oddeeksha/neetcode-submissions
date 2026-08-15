class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para_dict = {
        "}" : "{",
        ")" : "(",
        "]" : "["
       }
        for para in s:
            if para not in para_dict:
                stack.append(para)
            else:
                if not stack:
                    return False
                open_para = stack.pop()
                if para_dict[para] != open_para:
                    return False
        return not stack
            

       