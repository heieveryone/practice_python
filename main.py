import globals
import test

if __name__ == '__main__':
    globals.initialize()
    print(globals.num)
    test.increment()
    print(globals.num)
    


#print('before increment num in main.py,num address is {}'.format(id(num)))
#increment()
#print('final num value {} and address {}'.format(num,id(num)))


