import clips
clips.Reset()
r1 = clips.BuildRule("duck-rule", "(duck)", "(assert (quack))", "The Duck rule")
print r1.PPForm()
clips.PrintFacts()
clips.PrintRules()
#duck-rule
f1 = clips.Assert("(duck)")
clips.PrintAgenda()
clips.PrintFacts()
clips.Run()
clips.PrintFacts()
