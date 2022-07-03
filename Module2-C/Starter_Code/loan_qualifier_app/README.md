# Loan Qualifier Application Program

This program uses python via the terminal to check if a customer qualifies for a loan against our data sheet of possible lenders. The user will input the data location (data/daily_rate_sheet.csv) and then provide us with information to narrow down what loans might be available to the applicant(if any). If qualified, we will provide a list of the banks, maximum loan amount, and interest rate of each loan which can then be saved to a file if the customer wishes.

---

## Technologies

This project leverages python 3.9.12 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
```

---

## Usage

To use our wonderful loan qualifier program please clone the repository and run the **newapp.py** with:

```python
python newapp.py
```

You will be greeted with prompts, *remember the file path for the data is (**data/daily_rate_sheet.csv**)*. And don't worry if you spell it incorrectly the first few times, it allows for a few mistakes.

It will proceed to ask you for financial information, please provide this to the best of your knowledge.

If you qualify for any of our loans, it will print them out for you to view on the screen and give you the option to save them to a file if you wish.

Please name the file anything you like, no judgements here.

---

## Contributors

### Matthew Stream
m.stream3663@gmail.com

[LinkedIn](https://www.linkedin.com/in/matthew-stream-mba-215634102/)

---

## License

MIT
