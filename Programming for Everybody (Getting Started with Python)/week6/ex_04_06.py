def computepay(h, r):
    pay = h * r
    if h > 40.0:
        pay += (h - 40.0) * 0.5 * r
    return pay


hrs = input("Enter Hours:")
rate = input("Enter pay per hour:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("NaN")
    quit()

p = computepay(h, r)
print("Pay", p)
