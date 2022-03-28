##
#### 394. Decode String (medium)
####################################


## single stack
###################
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                curr = ""
                while stack[-1] != "[":
                    curr = stack.pop() + curr

                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                for _ in range(int(k)):
                    stack.append(curr)
            else:
                stack.append(char)

        return "".join(stack)


## two stacks
#################
class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        str_stack = [""]
        curr_str = ""
        k = ""
        for char in s:
            if char.isdigit():
                k += char
            if char.isalpha():
                curr_str += char
            if char == "[":
                count_stack.append(int(k))
                str_stack.append(curr_str)
                k = ""
                curr_str = ""
            if char == "]":
                curr_str = str_stack.pop() + curr_str * count_stack.pop()

        return curr_str


## recursion
################
