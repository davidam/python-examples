#!/usr/bin/python
# -*- coding: utf-8 -*-

def test_var_kwargs(farg, **kwargs):
    print("formal arg:" + str(farg))
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))
    if ("myarg2" in kwargs):
        print(str(kwargs["myarg2"]))

test_var_kwargs(farg=1, myarg2="two", myarg3=3)
