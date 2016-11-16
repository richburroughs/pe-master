# -*- mode: ruby -*-
# vi: set ft=ruby :

PE_VERSION = "2016.4.2"

Vagrant.configure("2") do |config|

  config.vm.box = "puppetlabs/centos-7.2-64-nocm"
  config.vm.network "forwarded_port", guest: 443, host: 4443
  config.vm.synced_folder "../../installers", "/vagrant_installers"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
  end
  
  config.vm.provision "shell", inline: <<-SHELL
    cp /vagrant_installers/puppet-enterprise-#{PE_VERSION}-el-7-x86_64.tar.gz /root
    cd /root
    tar xvfz puppet-enterprise-#{PE_VERSION}-el-7-x86_64.tar.gz
    cd puppet-enterprise-#{PE_VERSION}-el-7-x86_64
    ./puppet-enterprise-installer -c /vagrant/pe.conf
    /opt/puppetlabs/bin/puppet agent -t
    firewall-cmd --zone=public --add-port=443/tcp --permanent
    firewall-cmd --reload
  SHELL
end
