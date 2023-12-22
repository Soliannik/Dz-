a = [1, 2, 3, 4, 5]
iterator = iter(a)

print(next(iterator))
for i in iterator:
    print(i)
b = [0, 2, 4, 6, 8, 10]
iterator = iter(b)
for c in iterator:
    print(c)
for c in iterator:
    print(c)
class Iterator:
    def __init__(self, max_num):
        self.max_num = max_num
    def __iter__(self):
        self.i = -2
        return self
    def __next__(self):
        def gen():
            i=0
            while i!= 10:
                yield i
        generator = gen()
        if self.i > self.max.num:
            raise StopIteration
        return generator
