import random
from sys import exit


def username():
    print ""
    name = raw_input('Enter the username: ')
    count = raw_input('Enter the number of names to generate: ')
    length = raw_input('Enter the required length of the password: ')
    print ""
    return name, count, length


def generate(name, count, length):
    for x in range(0, int(count)):
        password = ''
        for z in range(0, int(length)):
            password += random.choice('123456789abcdefghijkmnopqrstuvwxyz\
                                      ABCDEFGHJKLMNPQRSTUVWXYZ')
        print 'Website:             opencloud-codemiller.rhcloud.com'
        print 'Workshop Username:   ' + name + str((x+1))
        print 'OpenShift Username:  ' + name + str((x+1)) + '@gmail.com'
        print 'Password:            ' + password + '\n'


def run():
    info = username()
    generate(info[0], info[1], info[2])
    repeat = raw_input('Run again? (y/n): ')
    if repeat == 'y':
        run()
    else:
        exit()


if __name__ == "__main__":
    run()
