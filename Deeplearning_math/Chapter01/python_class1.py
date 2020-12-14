class calculator:
    def __init__(self, x, y, operator):
        self._x = x
        self._y = y
        self._operator = operator
        
        self.result = None
        
        if self._operator == '+':
            self._adder()
        elif self._operator == '-':
            self._subtractor()
        elif self._operator == '*':
            self._multiplier()
        
    # 파이썬은 관용적으로 underscore(_)를 이용해 private, 즉 사용자를 위한 것이 아닌 내부적인 (연산을 위한) 매서드를 표기한다.
        
    def _adder(self):
        self.result = self._x + self._y
    
    def _subtractor(self):
        self.result = self._x - self._y
    
    def _multiplier(self):
        self.result = self._x * self._y
    
    def get_result(self):
        return self.result

print("ex. 3+4\nInput int, operator, int: ")
input_list = input()
x, op, y = int(input_list[0]), input_list[1], int(input_list[2])
tmp = calculator(x, y, op)
print(tmp.get_result())