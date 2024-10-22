class ex:
    def __init__(self):
        self.value = 1
    def a(self,x):
        self.value = x + 1
    def b(self,y):
        self.a(y * 2)
        return self.value
ex = ex()
result = ex.b(5)
print(result)
