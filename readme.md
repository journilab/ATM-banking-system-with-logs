# README
==========

## Author
---------
Sebastian Hsiao

Email: bastianhsiao@gmail.com

GitHub: [github.com/journilab](https://github.com/journilab)

## ATM Banking System
---------------------

This project is a simple implementation of an ATM banking system using Python. The system allows users to perform basic banking operations such as deposit, withdrawal, and account balance inquiry.

### Features
------------

* User authentication using a 4-digit PIN
* Deposit and withdrawal of funds
* Account balance inquiry
* Transaction logging

### Usage
---------

#### Prerequisites

* Python 3.13.3 or later
* `logging` and `datetime` modules

#### Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the `script.py` file to start the ATM system.

#### Running the Project

1. Run the `script.py` file to start the ATM system.
2. Enter your 4-digit PIN to authenticate.
3. Select an option from the menu to perform a banking operation.

### Implementation
-----------------

#### Architecture

The project consists of a single Python script `script.py` that implements the ATM system. The script uses the `logging` module to log transactions and the `datetime` module to display the current date and time.

#### Code Structure

The script is organized into the following sections:

* `BankAccount` class: defines the account balance and performs banking operations
* `authenticate` function: authenticates the user using a 4-digit PIN
* [deposit](cci:1://file:///Users/matth/AI%20Folder/github_repo/python_projects/atm_logs/SCRIPT.py:43:2-76:53) function: deposits funds into the account
* `withdraw` function: withdraws funds from the account
* [display](cci:1://file:///Users/matth/AI%20Folder/github_repo/python_projects/atm_logs/solution_sample1.py:67:2-68:48) function: displays the account balance

#### Key Components

* `BankAccount` class: defines the account balance and performs banking operations
* `logger` object: logs transactions using the `logging` module

### Example Use Cases
---------------------

* Deposit $50 into the account
* Withdraw $20 from the account
* Check the account balance

### Transaction Logging
----------------------

The system logs all transactions to a file named `banking.log`. The log file contains the date, time, and details of each transaction.