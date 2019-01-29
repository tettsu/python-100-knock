import re

sentence = "Chicken Little"

m = re.match("Chi", sentence)
if m:
    print(m.group())