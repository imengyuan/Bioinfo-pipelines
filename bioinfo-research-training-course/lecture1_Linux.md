# 计算生物研究训练课程笔记week1

[课件地址](http://222.18.10.115/class/2018-Spring/001-Linux.html)
<!--整理知识点，记录遇到的问题-->

<br>

## Linux服务器概览
kernel-shell-application的结构

## 与服务器建立连接

### ssh连服务器
windows可使用putty连接服务器，winscp传输文件
macOS在终端下执行相应命令即可

```
ssh -i key -p port username@server_ip_address
```
(p为小写)

### scp传输文件

```
scp -i key -P 端口号 本地文件路径 username@服务器ip:目的路径
```
（P为大写）

## 终端编辑与执行命令

### 终端基本操作 bash/zsh
* 文件
* 路径
* 查看文件
* 查看进程
* 管道 |
* 标准输入输出
1>out 2>err ; >> out.log;  < input
* 后台运行 nohup & 

### 文本编辑 emacs
mac的键盘上，ctrl-control,M-command

列删除 c-x r d

列插入 m-x string-insert-rectangle （option-alt键）

### tmux
新建会话

```
tmux # 新建一个无名称的会话
tmux new -s demo 
```


断开当前会话

```
tmux detach 
ctrl+b+d
```
进入之前会话

```
tmux a -t session-name 
tmux a 
```

窗口新开和跳转

F2 F3 F4

### 常用命令

```
man 查看命令帮助；-h等

ls -lh 列出权限； ls -lhSr 按大小倒排； ls -a 所有文件；--sort=time按时间排序
cd - 返回之前目录
cat文件打开与创建； zcat解压缩，查看压缩的文件
mv 移动重命名；cp 复制
date显示时间
file查看文件信息
unzip；gzip .gz； tar .tar.gz
df 查看磁盘
echo 写入
export 修改环境变量
exit 退出服务器
grep查找 -R文件夹 -i忽略大小写
grep 查找关键字
rsync 远程拷贝,同步目录 -avP 进度
wc -l FILE word count查看行数
alias命令的别名
touch修改文件时间
rm -r慎用哈哈
find -iname "\*.pl"
diff比较文件
perl -i -p -e 's|||' file 正则表达式替换 
perl -lane 'print $F[1]\n' file perl文件处理
ps preocess state
less 查看文件 -Sx 30 按行查看和设置table宽度
ln -s pathsrc pathdst软链接
ps aux服务器所有进程的状态
top 查看进程cpu等信息
kill 杀死进程
```

chmod 修改文件权限

u用户自己；g同一个组；o其他人；
+增加权限，-去掉权限

| 管道，前者输出变为后者输入

顺序执行多个命令 命令组； && > output.txt

后台运行 & ; nohup &

正在运行的命令，先ctrl+Z暂停，bg后台运行 disown
后台命令转到前台 fg






## 管理若干项目
项目文件结构，project scripts分开为两个文件夹，便于备份script

### 注意事项
* 注重实验设计
* 提高代码对人的可读性（注释），数据对机器的可读性（统一 格式化）
* 尽量让电脑干活，使用已有的库，输入数据只读
* 测试代码
* 常用脚本变为通用工具

## 编译软件

```
tar -zxvf putty-0.70.tar.gz
cd putty-0.70
./configure --prefix=/home/train128/software
make
make install
```

## 遇到的问题与总结
mac的键盘中，使用emacs需要注意ctrl是control,M是command

应充分利用mac的优势更便捷地连接服务器并进行操作





