# family mall shopping


class familyShopping():

    def __init__(self, James, Swane, Tim):
        self.James = James
        self.Swane = Swane
        self.Tim = Tim

    def jamesSpending(self):
        print("\nThis is what james spent")
        self.James += float(input("How much did james spent in total?: "))
        print(f"James total spent is ${round(self.James, 2)}")

    def swaneSpending(self):
        print("\nThis is what swane spent")
        self.Swane += float(input("How much did swane spent in total?: "))
        print(f"Swane total spent is ${round(self.Swane, 2)}")

    def timSpending(self):
        print("\nThis is what tim spent")
        self.Tim += float(input("How much did tum spent in total?: "))
        print(f"Tim total spent is ${round(self.Tim, 2)}")

family_shopping = familyShopping(0, 0, 0)
def run():
    while True:
        response = input(
        "Proceed forward to see how much they alls spent: forward / quit:\n"
        ).lower()

        if response == "forward":
            family_shopping.jamesSpending()
            family_shopping.swaneSpending()
            family_shopping.timSpending()
        elif response == "quit":
            print("Goodbye!")
            break
        else:
            print("invalid. select different option.")
run()