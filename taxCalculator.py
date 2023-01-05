#!/usr/bin/env python3

"""
taxCalculator.py
Ashley Ung 

This program functions as a tax calculator. It will prompt the user to input their taxable income, tax deductions, tax exemptions, and their filing status. The tax calculator will assist users in filling out their 1040 tax income form. This program will calculate the user's tax liability (the combined amount of taxes the user owes the IRS from income tax, capital gains tax, self-employment tax, and any penalities or interest), and the tax refund amount.
"""

# Tax rates and brackets for 2023 (single filer)
singleTaxRates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
singleTaxBrackets = [0, 10275, 41775, 89075, 170050, 215950, 539900]

# Tax rates and brackets for 2023 (married filing jointly)
jointTaxRates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
jointTaxBrackets = [0, 20550, 83550, 178150, 340100, 431900, 647850]

# Tax rates and brackets for 2023 (married filing separately)
separateTaxRates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
separateTaxBrackets = [0, 10275, 41775, 89075, 170050, 215950, 323925]

# Tax rates and brackets for 2023 (head of household)
headTaxRates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
headTaxBrackets = [0, 14650, 55900, 89050, 170050, 215950, 539900]

# Tax rates and brackets for 2023 (qualifying widow)
widowTaxRates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
widowTaxBrackets = [0, 20550, 83550, 178150, 340100, 431900, 647850]

# Prompt the user to enter their filing status, income, tax deductions, tax exemptions, & tax paid 
filingStatus = input ("Enter your filing status (single, married filing jointly, married filing separately, head of household, 'widowed'): ")
combindedIncome = float (input ("Enter your combined (nontaxable and taxable) income: "))
taxedDeductions = float (input ("Enter your tax deductions: "))
taxedExemptions = float (input ("Enter your tax exemptions: "))
taxPaid = float (input ("Enter the amount of tax you have already paid: "))

# Calculate the taxable income
income = combindedIncome - taxedDeductions - taxedExemptions

# Calculate the tax liability based on the filing status and income
if filingStatus == "single":
	tax = 0
	for i in range (len (singleTaxRates)):
		if income > singleTaxBrackets[i]:
			tax += (income - singleTaxBrackets[i]) * singleTaxRates[i]
			income = singleTaxBrackets[i]
	print ("Your tax liability is: $" + str (tax))
elif filingStatus == "married filing jointly":
	tax = 0
	for i in range (len (jointTaxRates)):
		if income > jointTaxBrackets[i]:
			tax += (income - jointTaxBrackets[i]) * jointTaxRates[i]
			income = jointTaxBrackets[i]
	print ("Your tax liability is: $" + str (tax))
elif filingStatus == "married filing separately":
	tax = 0
	for i in range (len (separateTaxRates)):
		if income > separateTaxBrackets[i]:
			tax += (income - separateTaxBrackets[i]) * separateTaxRates[i]
			income = separateTaxBrackets[i]
	print ("Your tax liability is: $" + str (tax))
elif filingStatus == "head of household":
	tax = 0
	for i in range (len (headTaxRates)):
		if income > headTaxBrackets[i]:
			tax += (income - headTaxBrackets[i]) * headTaxRates[i]
			income = headTaxBrackets[i]
	print ("Your tax liability is: $" + str (tax))
elif filingStatus == "widowed": 
	tax = 0
	for i in range (len (widowTaxRates)):
		if income > widowTaxBrackets[i]:
			tax += (income - widowTaxBrackets[i]) * widowTaxRates[i]
			income = widowTaxBrackets[i]
	print ("Your tax liability is: $" + str (tax))
else:
	print ("Invalid filing status")
# Calculate tax refund amount 
taxRefund = tax - taxPaid # tax in this case is the tax liability 
print ("Your tax refund amount is: $" + str (taxRefund)) 
