class Casually_Stack:
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
            return "비어 있습니다"
        else:
            return self.s[-1]
    def __str__(self):
        return str(self.s)
 
T = int(input())
b_list = []

for i in range(T):
    b_list.append(input())

for test_case in b_list:
    b_stack = Casually_Stack()
    is_valid = True
    
    for b in test_case:
        if b == "(":
            b_stack.push(b)
        else:
            if b_stack.is_empty():
                is_valid = False
                break
            else:
                if b_stack.pop() == "(":
                    continue # for문의 다음 순서로 넘어가는 제어문
                else:
                    is_valid = False
                    break
    if not b_stack.is_empty():
        is_valid = False
    
    print("YES" if is_valid else "NO")