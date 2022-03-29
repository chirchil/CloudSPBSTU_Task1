#!/usr/bin/env bash
curl -X GET 192.168.13.10:5000/
curl -X POST -d 'username=mylinux' http://192.168.13.10:5000/login
curl -X PUT -d name="username" 192.168.13.10:5000/change_password