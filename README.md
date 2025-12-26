install script

ansible

(chezmoi or stow) + home_manager

~/.nix-profile/bin/alacritty


nix repl
builtins.attrNames ((builtins.getFlake "github:nix-community/nixGL").packages.x86_64-linux)

home-manager news

# Desktop enrironemnt

window manager: Kde, hyprland
file manager: dophine, nautilus
launcher: wofi, Fuzzel
network: nm-applet
audio: pipewire + pavucontrol
logout 
bar: waybar, eww
Compositor: kwin, hyprland
notification: mako
bluetooth: blueman
screenshot: grim + slurp + wl-copy
power menu: wlogout
setting gui: gnome or kde
lock screen: hyprlock
clipboard: wl-clipboard + CopyQ
widget: Quickshell

home-manager switch --flake ~/.config/home-manager#victor

# Resource
https://www.gnu.org/software/stow/manual/stow.pdf

https://www.youtube.com/watch?v=U6reJVR3FfA
https://github.com/omerxx/dotfiles/tree/master

https://www.youtube.com/watch?v=-RkANM9FfTM
https://github.com/logandonley/dotfiles/tree/main

https://www.youtube.com/watch?v=5oXy6ktYs7I
https://shaky.sh/simple-dotfiles/
https://github.com/andrew8088/dotfiles