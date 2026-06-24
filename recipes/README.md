source .venv/bin/activate

repo-> installation(aor, aur, manual with script-but it mean we need more deps?)

Funtion to add new config

repo->installation? and where we put it? ()
installtion-> initialize - config_cmd?
low level but pacman only? those behind the screen, passive active, rarely direct use thing
- systemd, glibc, sudo, base-devel, git
application: assume those below exist and not listed as dependency? gui, and cmd
desktop shell
develope
sudo, pacman

A recipe must be fully reproduce

# Scope
Arch base distro only? or arch only?

# Specification
PkgSpec:
- contain property: name, repo, tag, config, unit
- contain every posible choice of property. Now we only have config variation but we expect to have repo(at least) too(aor, aur, manual)

PkgVar:
- a specific variation got from select choice from coreponding PkgSpec
- If PkgVar.config do not exist, it will use the PkgSpec.config.default
- If PkgVar.units do not exist, it will use all the units in PkgSpec.units

PkgRecipe:
- a complete functioning of a package: core, enhancer, installation, env_vars
- enhacer is plugin to core, make core better in it main functioning
- enhancer is optional of core but not vice versa?
- if a package require the core, we consider it peer-which handle diffirect aspect, not enhancer
- enhancer now PkgRecipe, that allow better extext ability and seem to be a proper way. But since we want to limit enhacer recipe to have no dep, PkgVar may consider? But installation must come with PkgVar to make sense, we should use PkgRecipe but limit no enhancer?
- Should we create a PkgInstallation?(installation script, env_vars)
- recipe in enhancer may contain enhancer it self, but if an enhacer is direct use some where, only list the core, not it enhancer
- enhancer of core is minimal to function the core

UsageRecipe:
- Union of many package to serve a specific purpose: pkgs, installation(change to usage?), env_vars?
- If 1 or some recipe appear together too much, separeate them in to another UsageRecipe, and just refer the core package in enhancer field.
