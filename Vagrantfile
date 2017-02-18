# -*- mode: ruby -*-
# vi: set ft=ruby :

PE_VERSION = "2016.5.1"
PE_INSTALLER_DIR = "../../installers"

Vagrant.configure("2") do |config|
  config.ssh.insert_key = false

  config.vm.define "master", primary: true do |master|
    master.vm.box = "puppetlabs/centos-7.2-64-nocm"
    master.vm.network "forwarded_port", guest: 443, host: 4443
    master.vm.synced_folder "#{PE_INSTALLER_DIR}", "/vagrant_installers"
    master.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
    end
  
    master.vm.provision "shell", inline: <<-SHELL
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
end
