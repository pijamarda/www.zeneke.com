# Raspberry Pi Configuration Guide

Comprehensive guide for configuring and hardening your Raspberry Pi.

## Table of Contents

- [Initial Configuration](#initial-configuration)
- [Remote Access](#remote-access)
- [Extra Configuration](#extra-configuration)
- [Platform Hardening](#platform-hardening)
- [Server Installation](#server-installation)
- [Private Firefox Navigation](tunneling.md)

## Initial Configuration {#initial-configuration}

### Change keyboard to Spanish, timezone and locales

Change keyboard to Spanish:
```bash
sudo nano /etc/default/keyboard
```
Change `"gb"` to `"es"`

Configure timezone:
```bash
sudo dpkg-reconfigure tzdata
```

### Change to static IP

Edit `/etc/network/interfaces` and change the line:
```
iface eth0 inet dhcp
```

to:
```
iface eth0 inet static
    address 10.0.0.20
    netmask 255.255.255.0
    gateway 10.0.0.1
```

### Add normal user and enable sudo

Create a new user:
```bash
sudo adduser username
```

To allow the user to use "sudo":
```bash
sudo visudo
```

Add the following line under "root ALL=(ALL) ALL":
```
yourUsername ALL=(ALL) ALL
```

Alternatively, add user to sudo group:
```bash
adduser "username" sudo
```

## Remote Access {#remote-access}

### Enable SSH server

```bash
sudo bash
ssh-keygen
```

Press ENTER 3 times. Keys should appear in `/root/.ssh/` as `id_rsa` and `id_rsa.pub`.

### Disable ROOT for SSH

Edit `/etc/ssh/sshd_config` and change `PermitRootLogin` to `no`, then restart:
```bash
/etc/init.d/ssh restart
```

### Make SSH server start on boot

Rename `boot_enable_ssh.rc` to `boot.rc`:
```bash
sudo bash
cd /boot
mv boot_enable_ssh.rc boot.rc
shutdown -r -time now
```

## Extra Configuration {#extra-configuration}

### Enable autocomplete after SUDO

Add to the last line of `/etc/bash.bashrc`:
```bash
if [ "$PS1" ]; then
    complete -cf sudo
fi
```

### Expand memory for SD cards larger than 2 GB

Login and elevate to root:
```bash
sudo -i
df -h
```

Follow the fdisk process to resize partition (detailed steps in original guide).

### Connect USB stick

Find device ID:
```bash
tail -f /var/log/messages
```

Plug in USB and note the ID (sda1, sdb1, etc.). Press CTRL-C to stop.

Create mount directory:
```bash
sudo mkdir /media/usbstick
```

Mount with proper permissions:
```bash
sudo mount -t vfat -o uid=zeneke,gid=zeneke /dev/sda1 /media/usbstick/
```

## Platform Hardening {#platform-hardening}

### Install fail2ban

Reject continuous SSH login attempts:
```bash
sudo apt-get install fail2ban
```

### Install latest firmware to enable iptables

!!! warning
    In future distro updates this may not be necessary

Install prerequisites:
```bash
sudo apt-get install ca-certificates
sudo apt-get install git-core
```

Download and install rpi-update:
```bash
sudo wget http://goo.gl/1BOfJ -O /usr/bin/rpi-update
sudo chmod +x /usr/bin/rpi-update
sudo rpi-update
```

Run ldconfig and re-run update:
```bash
sudo ldconfig
sudo rpi-update
sudo reboot
```

## Server Installation {#server-installation}

### Install Apache2

First execute:
```bash
sudo groupadd www-data
sudo usermod -a -G www-data www-data
```

Update package repository:
```bash
sudo apt-get update
```

Install server:
```bash
sudo apt-get install apache2
```
