import subprocess
from pathlib import Path

from src.recipe.foundation import x
from src.recipe.schema import USER

user="victor"
root=Path.cwd().parent / "root"


def install_pkgs(tool, pkgs):
    command = [tool, "-S", *pkgs]

    if tool == "pacman":
        command.insert(0, "sudo")

    print(command)

    # subprocess.run(command, check=True)

def tmp():
    for name, recipe in x.items():
        aor=[]
        aur=[]
        for pkg in recipe.pkg:
            if(pkg[1]==USER):
                aur.append(pkg[0]);
            else:
                aor.append(pkg[0])

        if(aor):
            install_pkgs("pacman", aor)

        if(aur):
            install_pkgs("paru", aor)


        if recipe.manual:
            print(f"Recipe {name} config manually")
            continue

        for config in recipe.config:
            if(type(config)==str):
                target = Path(config)
                if(config[0]=='~'):
                    source=root / "home" / user / config[2:]
                else:
                    source= root / config[1:]

                if not target.exists():
                    print("target file did not exists!")

                if not source.exists():
                    print("source file did not exists!")

                # is that we just need stow all of user config?

                print(source)
            else:
                print(config)
                subprocess.run(config, check=True)


def main():
    print("Hello from recipes-1!")


if __name__ == "__main__":
    main()

    print(root)

    tmp()
