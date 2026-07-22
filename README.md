# Algorithm Toolkit

一个用于学习 Python 算法、项目结构和软件工程实践的项目。

## Features

- Two Sum
- Find Max
- Reverse Array

## Requirements

- Python 3.10+

## Installation

Clone the repository:
powershell
git clone https://github.com/inmaginebreaker-beep/algorithm-toolkit.git
cd algorithm-toolkit

## Create and activate a virtual environment:

python -m venv .venv
.\.venv\Scripts\activate

## Install the project:

python -m pip install -e .

## Install development dependencies:

python -m pip install -e ".[dev]"

## Usage

from algorithm_toolkit.algorithms.array import two_sum

result = two_sum([2, 7, 11, 15], 9)
print(result)

## Run

python -m algorithm_toolkit.main

## Project Structure

algorithm-toolkit/

├── src/

│   └── algorithm_toolkit/

│       ├── __init__.py

│       ├── main.py

│       └── algorithms/

│           ├── __init__.py

│           └── array.py

├── tests/

├── .gitignore

├── pyproject.toml

└── README.md

## License

This project is for educational purposes.