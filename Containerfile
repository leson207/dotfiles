FROM archlinux/archlinux

# Ansible
RUN pacman -Sy --noconfirm ansible
RUN echo "Ansible installation complete!"

COPY install/archlinux/playbooks/system_administration.yaml playbooks/system_administration.yaml
RUN ansible-playbook -vvv playbooks/system_administration.yaml

COPY install/archlinux/playbooks/development.yaml playbooks/development.yaml
RUN ansible-playbook -vvv playbooks/development.yaml

COPY install/archlinux/playbooks/package_management.yaml playbooks/package_management.yaml
RUN ansible-playbook -vvv playbooks/package_management.yaml

# COPY install/archlinux/playbooks/booting.yaml playbooks/booting.yaml
# RUN ansible-playbook -vvv playbooks/booting.yaml

# COPY install/archlinux/playbooks/draft.yaml playbooks/draft.yaml
# RUN ansible-playbook -vvv playbooks/draft.yaml

# RUN ansible-playbook -vvv playbooks/post-install.yaml

# # Nix and home-manager (for single user)
# RUN useradd -m victor
# RUN mkdir -m 0755 /nix && chown -R victor:victor /nix
# USER victor

# RUN curl -L https://nixos.org/nix/install | sh -s -- --no-daemon
# RUN echo "Nix installation complete!"

# ENV PATH=/home/victor/.nix-profile/bin:/home/victor/.nix-profile/sbin:$PATH
# RUN nix-channel --add https://github.com/nix-community/home-manager/archive/master.tar.gz home-manager
# RUN nix-channel --update

# ENV USER=victor
# RUN nix-shell '<home-manager>' -A install
# RUN rm ~/.config/home-manager/home.nix
# RUN echo "Home-manager installation complete!"

RUN pacman -Scc --noconfirm

CMD ["/bin/bash"]
