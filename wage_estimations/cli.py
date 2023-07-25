# Standard Imports
from simple_term_menu import TerminalMenu

from wage_estimations.estimation import Estimation


# Local Imports

# External Imports


def interactive_cli():
    print("Wage Calculation")
    print()
    print("Lets calculate the earnings from amount of:")

    options = [
        "Per Hour",
        "Per Week",
        "Per Month",
        "Per Year",
    ]
    menu = TerminalMenu(options)

    index = menu.show()
    amount = float(input("With the amount of: "))

    estimation: Estimation
    match index:
        case 0:
            estimation = Estimation.with_per_hours(amount, 1)
        case 1:
            estimation = Estimation.with_per_days(amount, 1)
        case 2:
            estimation = Estimation.with_per_weeks(amount, 1)
        case 3:
            estimation = Estimation.with_per_months(amount, 1)
        case 4:
            estimation = Estimation.with_per_years(amount, 1)
        case _:
            raise TypeError(f"Option not implemented: {options[index]}")

    print(estimation)

