'''
Calculate net salary
where net salary = gross salary + allowance – deduction.
Allowances are 10% while deductions are 3% of gross salary.'''
g=float(input("enter your gross salary:"))
a=g/10
d=g*3/10
s=g+a-d
print("your net salary is :",s)
