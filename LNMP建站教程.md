# LNMP建站教程

## 登陆到自己的vps中进行操作

```/bin/bash
# 我的系统是ubuntu20.04
# 显示当前操作系统的架构类型
arch	# x86_64
# 升级
sudo apt update&&sudo apt-get update
# 安装基本配置
sudo apt install curl
curl -faSL https://get.docker.com | bash -s docker
docker -v
# 拉取docker镜像
docker pull mysql:5.7
docker pull wordpress
docker pull jc21/nginx-proxy-manager
# 查看docker镜像
docker images
# 创建docker容器，配置容器内设置。
docker network create web
docker run --name mysql57 --net web -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7 --character-set-server=utf8 --collation-server=utf8_unicode_ci
docker  exec -it mysql57 bash
# 进入了mysql57,
mysql -uroot -p
# Enter password:密码为空，直接进
# create database wp;
# create user wp identified by "123456"
# grant all on wp.* to wp;
# exit
# exit
# 回到了宿主机
cd /home
mkdir blog
cd blog
docker run -dit --net web -v 'pwd':/var/www/html --name wordpress wordpress
cd /home
mkdir nginx_proxy
cd nginx_proxy
docker run -dit -p 80:80 -p 60066:81 -p 443:443 --net web --name nginx_proxy -v $PwD/data:/data -v $PwD/letsencrypt:/etc/letsencrypt --restart=unless-stopped jc21/nginx-proxy-manager
docker ps
```

## 进入web页面进行设置



Web地址：http://<自己vps公网ipv4地址>:60066/login

默认登陆信息：

```
Email： admin@example.com
Password: changeme
```



## 购买域名

namesilo上可以购买域名

## Cloudflare

申请名称服务器，并对域名做解析能解析到我们的服务器上。

## 配置名称服务器

namesilo上配置从Cloudflare上分配到的名称服务器。

## 申请SSL

回到web页面：http://<自己vps公网ipv4地址>:60066

登陆成功后点击页面中部的SSL Certificate再点击页面中下部ADD SSL Certificate。这里申请ssl只能用二级域名，www.开头的或者自己在cloudflare上配置的域名都可。

## 从申请完SSL的二级域名进入web网址

点击Proxy Hosts下已申请完毕的二级域名，按照指引过程，一步步填写安装即可。

## 强制HTTPS登陆

在/var/lib/docker/volumes/pwd/_data/wp-config.php中的<?php下添加

```php
<?php
/**强制使用SSL/HTTPS访问后台以及登录**/
define('FORCE_SSL_ADMIN', true);
define('FORCE_SSL_LOGIN', true);

/**请求标头告知**/
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO'])
	&& $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https'){
	$_SERVER['HTTPS'] = 'on';
}
```

再从上一步的web网址中直接刷新，就能进入网站后台了。

## 建站参考链接

youtube：[https://www.youtube.com/watch?v=lkNdVQJxtMU&ab_channel=Eystasy%E4%B8%A8%E4%BC%8A%E5%93%A5%E3%81%AE%E5%88%86%E4%BA%AB](https://www.youtube.com/watch?v=lkNdVQJxtMU&ab_channel=Eystasy丨伊哥の分享)