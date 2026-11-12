# OOP Bank Account System

A small Python mini-project that demonstrates object-oriented programming using a bank account hierarchy and a dataset analysis script.

## Project Overview

This project contains:

- `bank_account.py` : defines bank account classes and inheritance-based behavior
- `main_bank.py` : demonstrates deposit, withdrawal, and interest logic
- `dataset_analysis.py` : loads and analyzes the Titanic dataset using pandas and NumPy
- `titanic.csv` : sample Titanic dataset used for analysis

## Features

- `BankAccount` base class with balance validation
- `SavingsAccount` with interest calculation
- `CurrentAccount` with an overdraft limit
- Transaction history tracking for each account
- Polymorphism through account withdrawal behavior
- Dataset inspection, cleaning, and summary analysis

## How to Run

### Bank account demo

```bash
python main_bank.py
```

### Dataset analysis

```bash
python dataset_analysis.py
```

## Requirements

Make sure Python is installed and install these packages if needed:

```bash
pip install pandas numpy
```


