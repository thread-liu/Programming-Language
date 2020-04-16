# Windows 环境下实现 anaconda 包管理

cd 进入 anaconda 安装目录。

## python 版本切换

1. 查看当前 python 版本

   ```
   cmd > python -V
   ```

2.  安装新的 python. 示例安装 python3.7.4

   ```
   conda create --name python37 python=3.7.4
   ```

3. 查看 python 环境

   ```
   conda info -e
   ```

4. 激活一个 python 环境

   ```
   conda activate python37
   ```

5. 切换环境后，又想回到之前的环境，可以通过命令

   ```
   conda deactivate
   ```

6. 删除一个 python 环境

   ```
   conda remove --name python37 --all
   ```

   

   

   