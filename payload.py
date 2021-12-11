import os
import webbrowser

for a in ["open -a Calculator", "gnome-calculator", "kcalc", "xcalc", "calc"]:
  if os.system(a) == 0:
    break
else:
  webbrowser.open("https://www.google.com/search?q=calculator")
