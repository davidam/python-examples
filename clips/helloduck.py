import clips
clips.Reset()
clips.Assert("(duck)")
clips.BuildRule("duck-rule", "(duck)", "(assert (quack))", "the Duck Rule")
clips.PrintRules()
clips.PrintAgenda()
clips.PrintFacts()
clips.Run()
clips.PrintFacts()
