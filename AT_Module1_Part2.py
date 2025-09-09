"""
This is for assignment 1 part 2.
This script makes the user input their
favorite snowflake and ski resort
They will also enter their deepest
ski day last year along with the number
of ski days they had. It then sums 
the two values together. The highest
number wins!

"""


def get_favorite_snowflake() -> str:
    """
    Prompt the user for their favorite type of snowflake.
    """
    snowflake = input("What is your favorite snowflake?: ")
    print(snowflake)
    return snowflake

def get_favorite_ski_resort() -> str:
    """
    Prompt the user for their favorite type ski resort.
    """
    ski_resort = input("What is your favorite ski resort?: ")
    print(ski_resort)
    return ski_resort


def get_snow_and_ski_stats() -> tuple[int, int]:
    """
    Prompt the user for snow depth and number of ski days.
    """
    snow_depth = int(input("How deep was the snow on the best powder day last year? (in inches): "))
    print(snow_depth)
    ski_days = int(input("How many ski days did you have last year?: "))
    print(ski_days)

    return snow_depth, ski_days  # Remove the earlier return 0, 0


def main() -> None:
    """
    Get stats and compute total.
    """
    get_favorite_snowflake()  # Optional, runs input and print
    get_favorite_ski_resort()  # Optional, runs input and print

    snow_depth, ski_days = get_snow_and_ski_stats()
    total = snow_depth + ski_days

    print(f"Snow depth + ski days = {total}")


# 🔽 This actually runs the program
if __name__ == "__main__":
    main()