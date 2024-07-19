class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for elem in path.split("/"):
            if elem == "..":
                if stack:
                    stack.pop()  # Remove the last directory from the stack
            elif elem and elem != ".":  # Skip empty elements and "."
                stack.append(elem)  # Push directory onto the stack

        return "/" + "/".join(stack)  # Join elements in the stack with "/"
