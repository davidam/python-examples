def addf(a, b):
    return a + b
print addf("egg", "spam")
print addf(2, 4)

import clips
clips.RegisterPythonFunction(addf)
print clips.Eval('(python-call addf "egg" "spam")')
print clips.Eval('(python-call addf 2 4)')
