#!_*_coding:utf-8_*_
# __author__: "Lightwing Ng"

import os, sys
from core import main

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

if __name__ == '__main__':
    main.run()

