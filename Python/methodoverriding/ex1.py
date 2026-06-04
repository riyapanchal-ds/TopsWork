class Bank():
    def interest(self):
        print("genral bank interest rate:")

class SBI(Bank):
    def interest(self):
        print("SBI interest is 7%")
                
class HDFC(Bank):
    def interest(self):
        print("HDFC interest is 8%")
sbi=SBI()
hdfc=HDFC()

sbi.interest()
hdfc.interest()