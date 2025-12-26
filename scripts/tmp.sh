# Execute command
# Undo command
# ln -sf /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime
# hwclock --systohc

# - name: Disable root SSH login
#   ansible.builtin.lineinfile:
#     path: /etc/ssh/sshd_config
#     regexp: '^#?PermitRootLogin'
#     line: 'PermitRootLogin no'
#     create: yes
#     backup: yes
