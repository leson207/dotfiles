# 1. Enable systemd-resolved
systemctl enable --now systemd-resolved

# 2. Edit /etc/systemd/resolved.conf
nano /etc/systemd/resolved.conf

[Resolve]
DNS=45.90.28.0#YOUR_ID.dns.nextdns.io
DNS=2a07:a8c0::#YOUR_ID.dns.nextdns.io
DNS=45.90.30.0#YOUR_ID.dns.nextdns.io
DNS=2a07:a8c1::#YOUR_ID.dns.nextdns.io
DNSOverTLS=yes

# 3. Point resolv.conf to systemd-resolved
ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf

# 4. Tell NetworkManager to hand off DNS to systemd-resolved
nano /etc/NetworkManager/conf.d/dns.conf

[main]
dns=systemd-resolved

# 5. For each WiFi profile: clear any manual DNS and ignore router's DNS
nmcli connection modify "Co Phuong" ipv4.dns ""
nmcli connection modify "Co Phuong" ipv4.ignore-auto-dns yes
nmcli connection modify "Co Phuong" ipv6.ignore-auto-dns yes

# 6. Restart everything
systemctl restart systemd-resolved
systemctl restart NetworkManager

# 7. Verify
resolvectl status

# wlan0 should have no DNS servers of its own
# Global should show your NextDNS servers with DoT

------------------------------------------------------------------------------------------------
sudo pacman -S ufw
# Default: block all incoming, allow all outgoing
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow SSH if you use it (do this BEFORE enabling or you'll lock yourself out)
sudo ufw allow ssh

# Enable
sudo ufw enable

# Check status
sudo ufw status verbose

# Allow specific port
ufw allow 51820/udp    # WireGuard, if you use it later

# Allow from specific IP only (e.g. your LAN)
ufw allow from 192.168.1.0/24

# Delete a rule
ufw delete allow ssh

----------------------------------------------------------
# 1. Check resolvectl shows NextDNS with DoT
resolvectl status

# 2. Test an actual DNS query and see which server answered
resolvectl query google.com

# 3. Check the NextDNS test page
curl https://test.nextdns.io

# Check it's active and rules are correct
ufw status verbose
nmap -p 22,80,443 <your machine's IP>
ip addr show wlan0 | grep "inet "

curl -sL https://test.nextdns.io | jq

--------------------------------------------------------------------------------
sudo partprobe /dev/sda
sudo udevadm trigger
lsblk -o NAME,PARTUUID
findmnt /
cat /proc/cmdline
