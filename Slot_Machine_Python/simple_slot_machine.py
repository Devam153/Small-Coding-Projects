import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)
    
    return winnings , winning_lines


def get_slot_machine_spin(rows,cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns
            
def print_slot_machine(columns):
    for rows in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[rows], end = " | ")
            else:
                print(column[rows])
    print()

def deposit():
    while True:
        amount = input("\nPlease enter the amount u wanna deposit? ($): ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number.")
    return amount  


def get_no_of_lines():
    while True:
        lines = input("\nPlease enter the no. of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("lines must be between from 1 to " + str(MAX_LINES))
        else:
            print("please enter a number.")
    return lines  
    


def get_bet():
    while True:
        amount = input("\nPlease enter the amount u wanna bet on each line? ($): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number.")
    return amount  

def spin(balance):
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount.\nYour current balance is ${balance}")
            print("please bet under your current balance.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines.\nTotal bet is equal to : {bet*lines}")
    
    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines: ", *winning_lines)
    return winnings - total_bet

def main():

    balance = deposit()
    while True:
        print("current balance is $", balance)
        answer = input("Press enter to play (Q to quit)....")
        print()
        if answer.lower() == 'q':
            break
        balance += spin(balance)
        if balance == 0:
            print("uh-oh. no more balance left, try again later.")
            break
    print(f"you are left with ${balance}")
main()