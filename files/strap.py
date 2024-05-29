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
    shutil.copyfile(i, path.join(root, "bin/jpkg", i))

shutil.copyfile("jpkg.lja", path.join(root, "bin", "jpkg.lja"))
shutil.copyfile("jpkg.man", path.join(root, "usr/share/man", "jpkg.man"))
