

import re

filepath="surnamesmin.csv"
surnames = ""
with open(filepath) as fp:
    for line in fp:
        if re.match(r"(\w+),(\w+)", str(line)):
            m4 = re.match(r"(\w+),(\w+)", str(line))
            json_content = '[{\n'
            json_content += '  "name": ' + m4.group(1) + ',\n'
            json_content += '  "frequency": ' + m4.group(2) + '\n'
            json_content += '}]'
            print(json_content)
            json_file = m4.group(1) + '.json'
            print(json_file)
            with open(json_file, "w") as jf:
                jf.writelines(json_content)
            jf.close()
print("---------------------------------------------------------------------------")
fp.close()

