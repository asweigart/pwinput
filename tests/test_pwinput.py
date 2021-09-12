
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NOTE: We can't use pytest for these tests because using pyautogui to send
# the input results in a "oserror: reading from stdin while output is captured"
# error.
# These tests don't fail so much as hang the system. If you see the test hang,
# that means there's a failure somewhere.
# CURRENTLY TOX DOESN'T SEEM TO WORK WITH THIS TEST.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import io
import sys
import threading
import time
import unittest

import pwinput

from pynput.keyboard import Controller

keyboard = Controller()
originalStdout = sys.stdout


# TODO - work in progress

def pauseThenType(text, pauseLen=0.05):
    def inner(text):
        time.sleep(pauseLen)
        keyboard.type(text)
    t = threading.Thread(target=inner, args=(text,))
    t.start()
    sys.stdout = io.StringIO()

class test_main(unittest.TestCase):
    def test_pwinput(self):
        # Test typical usage.
        pauseThenType('swordfish\n')
        self.assertEqual(pwinput.pwinput(), 'swordfish')

        # Test the backspace key.
        pauseThenType('swordfish\bH\n')
        self.assertEqual(pwinput.pwinput(), 'swordfisH')

        # Test pressing the backspace key more times than necessary.
        pauseThenType('swordfish' + ('\b' * 20) + 'mary\n')
        self.assertEqual(pwinput.pwinput(), 'mary')

        # Test every typable character.
        pauseThenType('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+,./;\'<>?:"[]{}\n')
        self.assertEqual(pwinput.pwinput(), 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+,./;\'<>?:"[]{}')


if __name__ == '__main__':
    unittest.main()
    sys.stdout = originalStdout # Restore stdout.
