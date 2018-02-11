# ansible-netscaler_raw

Some Ansible modules and roles for managing your favorite ADC - the Citrix NetScaler.

Still in development (alpha stadium). Use with caution, especially in your production environment. 

The Playbooks require at least Ansible 2.4. Running the plays *on* a NetScaler (as your Ansible control host) will not work. Currently NetScaler 12.0 is shipped with Python 2.6.6 and Ansible 2.1.1.0, which is completly outdated.

Feedback and feature requests are appreciated.

## Dependencies

The NetScaler module requires python-requests. 

## Parameters 

### General

| parameter        | description 
---                | ---        
netscaler_url      | URL to the the target NetScaler (without a tailing slash)
netscaler_username | Username for the administrative user
netscaler_password | Password for the administrative user

## Author

- [Simon Lauger](https://github.com/slauger)

## TODOs

- docs 
- Gateway configs
- Sharefile configs
- Exchange configs
- remove JSON files
- improve error handling in module
- integrate servers in common -> DNS bootstrap?
- how to deploy certs? NITRO vs SCP
- caching and connection multiplexing for sharefile disabled
- ssl
  - ssldhfile
  - sslcrlfile
  - ocsp
- systemsshkey
- systemuser - second admin
- systemfile
- systembackup
- facts (the easy way)
- add nsroot/nsroot as default in defaults.yml in every roles
- option to set url, username and password by $ENV

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


