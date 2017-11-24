import clips
clips.DebugConfig.ActivationsWatched = True
r0 = clips.BuildRule("sayhello", "(hello)",
                         '(printout stdout "hello, world!" crlf)')
print r0.PPForm()
clips.Assert("(hello)")
t = clips.TraceStream.Read()
print t
clips.Run()
t = clips.StdoutStream.Read()
print t
