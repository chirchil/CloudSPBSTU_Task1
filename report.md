# Домашнее задание по linux

1. Устанавливаю и запускаю 3 виртуальные машины в Virtual Box:
Ubuntu_A, Ubuntu_B, Ubuntu_C

![](./screenshots/Screenshot_4.png)


2. Для каждой виртуальной машины переименовываю hostname в соответственно shibalovserver, shibalovgateway и shibalovclient, создавая так же пользователей shibalov_1, shibalov_2, shibalov_3. 

```shell 
$ sudo vim /etc/hostname 
```

```shell 
$ sudo adduser shibalov_1 
```
Пытаюсь подключиться с терминала ко второй машине через ssh:

![](./screenshots/Screenshot_5.png)

3. На каждой машине устанавливаю ssh командами:

```shell
$ sudo apt update
```

Установка ssh:

```shell
$ sudo apt-get install ssh
```

Установка OpenSSH

```shell
$ sudo apt install openssh-server
```

Добавим пакет SSH-сервера в автозагрузку


```shell
$ sudo systemctl enable sshd
$ apt install openssh-server -y
$ systemctl enable ssh
$ systemctl start ssh
$ system status ssh
```

4. Также я пробросил порты для ssh на каждой виртуальной машине

- ```shibalov_1 : 1001```

- ```shibalov_2 : 1002```

- ```shibalov_3 : 1003```