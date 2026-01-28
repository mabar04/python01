#!/usr/bin/env python3
"""
a main program that creates varriables and print them to the screen
the difference between executing the code inside a main and not is the
import part, the only time that the code runs in the terminal is
when you run it as a program and not as an import
"""
if __name__ == "__main__":
    name: str = "Rose"
    height: str = "25cm"
    age: str = "30 days"
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}")
    print(f"Age: {age}")
    print("=== End of Program ===")
