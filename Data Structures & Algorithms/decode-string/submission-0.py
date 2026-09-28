class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        curr_string = ""
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                count_stack.append(num)
                string_stack.append(curr_string)
                curr_string = ""
                num = 0
            elif char == "]":
                temp = curr_string
                curr_string = string_stack.pop()
                temp_num = count_stack.pop()
                curr_string += temp*temp_num
            else:
                curr_string += char
        return curr_string