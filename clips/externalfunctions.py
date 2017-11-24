import clips
def py_square(x):
        return x * x
clips.RegisterPythonFunction(py_square)
print clips.Eval("(python-call py_square 7)")
print clips.Eval("(python-call py_square 0.7)")
