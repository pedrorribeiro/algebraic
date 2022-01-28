import random
from dataclasses import dataclass, field
# TODO: need to add timer
# TODO: need to add storage class
# TODO: need to add second stage band finish first stage

@dataclass
class Algebraic:
    """
    Class manages the creation of algebraic operations for user completion.
    """
    x: int
    y: int
    z: int
    b: int
    allowed_types: list = field(default_factory=lambda: ['sum', 'sub', 'divide'])

    def type_definition(self, count, dx, dy, dz, db):
        """
        Type definition checks if type is allowed type and feeds paremeters count, dx, dy, dz, db to the specific
        type functions.
        :param count:
        :param dx:
        :param dy:
        :param dz:
        :param db:
        :return:
        """
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
        """
        Turns all operational parameters into class parameters.
        :param dx:
        :param dy:
        :param dz:
        :param db:
        :return:
        """
        if dx is int and dy is int and dz is int and db is int:
            self.x = dx
            self.y = dy
            self.z = dz
            self.b = db
        else:
            raise ValueError("all status must be integers")

    def sum(self):
        """
        Deals with sum type operations.
        :return:
        """
        result = (self.b - self.y) / self.z
        text = f'{self.z}x + {self.y} = {self.b} \n'
        return result, text

    def sub(self):
        """
        Deal with sub type operations.
        :return:
        """
        result = (self.b + self.y) / self.z
        text = f'{self.z}x - {self.y} = {self.b} \n'
        return result, text

    def divide(self):
        """
        Deals with divide type operations.
        :return:
        """
        result = (self.b * self.y) / self.z
        text = f'{self.z}x/{self.y} = {self.b} \n'
        return result, text

    def make_algebra(self):
        """
        randomizes the process of creating the algebraic operations.
        :return:
        """
        dx = random.randrange(1, 51)
        dy = random.randrange(1, 51)
        dz = random.randrange(1, 51)
        db = random.randrange(1, 51)
        count = random.choice(self.allowed_types)
        math, text = self.type_definition(count, dx, dy, dz, db)
        return math, text

    def count_control(self):
        """
        Automates subject interaction.
        :return:
        """
        math, text = self.make_algebra()
        response = int(input(text))
        if response == math:
            print('Correct')
        else:
            print('Wrong')

    def first_phase(self):
        """
        Manages first algebraic game phase.
        :return:
        """
        start_text = 'You will now be shown several algebraic operations. You will have to solve each of them. \n' \
                     'Take as long as you need to perform this task. You must not use paper, or a calculator. \n'
        print(start_text)
        for
        self.count_control()

    def second_stage
