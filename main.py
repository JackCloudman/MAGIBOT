import os
from dotenv import load_dotenv,find_dotenv
from core.core import Core
load_dotenv(find_dotenv())

def main():
    c = Core()
    c.start()

if __name__ == '__main__':
    main()
