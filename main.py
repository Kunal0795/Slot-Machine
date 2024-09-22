import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines =[]
    for line in range (lines):
        symbol = columns[0][line]
        for column in columns:                      # for - else statement
            symbols_to_check = column[line]
            if symbol != symbols_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings , winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        current_symbols= all_symbols[:]             #[:] used beacuase we needed to make a copy . we use this because
                                                    #if we wrote only all_symbols it would take reference instead of making a copy.
                                                    # : this is a slice operator.
        for row in range (rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
     for row in range (len (columns[0])):           #transposing the columns 
        for i,column in enumerate(columns):
            if i != len (column) -1:
                 print(column[row], end=" | ")
            else:
                print(column[row] , end = "")

        print()

                                               
def deposit():
    while True:
        amount = input ("What would you like to deposit ? $$ :")
        if amount.isdigit():
            amount = int(amount)
            if amount> 0:
                break
            else:
                print("Amount must be greater than 0.")
        else: 
            print("Please enter a number." )
    return amount

def get_number_of_lines():
    while True:
        lines  = input ("Enter the number of lines to bet on (1-" + str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines :")
        else: 
            print("Please enter a number." )
    return lines

def get_bet():
    while True:
        amount = input ("What would you like to bet on each line? $$ :")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number." )
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet= get_bet()
        total_bet = bet * lines

        if total_bet >  balance:
            print (f"Amount not sufficient . Your current balance is {balance}.")
        else:
            break
    
    print (f"you are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You Won {winnings}.")
    print(f"You won on", *winning_lines)        # '*' this is a splat operator or unpack operator
                                        # It's going to pass every single line from winning_lines list to print function 
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input ("Press Enter to play (q to quit).")
        if answer == "q":
            break
        else :
           balance += spin(balance)
    print (f"You are left with ${balance}.")
    
main()
