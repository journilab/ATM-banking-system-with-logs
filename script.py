import random
import sys
import logging
from datetime import datetime

# Logging Configurations
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)  # if not set, default level is WARNING
# logger.setLevel(logging.INFO)  # if not set, default level is WARNING

# option a. set manual logger levels and handlers
stream_hdlr = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_hdlr)
formatter = logging.Formatter("[%(lineno)d]{%(levelname)s}: %(message)s")
stream_hdlr.setFormatter(formatter)

# # external log file handler - uncomment to enable logging to file
# file_hdlr = logging.FileHandler('banking.log')
# file_hdlr.setFormatter(formatter)
# logger.addHandler(file_hdlr)

# option b. set basic config method for both console and file
# logging.basicConfig(filename="banking.log", 
  # level=logging.INFO, format="Line[%(lineno)d] {%(levelname)s}: %(message)s")
# ----------------------------------------- #

class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")
    logger.info("--- >>>> Starting ATM <<<< ---")
    logger.debug(f"Current Acc Balance: ${self.balance}")
    
  def authenticate(self):
    while True:
      pin = int(input("Enter account pin: "))
      logger.debug(f"Pin entered: {pin}")
      if pin != 1234:
        print("Error! Invalid pin. Try again.")
        logger.error(f"Error! Invalid pin.")
      else:
        return None
 
  def deposit(self):
    # Handles deposit transactions
    while True:
      try:
        amount=float(input("Enter amount to be deposited: "))
        logger.debug(f"Amount to deposit: ${amount}")

        
        # Check for invalid amounts (negative)
        if amount < 0:
          print("Error! Cannot withdraw negative amounts.")
          logger.error("Error! Negative withdrawal amount entered.")
          continue  # Go back to start of loop


        # Valid amount - process the deposit
        self.balance += amount
        logger.info(f"Amount Deposited: ${amount}")
        logger.info("Transaction Info:")
        logger.info("Status: Successful")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
        logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
        logger.debug(f"New Acc Balance: ${self.balance}")
        break  # Exit the loop on successful deposit

      # error handling
      except ValueError:
        print("Error! You entered a non-number value to deposit.")
        logger.error("Error! Non valid value entered.")
        logger.info("Transaction Info:")
        logger.info("Status: Failed")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
        logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
        # The next iteration will ask for input again

  def withdraw(self):
    # Handles withdrawl transactions
    while True:
      try:
        amount = float(input("Enter amount to be withdrawn: "))
        logger.debug(f"Amount to withdraw: ${amount}")
        
        # Check for exit condition first
        if amount == 0:
          print("Operation Interrupted!\nExiting Program...")
          logger.info("Withdrawal operation cancelled by user")
          return  # Exit the method entirely
        
        # Check for invalid amounts (negative or insufficient balance)
        if amount < 0:
          print("Error! Cannot withdraw negative amounts.")
          logger.error("Error! Negative value entered.")
          continue  # Go back to start of loop
            
        if self.balance < amount:
          print("Error! Insufficient balance to complete withdraw. Please enter a lower amount or enter \"0\" to end operation!")
          logger.error("Error! Insufficient balance to complete withdraw.")
          continue  # Go back to start of loop

        # Confirmation check
        # print(f"\nYou are about to withdraw: ${amount:.2f}")
        # print(f"Current balance: ${self.balance:.2f}")
        # print(f"Balance after withdrawal: ${self.balance - amount:.2f}")
        logger.warning(f"You are about to withdraw ${amount} from your check account. Please Confirm\
                        \n\t\tCurrent balance: \t\t${self.balance}\n\t\tBalance after withdrawal: \t${self.balance - amount}")
          
        while True:
          confirm = input("Do you want to proceed with this withdrawal? (y/yes/n/no): ").lower().strip()
          logger.debug(f"confirmation input: {confirm}")
          
          if confirm in ['y', 'yes']:
            logger.info(f"User confirmed withdrawal of ${amount}")
            break  # Proceed with withdrawal
          elif confirm in ['n', 'no']:
            print("Withdrawal cancelled.")
            logger.info("Withdrawal cancelled by user confirmation")
            return  # Exit the method
          else:
            print("Please enter 'y' or 'yes' to confirm, or 'n' or 'no' to cancel.")
        
        # Valid withdrawal - process it
        self.balance -= amount
        print("You withdrew: \t\t${amount}".format( amount=amount))
        logger.info(f"You withdrew: ${amount}")
        logger.info("Transaction Info:")
        logger.info("Status: Successful")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
        break  # Exit the loop on successful withdrawal
      
      # Error handling
      except ValueError:
        print("Error! You entered a non-number value to withdraw.")
        logger.error("Error! You entered a non-number value to withdraw.")
        logger.info("Transaction Info:")
        logger.info("Status: Failed")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
        logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
        # Loop will continue and ask for input again
 
  def display(self):
    print("Available Balance: \t${balance}".format(balance=self.balance))
    print("Thank you for using the ATM Depot!")
    logger.debug(f"Account Balance = ${self.balance}")
    logger.info("--- >>>> End ATM Operation <<<< ---")
 
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()