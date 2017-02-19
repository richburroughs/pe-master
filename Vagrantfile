# -*- mode: ruby -*-
# vi: set ft=ruby :

PE_VERSION = "2016.5.1"
PE_INSTALLER_DIR = "../../installers"

Vagrant.configure("2") do |config|
  config.ssh.insert_key = false

  config.vm.define "master", primary: true do |master|
    master.vm.box = "puppetlabs/centos-7.2-64-nocm"
    master.vm.synced_folder "#{PE_INSTALLER_DIR}", "/vagrant_installers"
    master.vm.hostname = "master.example.com"
    master.vm.network :private_network, ip: "192.168.77.2"
    master.vm.network "forwarded_port", guest: 443, host: 8443, protocol: 'tcp', auto_correct: true
    master.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.name = "vagrant-pe-master"
    end
  
    master.vm.provision "shell", inline: <<-SHELL
      cp /vagrant/files/hosts /etc/hosts
      cp /vagrant_installers/puppet-enterprise-#{PE_VERSION}-el-7-x86_64.tar.gz /root
      cd /root
      tar xvfz puppet-enterprise-#{PE_VERSION}-el-7-x86_64.tar.gz
      cd puppet-enterprise-#{PE_VERSION}-el-7-x86_64
      ./puppet-enterprise-installer -c /vagrant/files/pe.conf
      /opt/puppetlabs/bin/puppet agent -t
      firewall-cmd --zone=public --add-port=443/tcp --permanent
      firewall-cmd --reload
    SHELL
  end
  (1..3).each do |i|
    config.vm.define "centos7-#{i}" do |node|
      node.vm.box = "puppetlabs/centos-7.2-64-nocm"
      node.vm.hostname = "agent1.example.com"
      node.vm.network :private_network, ip: "192.168.77.#{2 + i}"
      node.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
        vb.name = "agent1"
      end
      node.vm.provision "shell", inline: <<-SHELL
        cp /vagrant/files/hosts /etc/hosts
      SHELL
    end
  end
end
