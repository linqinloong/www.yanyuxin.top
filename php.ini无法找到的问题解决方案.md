# php.ini无法找到的问题解决方案

在外部写一个php.ini

    upload_max_filesize = 512M
    post_max_size = 512M

我是在根目录写的pip.ini因此

docker cp /php.ini wordpress\:/usr/local/etc/php/

在容器外重启容器

docker restart wordpress
