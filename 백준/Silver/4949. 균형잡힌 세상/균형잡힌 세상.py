class Stack:
    def __init__(self):
        self.s = []
    def push(self, data):
        self.s.append(data)
    def pop(self):
        return self.s.pop()
    def is_empty(self):
        return len(self.s) == 0
    def peek(self):
        if self.is_empty() == True:
            return None
        else:
            return self.s[-1]
    def __str__(self):
        return str(self.s)

while True:
    S = input()
    if S == ".":
        break
    else:
        st = Stack()
        is_valid = True
        dot_cnt = 0
        for ch in S:
            if ch == "(":
                st.push(ch)
            elif ch == "[":
                st.push(ch)
            elif ch == ")":
                if st.peek() == "(":
                    st.pop()
                else:
                    is_valid = False
            elif ch == "]":
                if st.peek() == "[":
                    st.pop()
                else:
                    is_valid = False
            elif ch == ".":
                dot_cnt += 1
        
        if st.is_empty() and dot_cnt == 1 and S[-1] == "." and is_valid:
            print(f"yes")
        else:
            print(f"no")