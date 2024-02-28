print("[1/2] Loading jz")
from sys import path

path.insert(1, "submodules/jz")
del path
from jz import compress

print("[2/2] Building package")
from os import listdir, chdir

chdir("files")
execstr = ""
for filee in listdir():
    execstr += f", '{filee}'"
execstr = "compress(" + execstr[2:] + ", '../jpkg.jpk')"  # fancy bullshittery
exec(execstr)
print("Done.")
