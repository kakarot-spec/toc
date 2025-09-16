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
        self.stack.append('Z')  # Bottom of stack marker
        
        for i, symbol in enumerate(input_string):
            # Record stack state before processing this symbol
            stack_before = self.get_stack_string()
            
            if self.state == 'q0':
                if symbol in ['a', 'b']:
                    self.push(symbol)
                elif symbol == 'c':
                    self.state = 'q1'
                else:
                    return False
                    
            elif self.state == 'q1':
                if symbol in ['a', 'b']:
                    if self.stack and self.stack[-1] == symbol:
                        self.pop()
                    else:
                        return False
                else:
                    return False
                    
            # Record stack state after processing this symbol
            self.history.append(f"Stack: {self.get_stack_string()}")
            
        # Check if we're in final state with only Z in stack
        if self.state == 'q1' and len(self.stack) == 1 and self.stack[0] == 'Z':
            return True
        return False
        
    def display_history(self):
        for entry in self.history:
            print(entry)


def main():
    print("PDA: Accepts strings of the form wcw^r, where w ∈ {a,b}, by final state.\n")
    
    while True:
        input_str = input("Enter a string of a, b, and c: ")
        
        if not all(char in 'abc' for char in input_str):
            print("Invalid input! Only 'a', 'b', and 'c' are allowed.")
            continue
            
        pda = PDA()
        result = pda.process(input_str)
        
        pda.display_history()
        
        if result:
            print("✓ String Accepted by PDA (Final State)")
        else:
            print("✗ String Rejected by PDA")
            
        choice = input("Do you want to check another string? (y/n): ")
        if choice.lower() != 'y':
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
    