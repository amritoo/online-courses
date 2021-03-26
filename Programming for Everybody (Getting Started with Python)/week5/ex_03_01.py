hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate per hour:")
r = float(rate)

pay = h * r

if h > 40.0:
    pay += (h - 40.0) * (0.5 * r)

print(pay)
