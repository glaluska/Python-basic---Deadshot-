# 1
class FibonacciNumbers:
    def __init__(self, number):
        self.number = number
        self.fn_1 = 0
        self.fn_2 = 1
        self.fn = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.counter > self.number:
            raise StopIteration
        if self.counter == 0:
            self.counter += 1
            return 0
        elif self.counter == 1:
            self.counter += 1
            return 1
        else:
            self.counter += 1
            self.fn = self.fn_2 + self.fn_1
            self.fn_2, self.fn_1 = self.fn, self.fn_2
        return self.fn


for i in FibonacciNumbers(10):
    print(i)

print()

# 2
def generator_fibonacci (number):
    yield 0
    yield 1
    fn_2, fn_1 = 0, 1
    for i in range(1, number):
        fn = fn_1 + fn_2
        fn_2, fn_1 = fn_1, fn
        yield fn


for i in generator_fibonacci(10):
    print(i)

print()

# 3

def square_numbers (number):
    for i in range(0, number):
        yield i**2

for i in square_numbers(10):
        print(i)

print()


# 4

def accumulation_mean():
    n1 = yield
    n2 = 1
    while True:
        result = n1 / n2
        n1 += yield result
        n2 += 1

acc_mean = accumulation_mean()
acc_mean.__next__()
print(acc_mean.send(2))
print(acc_mean.send(8))
print(acc_mean.send(2))
print(acc_mean.send(4))




