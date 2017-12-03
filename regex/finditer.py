import re
text = "He was carefully disguised but captured quickly by police."
for m in re.finditer(r"\w+ly", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
