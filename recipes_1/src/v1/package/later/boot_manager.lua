return {
    efibootmgr={repo=Repo.AOR}
}

# Auto
bootctl install
# Manual: Create correct systemd-boot entry
sudo efibootmgr --create --disk /dev/sda --part 1 --label "Arch Linux" --loader "\EFI\systemd\systemd-bootx64.efi"

# Check new entry ID
efibootmgr -v

# Delete stale entries
sudo efibootmgr -b 0000 -B  # old Fedora
sudo efibootmgr -b 0001 -B  # floppy
sudo efibootmgr -b 0005 -B  # stale GRUB
sudo efibootmgr -b 000B -B  # old Toshiba
sudo efibootmgr -b 0008 -B # old window

# Set boot order (replace 0010 with your new entry ID)
sudo efibootmgr -o 0007,0008,000F,0003,0006





09:39 ~ took 0ms
❯ sudo bootctl install
[sudo] password for victor:
Created directory "/boot/EFI".
Created directory "/boot/EFI/systemd".
Created directory "/boot/EFI/BOOT".
Created directory "/boot/loader".
Created directory "/boot/loader/keys".
Created directory "/boot/loader".
Created directory "/boot/loader/entries".
Created directory "/boot/EFI".
Created directory "/boot/EFI/Linux".
Copied "/usr/lib/systemd/boot/efi/systemd-bootx64.efi" to "/boot/EFI/systemd/systemd-bootx64.efi".
Copied "/usr/lib/systemd/boot/efi/systemd-bootx64.efi" to "/boot/EFI/BOOT/BOOTX64.EFI".
⚠️  Mount point '/boot' which backs the random seed file is world accessible, which is a security hole!  ⚠️
⚠️ Random seed file '/boot/loader/random-seed' is world accessible, which is a security hole! ⚠️
Random seed file /boot/loader/random-seed successfully refreshed (32 bytes).
Updated EFI boot entry "Linux Boot Manager".


0022-177
0022-177
unsecure: UUID=FCE7-3C97    /boot    vfat    rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=ascii,shortname=mixed,utf8,errors=remount-ro    0 2
secure: UUID=FCE7-3C97    /boot    vfat    rw,relatime,fmask=0177,dmask=0077,codepage=437,iocharset=ascii,shortname=mixed,utf8,errors=remount-ro    0 2
