# 524 Raspberry Pi Cluster

Each cluster consists of:

- 1 head node ([setup](head.md))
- 4 compute nodes ([setup](compute.md)) 

## Configuration

### Flash Raspbian

1. Download Raspbian image [here](https://www.raspberrypi.org/downloads/).
2. Download Etcher [here](https://etcher.io/).
3. Using Etcher, flash Raspbian onto SD card.

### Change password

Change password:

    passwd
    
Enter new password via prompts.

### Change hostnames

rp0 - rp4

This can be done on the command line using:

    sudo raspi-config
    
Or by going to preferences -> ???

Or by modifying **/etc/hostname**

### Setup hosts

For each node, change **/etc/hosts** to:

```
127.0.0.1 localhost
::1 localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

127.0.1.1 rpi0 rpi0.local rpi0.lan rpi0.cluster

192.168.50.1    rp0 rp0.local rp0.lan rp0.cluster
192.168.50.11   rp1 rp1.local rp1.lan rp1.cluster
192.168.50.12   rp2 rp2.local rp2.lan rp2.cluster
192.168.50.13   rp3 rp3.local rp3.lan rp3.cluster
192.168.50.14   rp4 rp4.local rp4.lan rp4.cluster
```

### SSH

(to-do)

    