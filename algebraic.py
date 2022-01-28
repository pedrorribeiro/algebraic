import random
from dataclasses import dataclass, field
# TODO: need to add documentation
# TODO: need to add timer
# TODO: need to add storage class
# TODO: need to add second stage band finish first stage

@dataclass
class Algebraic:
    x: int
    y: int
    z: int
    b: int
    allowed_types: list = field(default_factory=lambda: ['sum', 'sub', 'divide'])

    def type_definition(self, count, dx, dy, dz, db):
        if count in self.allowed_types:
            self.make_xyz(dx, dy, dz, db)
            if count == 'sum':
                math, text = self.sum()
            elif count == 'sub':
                math, text = self.sub()
            elif count == 'divide':
                math, text = self.divide()
        else:
            raise ValueError("only types sum, sub and divide are allowed")
        return math, text

    def make_xyz(self, dx: int, dy: int, dz: int, db: int):
        if dx is int and dy is int and dz is int and db is int:
            self.x = dx
            self.y = dy
            self.z = dz
            self.b = db
        else:
            raise ValueError("all status must be integers")

    def sum(self):
        result = (self.b - self.y) / self.z
        text = f'{self.z}x + {self.y} = {self.b} \n'
        return result, text

    def sub(self):
        result = (self.b + self.y) / self.z
        text = f'{self.z}x - {self.y} = {self.b} \n'
        return result, text

    def divide(self):
        result = (self.b * self.y) / self.z
        text = f'{self.z}x/{self.y} = {self.b} \n'
        return result, text

    def make_algebra(self):
        dx = random.randrange(1, 51)
        dy = random.randrange(1, 51)
        dz = random.randrange(1, 51)
        db = random.randrange(1, 51)
        count = random.choice(self.allowed_types)
        math, text = self.type_definition(count, dx, dy, dz, db)
        return math, text

    def count_control(self):
        math, text = self.make_algebra()
        response = int(input(text))
        if response == math:
            print('Correct')
        else:
            print('Wrong')

    def first_phase(self):
        start_text = 'You will now be shown several algebraic operations. You will have to solve each of them. \n' \
                     'Take as long as you need to perform this task. You must not use paper, or a calculator. \n'
        print(start_text)
        for
        self.count_control()

    def second_stage
