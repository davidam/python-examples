filepath="README.org"
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        print("Line {}: {}".format(cnt, line))
