import clips
clips.Reset()
t0 = clips.BuildTemplate("person", """
    (slot name (type STRING))
    (slot age (type INTEGER))
""", "template for a person")
print t0.PPForm()
f1 = clips.Fact(t0)
f1_slotkeys = f1.Slots.keys()
print f1_slotkeys
f1.Slots['name'] = "Grace"
f1.Slots['age'] = 24
print f1.PPForm()
clips.PrintFacts()
f1.Assert()
clips.PrintFacts()
f1.Retract()
clips.PrintFacts()
