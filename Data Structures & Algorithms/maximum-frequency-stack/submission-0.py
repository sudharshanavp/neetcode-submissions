class FreqStack:
    def __init__(self):
        self.freq_stack = []
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq_stack.append(val)
        self.freq[val] += 1

    def pop(self) -> int:
        max_count = max(self.freq.values())
        i = len(self.freq_stack) - 1
        while self.freq[self.freq_stack[i]] != max_count:
            i -= 1
        self.freq[self.freq_stack[i]] -= 1
        return self.freq_stack.pop(i)




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()