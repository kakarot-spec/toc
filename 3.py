class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'  # start state

    def transition(self, symbol):
        # q0: initial state
        if self.state == 'q0':
            if symbol == '0':
                print("Push(X)")
                self.stack.append('X')  # push for 0
                self.state = 'q0'       # stay in q0 for more 0's
            elif symbol == '1':
                if self.stack:
                    print("Pop(X)")
                    self.stack.pop()    # start popping for 1's
                    self.state = 'q1'   # move to q1
                else:
                    self.state = 'reject'  # more 1's than 0's
            print("Stack:", " ".join(self.stack) if self.stack else "Empty")

        # q1: reading 1's
        elif self.state == 'q1':
            if symbol == '1':
                if self.stack:
                    print("Pop(X)")
                    self.stack.pop()    # pop for each 1
                else:
                    self.state = 'reject'  # more 1's than 0's
            elif symbol == '0':
                self.state = 'reject'      # 0 after 1 not allowed
            print("Stack:", " ".join(self.stack) if self.stack else "Empty")

    def process_string(self, input_string):
        for symbol in input_string:
            if symbol not in '01':
                self.state = 'reject'
                break
            self.transition(symbol)
            if self.state == 'reject':
                return False

        # Accept if stack is empty and final state q1 (all 0's matched with 1's)
        return self.state == 'q1' and not self.stack


if __name__ == "__main__":
    print("PDA: Accepts strings of the form 0^n1^n (n ≥ 1) by FINAL STATE.\n")

    while True:
        string = input("Enter a binary string (or 'q' to quit): ")
        if string.lower() == 'q':
            print("Exiting program. Goodbye!")
            break

        pda = PDA()
        if pda.process_string(string):
            print("✅ String is ACCEPTED by the PDA (final state).\n")
        else:
            print("❌ String is REJECTED by the PDA.\n")