# Provisioning Ubuntu Guest VM

This folder contains the files to provision a Ubuntu 16.04 VM onto your local machine, with a minikube cluster running the Confluent Kafka platform and the `datetime-injector-app`[^This was unfortunately not completed due to various provisioning issues with setting up minikube and then Helm]

### Vagrantfile

Contains the instruction set for what machine to build.

- 8GB of memory is currently set, which is a requirement to run the Kafka confluent platform
- Port 5000 is forward out from the Ubuntu VM also. This allows the `datetime-injector-app` to listen in on traffic outside of the Guest VM

### ubuntu_box/playbook.yml

Contains all individual provisioning steps that configure the Guest VM as required

## Pre-requisites

- VirtualBox
- Vagrant
- Ansible

## Usage

Provisioning the Ubuntu VM:

```
vagrant up
```

Once the Guest VM has been provisioned, `port-forward` the `datetime-injector-app` from the minikube cluster:

```
# ssh onto the Guest VM
$ vagrant ssh ubuntu-box

# port-forward the 'datetime-injector-app'
vagrant@ubuntu-xenial:~$ kubectl port-forward datetime-injector-app<unique_id_to_pod> 5000

# you should now be able to interact with the 'datetime-injector-app'
# e.g. Posting Kafka messages from your local machine
$ curl -X POST localhost:5000/producer/insert
```

[Return back to main README](../README.md)