class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for curr_path in path:
            if stack and curr_path == "..":
                stack.pop()
                continue
            elif curr_path != "" and curr_path != "." and curr_path != "..":
                stack.append(curr_path)

        return "/" + "/".join(stack)