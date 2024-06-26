rename_process("jpkg")
be.api.setvar("return", "1")
vr("opts", be.api.xarg())
vr("errored", False)

vr("jpkg_version", 2)

if len(vr("opts")["w"]) > 1 and vr("opts")["w"][0] == "install":
    be.api.subscript("/bin/jpkg/install.py")
elif len(vr("opts")["w"]) > 1 and vr("opts")["w"][0] == "uninstall":
    be.api.subscript("/bin/jpkg/uninstall.py")
elif len(vr("opts")["w"]) is 1 and vr("opts")["w"][0] == "list":
    vr("pkgs", listdir(pv[0]["root"] + "/etc/jpkg/installed"))
    vr("pkgs").sort()
    for pv[get_pid()]["package"] in vr("pkgs"):
        with be.api.fs.open(pv[0]["root"] + "/etc/jpkg/installed/" + vr("package")) as pv[
            get_pid()
        ]["manifest_f"]:
            from json import load

            vr("manifest", load(vr("manifest_f")))
            del load
            term.write(
                colors.green_t
                + vr("manifest")["package_name"]
                + colors.endc
                + "/"
                + str(vr("manifest")["version"][0])
                + "."
                + str(vr("manifest")["version"][1])
                + "."
                + str(vr("manifest")["version"][2])
                + " [Installed]"
            )
    be.api.setvar("return", "0")
else:
    be.based.run("man jpkg")
    be.api.setvar("return", "1")
