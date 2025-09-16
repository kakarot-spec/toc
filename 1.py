class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'

    def transition(self, symbol):
        if self.state == 'q0':
            print("Push(Z)")
            self.stack.append('Z')  # bottom marker, only once
            if symbol == '0':
                print("Push(0)")
                self.stack.append('0')
                self.state = 'q1'
            elif symbol == '1':
                print("Push(1)")
                self.stack.append('1')
                self.state = 'q2'
            print("Stack:", " ".join(self.stack))

        elif self.state == 'q1':
            if symbol == '0':
                print("Push(0)")
                self.stack.append('0')
            elif symbol == '1':
                if self.stack and self.stack[-1] == '0':
                    print("Pop(0)")
                    self.stack.pop()
                else:
                    self.state = 'reject'
            print("Stack:", " ".join(self.stack))

        elif self.state == 'q2':
            if symbol == '1':
                print("Push(1)")
                self.stack.append('1')
            elif symbol == '0':
                if self.stack and self.stack[-1] == '1':
                    print("Pop(1)")
                    self.stack.pop()
                else:
                    self.state = 'reject'
            print("Stack:", " ".join(self.stack))

    def process_string(self, input_string):
        for i, symbol in enumerate(input_string):
            # avoid pushing Z again after first symbol
            if i == 0:
                self.transition(symbol)
            else:
                if self.state == 'q1' and symbol == '0':
                    print("Push(0)")
                    self.stack.append('0')
                elif self.state == 'q1' and symbol == '1':
                    if self.stack and self.stack[-1] == '0':
                        print("Pop(0)")
                        self.stack.pop()
                    else:
                        self.state = 'reject'
                elif self.state == 'q2' and symbol == '1':
                    print("Push(1)")
                    self.stack.append('1')
                elif self.state == 'q2' and symbol == '0':
                    if self.stack and self.stack[-1] == '1':
                        print("Pop(1)")
                        self.stack.pop()
                    else:
                        self.state = 'reject'
                print("Stack:", " ".join(self.stack))

            if self.state == 'reject':
                return False

        # Accept if only Z remains
        if self.stack == ['Z']:
            self.state = 'accept'
            return True
        return False


if __name__ == "__main__":
    while True:
        string = input("Enter a binary string (equal number of 0’s and 1’s), or 'q' to quit: ")
        if string.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        if all(ch in '01' for ch in string):
            pda = PDA()
            if pda.process_string(string):
                print("? String Accepted by PDA (Final State)\n")
            else:
                print("? String Rejected by PDA\n")
        else:
            print("Invalid input. Please enter a string containing only 0 and 1.\n")