#תרגיל פונקציות
def CelsiusToFahrenheit(c):
    f=(c*9)/5+32
    print(c,"°C is",f,"°F")
def FahrenheitToCelsius(f):
    c=((f-32)*5)/9
    print(f,"°F is",c,"°C")
CelsiusToFahrenheit(25)
FahrenheitToCelsius(77)