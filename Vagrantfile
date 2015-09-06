# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

VAGRANT_LOCAL_CONFIG = "vagrant-conf.local"

load(VAGRANT_LOCAL_CONFIG) if File.exist?(VAGRANT_LOCAL_CONFIG) # include local configuration if available

VAGRANT_ARCH = "x64" unless defined? VAGRANT_ARCH

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.define "resume" do |resume|
    resume.vm.box = "debian"
    resume.vm.box_url = "https://ftp.lugons.org/vagrant/debian-7.6.0-x86_64.box"

    resume.vm.network :private_network, ip: "192.168.55.33"
        resume.vm.provision :ansible do |ansible|
            ansible.playbook = "provision/site.yml"
            ansible.host_key_checking = false
            ansible.groups = {
                "vagrant" => ["resume"],
            }
        end
    end
end
