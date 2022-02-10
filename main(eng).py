import webbrowser
import random
def op():
    la = str(random.uniform(-90.00000000000000, 90.00000000000000))
    lo = str(random.uniform(-180.00000000000000, 180.00000000000000))
    url = "https://www.google.com.ua/maps/place/" + la + "," + lo
    webbrowser.open(url)
op()
ans = input("Open another page? [y/n] ")
while ans == "y":
    op()
    ans = input("Open another page? [y/n] ")
quit()