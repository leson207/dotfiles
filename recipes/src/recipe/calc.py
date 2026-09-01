from subprocess import run

base={}

def get_installed_pkgs() -> list[str]:
    return run(
        ["pacman", "-Qeq"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()

def get_declared_pkgs() -> list[str]:
    L=[]
    for val in base.values():
        for pkg in val.pkg:
            L.append(pkg[0])

    return L

def get_uninstalled_pkgs(installed, declared) -> list[str]:
    declared = set(declared)
    installed = set(installed)

    uninstalled = sorted(declared - installed)

    print("Uninstalled packages:")
    for pkg in uninstalled:
        print(pkg)

    return uninstalled

def get_undeclared_pkgs(installed, declared) -> list[str]:
    declared = set(declared)
    installed = set(installed)

    undeclared = sorted(installed - declared)

    print("Undeclared packages:")
    for pkg in undeclared:
        print(pkg)

    return undeclared

declared_pkgs= get_declared_pkgs()
installed_pkgs = get_installed_pkgs()
get_undeclared_pkgs(installed_pkgs, declared_pkgs)
