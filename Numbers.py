#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Jan 2022
# This program shows amount of positive, negative and zeros inputted


def main():

    positive_numbers = 0
    negative_numbers = 0
    zeros = 0

    while True:

        number = input(
            "Enter a number to show the amount of +,-,0 numbers or \
'End' to display amounts: "
        )
        try:
            number_as_number = int(number)

            if number_as_number > 0:
                positive_numbers = positive_numbers + 1

            elif number_as_number < 0:
                negative_numbers = negative_numbers + 1

            else:
                zeros = zeros + 1

        except (ValueError):
            if number == "End":
                print(
                    "There is {0} positive numbers, {1} negative numbers, \
and {2} zeros".format(
                        positive_numbers, negative_numbers, zeros
                    )
                )
                break
            else:
                print("Not a valid Input")
    print("\nDone.")

if __name__ == "__main__":
    main()
