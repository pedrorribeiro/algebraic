import random
import time
from threading import Timer
from dataclasses import dataclass, field


# TODO: need to fix timer

@dataclass
class Storage:
    listing: dict

    def open_list(self):
        self.listing = {}

    def dict_maker(self, iteration: int, text: str, result: float, timer: float):
        dictionary = {iteration: {
            'operation': text,
            'result': result,
            'time': time
        }
        }
        self.listing.update(dictionary)


@dataclass
class Algebraic(Storage):
    """
    Class manages the creation of algebraic operations for user completion.
    """
    x: int = 1
    y: int = 1
    z: int = 1
    b: int = 1
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

        self.x = dx
        self.y = dy
        self.z = dz
        self.b = db

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
        dx = random.randrange(1, 10)
        dy = random.randrange(1, 10)
        dz = random.randrange(1, 10)
        db = random.randrange(1, 10)
        count = random.choice(self.allowed_types)
        math, text = self.type_definition(count, dx, dy, dz, db)
        return math, text

    def count_control(self):
        """
        Automates subject interaction.
        :return:
        """
        math, text = self.make_algebra()
        response = float(input(text))
        if response == math:
            print('Correct')
        else:
            print('Wrong')
        return math, text

    def first_phase(self):
        """
        Manages first algebraic game phase.
        :return:
        """
        start_text = 'You will now be shown several algebraic operations. You will have to solve each of them. \n' \
                     'Take as long as you need to perform this task. You must not use paper, or a calculator. \n'
        print(start_text)
        time.sleep(5)
        for i in range(1, 10):
            start_time = time.time() * 1000
            math, text = self.count_control()
            final_time = time.time() * 1000
            timer = final_time - start_time
            self.dict_maker(i, text, math, timer)
        self.second_stage()

    def second_stage(self):
        start_text = 'You will now be shown the same operations you completed earlier. \n ' \
                     'You will have a certain amount of time to complete these operations again. \n' \
                     'This time will be half the time you took to complete them the first time.'
        print(start_text)
        for i in self.listing:
            op = self.listing[i]
            operation = op['operation']
            result = op['result']
            timeout = op['time']
            t = Timer(timeout, print, ['Sorry, times up'])
            t.start()
            response = input(operation)
            t.cancel()
            if response == result:
                print('Correct!')
            else:
                print('Wrong!')
            print('Thank you.')
