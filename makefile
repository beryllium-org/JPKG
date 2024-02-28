SHELL = bash
all:
	@echo -e "Ljinux hashutils builder.\n\nUsage:\n\tmake package\n\tmake clean"
update_modules:
	@echo "Updating git submodules from remotes.."
	@git submodule update --init --recursive --remote .
	@echo -e "Submodules ready\n\nMake sure to git commit before procceding to make!!"
modules:
	@echo "Preparing git submodules.."
	@git submodule update --init --recursive .
	@echo "Submodules ready"
package: modules
	@python3 -u scripts/make_lib.py
	@python3 -u scripts/generate_package.py
clean:
	@if [ -e "hashutils.jpk" ]; then rm hashutils.jpk; fi
	@if [ -e "./files/__init__.mpy" ]; then rm ./files/__init__.mpy; fi
	@if [ -e "./files/_md5.mpy" ]; then rm ./files/_md5.mpy; fi
	@if [ -e "./files/_sha1.mpy" ]; then rm ./files/_sha1.mpy; fi
	@if [ -e "./files/_sha224.mpy" ]; then rm ./files/_sha224.mpy; fi
	@if [ -e "./files/_sha256.mpy" ]; then rm ./files/_sha256.mpy; fi
	@if [ -e "./files/_sha384.mpy" ]; then rm ./files/_sha384.mpy; fi
	@if [ -e "./files/_sha512.mpy" ]; then rm ./files/_sha512.mpy; fi
