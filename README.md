# How to install and activate the OpenMSA freeware
## OpenMSA installation
###Interface configuration

Sometimes interfaces eth0 and eth1 are not visible. You have to edit the interface configuration file:
<pre>
[root@SNOC]#cd /etc/sysconfig/network-scripts
[root@SNOC network-scripts]#vi ifcfg-eth0
</pre>
remove reference to UUID and HWADDR the file should be like
<pre>
DEVICE="eth0"
BOOTPROTO="none"
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
NM_CONTROLLED="yes"
ONBOOT="yes"
TYPE="Ethernet"
IPADDR=10.31.1.14
NETMASK=255.255.255.0
GATEWAY=10.31.1.254
</pre>
Do the same with ifcfg-eth1

Then you can activate interfaces:
<pre>
[root@SNOC network-scripts]# ifup ifcfg-eth0
[root@SNOC network-scripts]# ifup ifcfg-eth1
</pre>
If an error occur:
<pre>
[root@SNOC]# echo "" > /etc/udev/rules.d/70-persistent-net.rules
[root@SNOC]#reboot
</pre>

###Configure the OpenMSA

Once the OVA is installed, start the VM. You should see the OpenMSA services starting messages in the console.

Make sure that the network setup of the VM are correctly set as well as the other parameters such as CPU, Disk,...

The MSActivator deploys with 50Gb disk but you may want to extends this to allow more flexibility later.

Connect as root to the MSActivator.

The following steps explain how to configure the network interface eth0 in order to be able to use the online configuration tool

configure eth0 with an address from your network:

![install_ip_config.png](Images/OpenMSA_installation_ifconfig.png)

and try to access http://ip_configured:3577/config.xml (login:socconfig password:b5ty9uvh4)

Then follow the instructions about the online configuration tool below

### Online configuration tool

This is the configuration method for the OpenMSA freeware.
access: http://w.x.y.z:3577/config.xml (socconfig/b5ty9uvh4) 
the access is only available through eth0 (maintenance interface). 

* eth0 is the interface dedicated to maintenance 
* eth1 is the interface dedicated to device management

#### OpenMSA information
![UBIqube_SOC_Configurator_1.png](Images/UBIqube_SOC_Configurator_1.png)

#### Company information
![UBIqube_SOC_Configurator_2.png](Images/UBIqube_SOC_Configurator_2.png)

#### Management interface configuration
![UBIqube_SOC_Configurator_3.png](Images/UBIqube_SOC_Configurator_3.png)

#### Maintenance interface configuration
![UBIqube_SOC_Configurator_4.png](Images/UBIqube_SOC_Configurator_4.png)

#### SMTP and DNS configuration
![UBIqube_SOC_Configurator_6.png](Images/UBIqube_SOC_Configurator_6.png)

#### Alarm and event configuration
![UBIqube_SOC_Configurator_7.png](Images/UBIqube_SOC_Configurator_7.png)




## OpenMSA activation
TODO write the doc
