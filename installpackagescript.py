import os
import sys


try:
    import pip

except ImportError:
    print('----- Install pip -----')
    cmd = 'easy_install pip'
    os.system(cmd)


pip = f'{sys.executable} -m pip'


if __name__ == '__main__':
    print('Start installing packages')

    print('----- Install pyqt5 -----')
    cmd = 'sudo apt-get install python3-pyqt5'
    os.system(cmd)

    print('Success !!! : All packages have been installed')
