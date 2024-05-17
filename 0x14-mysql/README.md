# how to install MySQL server 5.7.*

```bash
wget https://repo.mysql.com//mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
sudo apt-key adv --keyserver pgp.mit.edu --recv-keys B7B3B788A8D3785C
sudo apt update
sudo apt install mysql-client=5.7.*-1ubuntu18.04
sudo apt install mysql-community-server=5.7.*-1ubuntu18.04
sudo apt install mysql-server=5.7.*-1ubuntu18.04
```
