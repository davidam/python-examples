import sexmachine.detector as gender
d = gender.Detector()
if (d.get_gender(u"Bob") == 'male'):
    print("Python")
elif (d.get_gender(u"Sally") == 'female'):
    print("Shell")
else:
    print("PHP")
