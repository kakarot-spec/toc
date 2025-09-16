class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'
        self.history = []
        
    def push(self, symbol):
        self.stack.append(symbol)
        self.history.append(f"Push({symbol})")
        
    def pop(self):
        if self.stack:
            symbol = self.stack.pop()
            self.history.append(f"Pop({symbol})")
            return symbol
        return None
        
    def get_stack_string(self):
        if not self.stack:
            return "Empty"
        return " ".join(reversed(self.stack))
        
    def process(self, input_string):
        self.__init__()  # Reset for new processing
        self.history.append("Push(Z)")
        self.push('Z')  # Bottom of stack marker
        
        for symbol in input_string:
            # Record stack state before processing this symbol
            stack_before = self.get_stack_string()
            
            if self.state == 'q0':
                if symbol == 'a':
                    self.push('X')
                elif symbol == 'b':
                    if self.stack and self.stack[-1] == 'X':
                        self.state = 'q1'
                    else:
                        return False
                else:
                    return False
                    
            elif self.state == 'q1':
                if symbol == 'b':
                    # Continue reading b's without changing stack
                    pass
                elif symbol == 'c':
                    if self.stack and self.stack[-1] == 'X':
                        self.pop()
                        self.state = 'q2'
                    else:
                        return False
                else:
                    return False
                    
            elif self.state == 'q2':
                if symbol == 'c':
                    if self.stack and self.stack[-1] == 'X':
                        self.pop()
                    else:
                        return False
                else:
                    return False
                    
            # Record stack state after processing this symbol
            self.history.append(f"Stack: {self.get_stack_string()}")
            
        # Check if we're in final state with only Z in stack
        if self.state in ['q1', 'q2'] and len(self.stack) == 1 and self.stack[0] == 'Z':
            return True
        return False
        
    def display_history(self):
        for entry in self.history:
            print(entry)


def main():
    print("PDA: Accepts strings of the form a^n b^m c^n where n,m>=1\n")
    
    while True:
        input_str = input("Enter a string (a's, b's, and c's): ")
        
        if not all(char in 'abc' for char in input_str):
            print("Invalid input! Only 'a', 'b', and 'c' are allowed.")
            continue
            
        pda = PDA()
        result = pda.process(input_str)
        
        pda.display_history()
        
        if result:
            print("✓ String Accepted by PDA")
        else:
            print("✗ String Rejected by PDA")
            
        choice = input("Do you want to check another string? (y/n): ")
        if choice.lower() != 'y':
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()