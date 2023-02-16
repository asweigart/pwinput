PWInput
======

A cross-platform Python module that displays **** for password input. Formerly called stdiomask.

Installation
------------

To install with pip, run:

    pip install pwinput

Quickstart Guide
----------------

The `getpass.getpass()` function in the Python Standard Library won't display "mask" characters as you type; it only displays nothing as you type. If you want mask characters to appear, you can use the `pwinput.pwinput()` function instead.

Typical usage:

    >>> import pwinput
    >>> pwinput.pwinput()  # Show * for each typed character.
    Password: *********
    'swordfish'
    >>> pwinput.pwinput(prompt='PW: ')  # Show a custom prompt.
    PW: *********
    'swordfish'
    >>> pwinput.pwinput(mask='X')  # Show a different character when user types.
    Password: XXXXXXXXX
    'swordfish'
    >>> pwinput.pwinput(mask='') # Don't show anything when user types (falls back and calls getpass.getpass()).
    Password:
    'swordfish'

Contribute
----------

If you'd like to contribute to pwinput, check out https://github.com/asweigart/pwinput

Support
-------

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon](https://www.patreon.com/AlSweigart).
