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
