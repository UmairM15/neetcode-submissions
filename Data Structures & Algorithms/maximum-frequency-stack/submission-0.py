from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(list)
        self.stack = []

    def push(self, val: int) -> None:
        i = 0
        while val in self.freq[i]:
            i += 1 
        self.freq[i].append(val)
        self.stack.append(val)
        
    def pop(self) -> int:
        maxFreq = max(self.freq.keys())
        freqVal = self.freq[maxFreq].pop()
        if not self.freq[maxFreq]:
            self.freq.pop(maxFreq)
        temp = []
        while self.stack[-1] != freqVal:
            temp.append(self.stack.pop())
        self.stack.pop()
        while temp:
            self.stack.append(temp.pop())
        return freqVal
        




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()