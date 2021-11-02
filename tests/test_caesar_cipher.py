from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    text1='abc'
    text2='zzz'
    shift1=1
    shift2=10
    shift3=27
    actual1=encrypt(text1,shift1)
    actual2=encrypt(text1,shift2)
    actual3=encrypt(text1,shift3)
    actual4=encrypt(text2,shift1)
    excpected1='bcd'
    excpected2='klm'
    excpected3='bcd'
    excpected4='aaa'

    assert actual1==excpected1
    assert actual2==excpected2
    assert actual3==excpected3
    assert actual4==excpected4

def test_decrypt():
    text='bcd'
    shift=1
    actual=decrypt(text, shift)
    excpected='abc'
    assert actual==excpected

def test_crack():
    text='It was the best of times'
    actual=crack(text)
    excpected='It was the best of times'
    assert actual==excpected