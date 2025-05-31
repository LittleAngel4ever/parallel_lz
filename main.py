from zd_1 import main as zd_1
from zd_2 import main as zd_2
from zd_3 import main as zd_3
import asyncio

def main():
    choose = input('Select what you want to see: \n 1 - multithreading;\n 2 - multiprocessing\n 3 - asynchronous\n. Your choise: ')
    if choose == '1':
        zd_1()
    elif choose == '2':
        zd_2()
    elif choose =='3':
        asyncio.run(zd_3())
    else:
        print('Please, try again')

if __name__ == '__main__':
    main()