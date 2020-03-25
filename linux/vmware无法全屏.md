# vmware 虚拟机无法全屏

## 问题：

安装 vm tools 后依然无法全屏 ， 查看->自动调整大小 选项无法选择

## 解决办法：

命令修改：

 sudo vim /etc/systemd/system/multi-user.target.wants/open-vm-tools.service
 在"Unit" 段中，增加如下配置：

```
Requires=graphical.target
After=graphical.target
```

保存后重启虚拟机就可以全屏显示了。


