try:
    mkdir(path.join(root, "bin/jpkg"))
except FileExistsError:
    pass

for i in [
    "generatelist.py",
    "install.py",
    "uninstall.py",
    "main.py",
]:
    shutil.copy(i, path.join(root, "bin/jpkg", i))

shutil.copy("jpkg.lja", path.join(root, "bin", "jpkg.lja"))
shutil.copy("jpkg.man", path.join(root, "usr/share/man", "jpkg.man"))
