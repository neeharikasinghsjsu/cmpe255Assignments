class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def subtract(self, num):
        self.result -= num
        return self.result

    def multiply(self, num):
        self.result *= num
        return self.result

    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            self.result = 'Error'
        return self.result

    def clear(self):
        self.result = 0
