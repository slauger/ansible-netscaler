# ansible-netscaler_raw

Some Ansible modules and roles for managing your favorite ADC - the Citrix NetScaler.

Still in development (alpha stadium). Use with caution, especially in your production environment. 

The Playbooks require at least Ansible 2.4. Running the plays *on* a NetScaler (as your Ansible control host) will not work. Currently NetScaler 12.0 is shipped with Python 2.6.6 and Ansible 2.1.1.0, which is completely outdated.

Feedback and feature requests are appreciated.

## Dependencies

The NetScaler module requires python-requests. 

## Usage

- Deploy your NetScaler (VPX/MPX/SDX/CPX)
- Setup your network configuration
- Configure a nsroot password
- Upload the a license, your ssl certificates and a ECDHE key
- Configure your inventory and run the playbook

### Roles

| role             | description 
---                | ---        
common             | Generic settings for all NetScaler setups (Best practices, SSL hardening, ...)
config_clear       | Clear the NetScaler configuration (for a play on a "fresh" instance)
config_save        | Save the NetScaler configuration
cvserver           | Setup Content Switching configuration by providing a configuration hash
sharefile          | Setup ShareFile Loadbalancing and AAA with SAML 
xenmobile          | Setup a full XenMobile Setup (LB and VPN)

... and many more.

## Parameters 

### General

| parameter        | description 
---                | ---        
netscaler_url      | URL to the the target NetScaler (without trailing slash)
netscaler_username | Username for the administrative user
netscaler_password | Password for the administrative user

## Author

- [Simon Lauger](https://github.com/slauger)

## TODOs

- Documentation for everything
- Exchange 2016 configuration (CS/AAA/Kerberos/NTLM)
- Loadbalancing for DNS servers (bootstrapping problem in common)
- Deploying certificates and license files trough NITRO, not trough SSH
- Be sure that caching and connection multiplexing is disabled for ShareFile
- SSL stuff
  - integrate sslcrlfile
  - integrate ocsp
- SSH Keys
  - systemsshkey
- Management
  - systemuser (secondary admin)
- Integrate systemfile
- Integrate systembackup
- Facts (the easy way)
- Option to set url, username and password by a ENV (run with Jenkins)

### How to implement customizations?

```
FreeBSD has chflags utility or command which modifies the file flags of the listed files as specified by the flags operand. See tutorial on how to Setup file immutable bit which is just like Linux chatter command. Following are flags

    arch: set the archived flag
    nodump: set the nodump flag
    sappnd: set the system append-only flag
    schg: set the system immutable flag
    sunlnk: set the system undeletable flag
    uappnd: set the user append-only flag
    uchg: set the user immutable flag
    uunlnk: set the user undeletable flag
```


