import androidhelper

droid = androidhelper.Android()
line = droid.dialogGetInput()
s = "Hello, %s" % (line.result)
droid.makeToast(s)