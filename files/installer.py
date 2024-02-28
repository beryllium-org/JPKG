be.based.run("mkdir /bin/jpkg")
for pv[get_pid()]["f"] in [
    "generatelist.py",
    "install.py",
    "uninstall.py",
    "main.py",
]:
    be.based.run("cp " + vr("f") + " /bin/jpkg/" + vr("f"))

be.based.run("cp jpkg.lja /bin/jpkg.lja")
be.based.run("cp jpkg.man /usr/share/man/jpkg.man")
be.api.setvar("return", "0")
