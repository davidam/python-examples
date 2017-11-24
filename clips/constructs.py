import clips
clips.Reset()
f0 = clips.Assert("(duck)")
print f0
print f0.Exists()
f0.Retract()
print f0.Exists()
