bill = float(input("What is the bill amount ?\n"))
members = int(input("What is the number of members to split the bill?\n"))
amt_per_person = bill / members
amt_per_p = round(amt_per_person, 2)
print("the amount per person is : ", amt_per_p)