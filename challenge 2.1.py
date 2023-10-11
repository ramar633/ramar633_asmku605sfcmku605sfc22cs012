class BankAccount:
  def__init__(self,account_number,account_holder_name,initial _balance=0.0):
  self._account_number=account_number
  self._account_holder_name=account_holder_name
  self._account_balance=initial_balance
  def deposit(self,amount):
    if amount>0:
      self.__account_balance+=amount
      print("deposited${amount:.2f}into account{self.__account_number}")
    else:
      print("invalid deposit amount.please deposit a positive amount.")
      def withdraw(self,amount):
        if amount>0:
          if self.__account_balance>=amount:
            self.__account_balance-=amount
            print("withdrew${amount:.2f}from account{self._account_number}")
          else:
            print("insufficient balance.cannot withdraw.")
          else:
          print("invalid withdrawal amount.please withdraw a positive amount.")
        def display_balance(self):
          print("account{self._account_number}balance:${self._account_balance:.2f}")
          #testing the bank account class
          if_name_=="_main_":
          #create a bank account instance
          account1=bank account("123456","john doe",1000.0)
          #deposit money
          account1.deposit(500.0)
          #withdraw money
          account1.withdraw (200.0)
          #display balance
          account1.display_balance()