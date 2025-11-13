#860. Lemonade Change

# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy 
# from you and order one at a time (in the order specified by bills). 
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
# You must provide the correct change to each customer so that the net transaction is that the 
# customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, 
# return true if you can provide every customer with the correct change, or false otherwise.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_five = 0 #Start Count of $5 bills
        count_ten = 0 #Start Count of $10 bills

        for bill in bills: #Iterate through each bill in the array of bills
            if bill == 5: # If Bill of $5, increase count of $5 bills
                count_five += 1 
            elif bill == 10: # If Bill of $10, increase count of $10 bills and decrease count of $5 bills by 1
                if count_five >= 1: 
                    count_five -= 1
                    count_ten += 1
                else:
                    return False #If no $5 bills to give change, we return false, the array cannot provide correct change
            elif bill == 20: #If Bill of $20, we need to give $15 in change 
                if count_ten >=1 and count_five >=1:
                    count_ten -= 1
                    count_five -= 1
                elif count_five >=3: #If no $10 bills, give 3 $5 bills as change for a $20 bill
                    count_five -= 3
                else:
                    return False #If not possible to give correct change, the array cannot provide correct change
                
        return True #Finally, if we can provide correct change to all customers, the algorithm returns true
