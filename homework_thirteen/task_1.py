import random    #kE^zbunsa$LR78v    / osho

KARMA = 500


class KillError(Exception):
    def __init__(self):
        super().__init__('Kill Error')

    # def __str__(self):
    #     return 'Kill Error'



class DrunkError(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return 'Drunk Error'


class CarCrashError(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return 'CarCrashError'

class GluttonyError(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return 'Gluttony Error'


class DepressionError(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return 'Depression Error'



def karma_counter():

   one_day = random.randint(1,7)
   exc = random.choice([KillError(), DrunkError(), DepressionError(), GluttonyError()])
   sin_choice = random.randint(1,10)

   if sin_choice == 5:
        raise exc
   return one_day


def main():

    karma = 0
    with open('karma.log', 'w') as krm_lg_write:
        while karma != KARMA:
            try:
                karma += karma_counter()
            except Exception as e:
                krm_lg_write.write(f'{e} \n')

    print(f'You achieved KARMA')



if __name__ == '__main__':
    main()



