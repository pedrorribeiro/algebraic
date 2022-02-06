import random
import asyncio
import sys
import time
import os
import fcntl
from dataclasses import dataclass, field


async def timex(prompt: str, timeout: int):
    timer = 0
    response = 0
    var = 0
    start = time.time()
    fl = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
    fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, fl | os.O_NONBLOCK)
    await asyncio.get_event_loop().run_in_executor(
        None, lambda s=prompt: sys.stdout.write(s + '\n'))
    while timer < timeout:
        try:
            stdin = sys.stdin.read()
            response = float(stdin)
            break
        except TypeError:
            timer = time.time() - start
            pass

    if timer >= timeout:
        print('Time is up!')
        var = 5985
        return var
    else:
        return response


@dataclass
class Storage:
    listing: dict

    def open_list(self):
        self.listing = {}

    def dict_maker(self, iteration: int, text: str, result: float, timer: float):
        dictionary = {iteration: {
            'operation': text,
            'result': result,
            'time': timer
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

    @staticmethod
    async def ainput(string: str) -> str:
        await asyncio.get_event_loop().run_in_executor(
            None, lambda s=string: sys.stdout.write(s + '\n'))
        return await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)

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
            print('\nCorrect!\n')
        else:
            print('\nWrong!\n')
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
            start_time = time.time()
            math, text = self.count_control()
            final_time = time.time()
            timer = int((final_time - start_time))
            self.dict_maker(i, text, math, timer)
        self.second_stage()

    def second_stage(self):
        start_text = 'You will now be shown the same operations you completed earlier. \n ' \
                     'You will have a certain amount of time to complete these operations again. \n' \
                     'This time will be half the time you took to complete them the first time.'
        print(start_text)
        time.sleep(5)
        for i in self.listing:
            op = self.listing[i]
            operation = op['operation']
            result = op['result']
            timeout = op['time'] / 2
            print(timeout)
            this = self
            response = asyncio.run(timex(operation, timeout))
            if response == result:
                print('Correct!')
            elif response == 5985:
                pass
            else:
                print('Wrong!')
        print('Thank you.')

    def third_stage(self):
        """
                Manages third algebraic game phase.
                :return:
                """
        start_text = 'You will now be shown several algebraic operations. You will have to solve each of them. \n' \
                     'You will have 15 seconds to complete each operation. You must not use paper, or a calculator. \n'

        print(start_text)
        time.sleep(5)
        for i in range(1, 20):
            math, text = self.make_algebra()
            response = asyncio.run(timex(text, 15))
            if response == math:
                print('\nCorrect!\n')
            elif response == 5985:
                pass
            else:
                print('\nWrong!\n')

    def fourth_stage(self):
        """
                Manages third algebraic game phase.
                :return:
                """
        start_text = 'You will now be shown several algebraic operations. You will have to solve each of them. \n' \
                     'You will have 8 seconds to complete each operation. You must not use paper, or a calculator. \n'

        print(start_text)
        time.sleep(5)
        for i in range(1, 37):
            math, text = self.make_algebra()
            response = asyncio.run(timex(text, 8))
            if response == math:
                print('\nCorrect!\n')
            elif response == 5985:
                pass
            else:
                print('\nWrong!\n')


alg = Algebraic(['sum', 'sub', 'divide'], 1, 2, 3, 4)

alg.fourth_stage()
