class Hello:
    x=2
    y=5
    def getSum(self, a, b):
        return a+b
obj=Hello()
print(obj.getSum(9,7))
print(obj.x, obj.y)