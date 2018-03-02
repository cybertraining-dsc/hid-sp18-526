# Raspberry Pi Cluster

- Tim Whitson @whitstd
- Juliano Gianlupi @JulianoGianlupi

## Hardware

Each cluster consists of:

- 1 head node ([setup](head)) (recommend following the instructions here first)
- 4 compute nodes

## Configuration

### Flash Raspbian

1. Download Raspbian image <https://www.raspberrypi.org/downloads/>.
2. Download Etcher <https://etcher.io/>.
3. Using Etcher, flash Raspbian onto SD card.

### Keyboard Layout

The default keyboard layout may need to be changed to US.

Menu -> Preferences -> Mouse and Keyboard Settings -> Keyboard tab -> Variant -> English (US)

### Change password

Change password:

    passwd
    
Enter new password via prompts.

### Change hostnames

Change hostname of each raspberry pi (in descending order).

1. rp0
2. rp1
3. rp2
4. rp3
5. rp4

This can be done on the command line using:

    sudo raspi-config
    
Or on the desktop by going to Menu -> Preferences -> Raspbery Pi Configuration

Or by modifying **/etc/hostname**

### Configure Head Node

Follow instructions [here](head)

### SSH

**Note: Gregor says this is not best practice**

Generate SSH keys:

    ssh-keygen -t rsa
    
Copy key to each node:

    ssh-copy-id <hostname>
    
For hostnames rp1-4.