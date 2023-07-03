import pymysql
import configparser

# 创建一个配置解析器对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('mysql_db.ini')

# 获取MySQL连接配置
host = config.get('mysql', 'host')
port = config.get('mysql', 'port')
database = config.get('mysql', 'database')
user = config.get('mysql', 'user')
password = config.get('mysql', 'password')
print(host, port, database, user, password)
print(type(host), type(port), type(database), type(user), type(password))

# 创建数据库连接
db = pymysql.connect(
    host=host,
    user=user,
    passwd=password,
    port=int(port),
    db=database,
    charset='utf8'
)

curses = db.cursor()
curses.execute('insert into user (username, age) values ("张三", 20)')