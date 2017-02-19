# -*- mode: ruby -*-
# vi: set ft=ruby :

PE_VERSION = "2016.5.2"
PE_INSTALLER_DIR = "../../installers"
MASTER_MEMORY = 4096
AGENT_MEMORY = 768

Vagrant.configure("2") do |config|
  config.ssh.insert_key = false

  config.vm.define "master", primary: true do |master|
    master.vm.box = "puppetlabs/centos-7.2-64-nocm"
    master.vm.synced_folder "#{PE_INSTALLER_DIR}", "/vagrant_installers"
    master.vm.hostname = "master.example.com"
    master.vm.network :private_network, ip: "192.168.77.2"
    master.vm.network "forwarded_port", guest: 443, host: 8443, protocol: 'tcp', auto_correct: true
    master.vm.provider "virtualbox" do |vb|
      vb.memory = "#{MASTER_MEMORY}"
      vb.name = "vagrant-pe-master"
    end
  
    master.vm.provision "shell", inline: <<-SHELL
      systemctl stop firewalld
      systemctl disable firewalld
      yum install -y epel-release
      yum install -y jq
      cp /vagrant/files/hosts /etc/hosts
      # PE install
      cp /vagrant_installers/puppet-enterprise-#{PE_VERSION}-el-7-x86_64.tar.gz /root
      cd /root
      tar xvfz puppet-enterprise-#{PE_VERSION}-el-7-x86_64.tar.gz
      cd puppet-enterprise-#{PE_VERSION}-el-7-x86_64
      ./puppet-enterprise-installer -c /vagrant/files/pe.conf
      cp /vagrant/files/autosign.conf /etc/puppetlabs/puppet
      /opt/puppetlabs/bin/puppet agent -t
    SHELL
  end
  (1..3).each do |i|
    config.vm.define "centos7-#{i}" do |node|
      node.vm.box = "puppetlabs/centos-7.2-64-nocm"
      node.vm.hostname = "centos7-#{i}.example.com"
      node.vm.network :private_network, ip: "192.168.77.#{2 + i}"
      node.vm.provider "virtualbox" do |vb|
        vb.memory = "#{AGENT_MEMORY}"
        vb.name = "centos7-#{i}"
      end
      node.vm.provision "shell", inline: <<-SHELL
        systemctl stop firewalld
        systemctl disable firewalld
        cp /vagrant/files/hosts /etc/hosts
        curl -k https://master.example.com:8140/packages/current/install.bash | bash
      SHELL
    end
  end
  config.vm.define "centos6" do |node|
    node.vm.box = "puppetlabs/centos-6.6-64-nocm"
    node.vm.hostname = "centos6.example.com"
    node.vm.network :private_network, ip: "192.168.77.6"
    node.vm.provider "virtualbox" do |vb|
      vb.memory = "#{AGENT_MEMORY}"
      vb.name = "centos6"
    end
    node.vm.provision "shell", inline: <<-SHELL
      cp /vagrant/files/hosts /etc/hosts
      curl -k https://master.example.com:8140/packages/current/install.bash | bash
    SHELL
  end
  config.vm.define "debian7" do |node|
    node.vm.box = "debian/wheezy64"
    node.vm.hostname = "debian7.example.com"
    node.vm.network :private_network, ip: "192.168.77.7"
    node.vm.provider "virtualbox" do |vb|
      vb.memory = "#{AGENT_MEMORY}"
      vb.name = "debian7"
    end
    node.vm.provision "shell", inline: <<-SHELL
      echo "192.168.77.2 master.example.com master" >> /etc/hosts
      apt-get install -y curl
      curl -k https://master.example.com:8140/packages/current/install.bash | bash
    SHELL
  end
  (1..3).each do |i|
    config.vm.define "debian8-#{i}" do |node|
      node.vm.box = "debian/jessie64"
      node.vm.hostname = "debian8-#{i}.example.com"
      node.vm.network :private_network, ip: "192.168.77.#{7 + i}"
      node.vm.provider "virtualbox" do |vb|
        vb.memory = "#{AGENT_MEMORY}"
        vb.name = "debian8-#{i}"
      end
      node.vm.provision "shell", inline: <<-SHELL
        echo "192.168.77.2 master.example.com master" >> /etc/hosts
        apt-get install -y curl
        curl -k https://master.example.com:8140/packages/current/install.bash | bash
      SHELL
    end
  end
end
