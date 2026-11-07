'''
def add():
    a = 10
    b=20
    print(a+b)
add()


def add(a,b):
    print(a+b)

add(10,20)


def add():
    a = 10
    b=20
    return a+b
    print('hii')

print(add())


def add(a,b):
    return a+b

print(add(10,20))
'''
'''
**Question 1: Electricity Bill Calculation**

Write a Python program using a function without arguments and without a return value
to calculate an electricity bill.

The function should:
- Store the number of units consumed as `185`.
- Calculate the bill at ₹6 per unit.
- Add a fixed service charge of ₹120.
- Print the total electricity bill.
'''

def electricity_bill():
    units = 185
    rate = 6
    service_charge = 120
    total = units * rate + service_charge
    print("Total electricity bill: ₹", total)

electricity_bill()

'''
**Question 2: Employee Attendance and Salary**

Write a Python program using a function without arguments and without a return value.

The function should:
- Store the employee's monthly salary as ₹28,000.
- Store the number of absent days as `3`.
- Consider the total working days as `28`.
- Calculate the salary deduction based on the absent days.
- Print the salary after deducting the amount for absent days.

Assume the deduction per absent day is calculated using the monthly salary divided
by the total working days.

## 2. Function With Arguments and Without Return Value
'''


def employee_salary():
    salary = 28000
    absent_days = 3
    working_days = 28
    deduction_per_day = salary / working_days
    deduction = deduction_per_day * absent_days
    final_salary = salary - deduction
    print("Salary after deduction: ₹", final_salary)

employee_salary()


'''
**Question 3: Online Examination Result**

Write a Python program using a function with arguments and without a return value
to calculate and display a student's examination result.

Pass the marks of three subjects as arguments.

The function should:
- Calculate the total marks.
- Calculate the average marks.
- Print the total and average.
- Print the result as `Pass` if the average is at least 40; otherwise, print `Fail`.

Use the marks `78`, `65`, and `32` while calling the function.
'''

def exam_result(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    print("Total marks:", total)
    print("Average marks:", round(average, 2))
    if average >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

exam_result(78, 65, 32)

'''
**Question 4: Courier Delivery Charges**

Write a Python program using a function with arguments and without a return value to calculate courier delivery charges.

Pass the parcel weight in kilograms and the delivery distance in kilometres as arguments.

Apply the following conditions:
- Charge ₹50 for the first kilogram.
- Charge ₹20 for every additional kilogram.
- Charge ₹5 per kilometre when the distance exceeds 100 km.
- Add all applicable charges and print the final delivery amount.

Use a parcel weight of `4` kg and a delivery distance of `150` km.

Assume the parcel weight is a whole number of kilograms.

## 3. Function Without Arguments and With Return Value
'''

def courier_charges(weight, distance):
    charge = 50                          # first kg
    if weight > 1:
        charge += (weight - 1) * 20      # additional kgs
    if distance > 100:
        charge += distance * 5           # distance charge
    print("Final delivery amount: ₹", charge)

courier_charges(4, 150)

'''
**Question 5: Shopping Discount Calculation**

Write a Python program using a function without arguments but with a return value.

The function should:
- Store the original bill amount as ₹4,850.
- Calculate a discount of 12% on the bill.
- Return the final amount after deducting the discount.

Call the function and display the returned amount outside the function.
'''
def shopping_bill():
    bill = 4850
    discount = bill * 12 / 100
    final_amount = bill - discount
    return final_amount

amount = shopping_bill()
print("Final amount after discount: ₹", amount)

'''
**Question 6: Water Tank Capacity**

Write a Python program using a function without arguments but with a return value to calculate the capacity of a cylindrical water tank.

The function should:
- Store the radius as `7` metres.
- Store the height as `10` metres.
- Calculate the tank's volume using the formula:

  Volume = 3.14 × radius × radius × height

- Return the calculated volume.

Call the function and display the returned capacity in cubic metres.

## 4. Function With Arguments and With Return Value
'''
def tank_capacity():
    radius = 7
    height = 10
    volume = 3.14 * radius * radius * height
    return volume

capacity = tank_capacity()
print("Tank capacity:", capacity, "cubic metres")

'''
**Question 7: Monthly Savings Calculator**

Write a Python program using a function with arguments and with a return value.

Pass the monthly income and monthly expenses as arguments.

The function should:
- Calculate the monthly savings.
- Calculate the yearly savings, assuming the monthly savings remain constant.
- Return the yearly savings.

Call the function using a monthly income of ₹45,000 and monthly expenses of ₹32,500,
then display the returned yearly savings.
'''

def yearly_savings(income, expenses):
    monthly_savings = income - expenses
    yearly = monthly_savings * 12
    return yearly

result = yearly_savings(45000, 32500)
print("Yearly savings: ₹", result)

'''
*Question 8: Multi-Item Order Calculation**

Write a Python program using a function with arguments and with a return value
to calculate the final amount payable for an order.

Pass the price of three different items as arguments.

The function should:
- Calculate the total price of the three items.
- Apply a discount of 10% if the total exceeds ₹2,000.
- Otherwise, apply a discount of 5%.
- Return the final amount after the discount.

Call the function with item prices of ₹850, ₹720, and ₹650, then display
the returned amount.
'''

def order_amount(item1, item2, item3):
    total = item1 + item2 + item3
    if total > 2000:
        discount = total * 10 / 100
    else:
        discount = total * 5 / 100
    final_amount = total - discount
    return final_amount

amount = order_amount(850, 720, 650)
print("Final amount payable: ₹", amount)
