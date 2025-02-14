# forces user to enter a mutliple of 6 number, use try, expcept to chat invalid inputs, return that number

def multiple_of_6():
    """
    Forces user to enter a multiple of 6 number, uses try
    :return:
    """
    while True:
        try:
            number = int(input('Enter a multiple of 6: '))
            if number % 6 == 0:
                print(number)
                break
            else:
                print('Invalid input')
        except ValueError:
            print('Invalid input')

multiple_of_6()


# def multiple_of_6():
#     """
#     Returns a multiple of 6
#     :return: int
#     """
#     try:
#         n = int(input("Please give  me a multiple of 6: "))
#         if n % 6 == 0:
#             return n
#         # if n /6 == n//6:
#         #     return n
#
#     except ValueError:
#         print("That is not a valid number")

