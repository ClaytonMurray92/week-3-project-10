hourlyWages = float(input("Enter the hourly wages: "))
regularHours = float(input("Enter the total number of regular hours: "))
overtimeHours = float(input("Enter the total number of overtime hours "))
regularPay = hourlyWages * regularHours
overtimePay = overtimeHours * (1.5 * regularHours)
totalPay = regularPay + overtimePay
print("The total pay for the week is: ", totalPay)
