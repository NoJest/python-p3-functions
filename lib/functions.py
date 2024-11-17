#!/usr/bin/env python3

def greet_programmer():
    return print(f"Hello, programmer!")
    pass

def greet(name="guido"):
    return print(f"Hello, {name}!")
    pass

def greet_with_default(name="programmer"):
    return print(f"Hello, {name}!")
    pass

def add(num1=44, num2=55):
    return num1 + num2
    pass

def halve(number=100):
    return number / 2
    pass
