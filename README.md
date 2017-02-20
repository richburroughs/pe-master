To use:
```
vagrant up master
```
This will build the master VM and install Puppet Enterprise.

By default it has the agent binaries for CentOS 7. If you want to use the other
agent platforms, you need to log into the console and enable them.

The console is at:
```
https://localhost:8443
username: admin
password: 12345678
```
The doc on how to add the additional platforms is here:

https://docs.puppet.com/pe/latest/install_agents.html#install-agents-with-a-different-os-and-architecture-than-the-puppet-master

To support all the other platforms in the Vagrantfile you need to add these classes:

```
pe_repo::platform::el_6_x86_64
pe_repo::platform::debian_7_amd64
pe_repo::platform::debian_8_amd64
```

After you make the changes in the console and apply them, run the puppet agent
on the master VM (sudo puppet agent -t). Then:
```
vagrant up
```
Or just bring up the hosts you want.
