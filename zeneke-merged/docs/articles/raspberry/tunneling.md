# Private Firefox Navigation through Raspberry Pi

Guide to browse with Firefox through your home ADSL using Raspberry Pi.

## Requirements

- Have a Raspberry Pi
- Have configured a fixed IP on the RPi
- Have SSH server running on the RPi
- Be able to open router ports
- Recommended: Have a DNS Host service like DYNDNS

## Steps

### 1. Configure the Router {#con_router}

Redirect port 22 in the Router to the local fixed IP of your RPi.

### 2. Configure RPi SSH Server {#con_ssh}

Use the [original configuration guide](index.md) for SSH setup.

To check if port 22 is open, use [yougetsignal.com/tools/open-ports/](http://www.yougetsignal.com/tools/open-ports/).

In Remote Address, put your public IP (default if you're at home).
In Port Number, put 22. Click check and you should see "Port 22 is open on IP".

### 3. Configure DNS Hosting Service {#con_dns}

We'll use [no-ip.com](http://www.no-ip.com) (or [dynDNS](http://www.dyndns.com)).

1. Register on the website
2. Login with your user
3. Click "Add a host"
4. Choose a Hostname (the name you'll use to access your RPi from outside)
5. Choose a free domain type, e.g., "no-ip.org"
6. From now on, access your RPi with: YourChosenName.no-ip.org

Download the client for your local PC to automatically update when your IP changes:
[Download link](http://www.noip.com/downloads.php)

### 4. Configure the PC {#con_pc}

Download Putty for Windows: [putty.exe](http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe)

**Initial Screen Configuration:**
- Host Name: YourChosenName.no-ip.org
- Port: 22
- Connection type: SSH

**Configure Tunnels:**
1. Select in left menu: Connection → SSH → Tunnels
2. Choose "Dynamic" option
3. In "Forwarded ports", choose a port (e.g., 4567)
4. Click "Add"

**Save Session:**
1. Return to Session in left menu
2. Enter name in "Saved Sessions"
3. Click "Save"
4. Click "Open"

Enter your Raspberry Pi username and password when prompted.

**Configure Firefox:**

1. Firefox button (top left) → Options → Options
2. Advanced → Network tab → Connection → Settings button
3. Select "Manual proxy configuration"
4. SOCKS Host: localhost
5. Port: 4567
6. Select SOCKS v5
7. No proxy for: localhost, 127.0.0.1
8. Click OK

If everything went well, you're now browsing through your home ADSL securely!

To test, navigate to your router's IP address - you should see the configuration page.
