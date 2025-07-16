import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
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
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbol = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): #the '_' is an anonymous variable used in python when you loop through something but you dont actually care the counter or the iteration. 
            all_symbol.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbol[:]
        for _ in range(rows):
            value = random.choice(all_symbol)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input('What amount would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number.')
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-"+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines.')
        else:
            print('Please enter a number.')
    return lines

def get_bets():
    while True:
        amount = input('Enter the amount you would like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'The amount must be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Please enter a number.')
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bets()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You don't have enough money! Your total balance: ${balance}.")
        else:
            break
    print(f"you're betting on ${bet} on {lines} lines. Your total bet is ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You Won ${winnings}.")
    print(f"You Won on", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spins = input("Press Enter to Play Again or q to quit: ")
        if spins == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
main()
