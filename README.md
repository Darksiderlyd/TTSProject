# TTSProject

## [ttsfile.py](ttsfile.py) 文件生成语音和字幕

## [ttssrtvtt.py](ttssrtvtt.py) vtt字幕转srt字幕

## [ttstext.py](ttstext.py) 文字生成语音和字幕

# [PaddlePaddle 安装](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/windows-pip.html)

## 一.Python 环境

使用以下命令确认是 3.8/3.9/3.10/3.11/3.12

   ``` 
   python --version
   ```

需要确认 pip 的版本是否满足要求，要求 pip 版本为 20.2.2 或更高版本

``` 
python -m ensurepip
```

``` 
python -m pip --version
```

需要确认 Python 和 pip 是 64bit，并且处理器架构是 x86_64（或称作 x64、Intel
64、AMD64）架构。下面的第一行输出的是”64bit”，第二行输出的是”x86_64”、”x64”或”AMD64”即可：

``` 
python -c "import platform;print(platform.architecture()[0]);print(platform.machine())"
```

默认提供的安装包需要计算机支持 MKL

Windows 暂不支持 NCCL，分布式等相关功能

## 二.安装Paddle

选择1: 直接安装CPU版本

```
python -m pip install paddlepaddle==2.6.0 -i https://mirror.baidu.com/pypi/simple
```

选择2: 安装GPU

第一步: 先安装CUDA，[参考](https://zhuanlan.zhihu.com/p/102966512) [12.0版本](https://developer.nvidia.com/cuda-12-0-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)

第二步: 安装cudnn [8.9.1](https://developer.nvidia.com/rdp/cudnn-archive)

第三步: 安装CUDA12.0 的 PaddlePaddle
```
python -m pip install paddlepaddle-gpu==2.6.0.post120 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
```

## 三、验证安装

安装完成后您可以使用 python 进入 python 解释器，输入import paddle ，再输入 paddle.utils.run_check()
如果出现PaddlePaddle is installed successfully!，说明您已成功安装。

## 四、如何卸载
请使用以下命令卸载 PaddlePaddle：

CPU 版本的 PaddlePaddle: 
```
python -m pip uninstall paddlepaddle
```

GPU 版本的 PaddlePaddle:
```
python -m pip uninstall paddlepaddle-gpu
```

## 五、安装 Conda
Conda是一个包管理的环境。

第一步: 你可以前往 [minicoda](https://docs.conda.io/projects/miniconda/en/latest/
) 去下载并安装 conda（请下载 py>=3.7 的版本）。

第二步: [环境变量配置](https://blog.csdn.net/yinjun3215/article/details/123705879)

第三步: 然后你需要安装 paddlespeech 的 conda 依赖:
```
conda install -y -c conda-forge sox libsndfile bzip2
```

第四步: 安装 C++ 编译环境
(如果你系统上已经安装了 C++ 编译环境，请忽略这一步。)

Windows
对于 Windows 系统，需要安装 Visual Studio 来完成 C++ 编译环境的安装。

https://visualstudio.microsoft.com/visual-cpp-build-tools/

你可以前往讨论区[#1195](https://github.com/PaddlePaddle/PaddleSpeech/discussions/1195)获取更多帮助。

## 六、安装 PaddleSpeech
第一步: 部分用户系统由于默认源的问题，安装中会出现kaldiio安转出错的问题，建议首先安装pytest-runner:

```
pip install pytest-runner -i https://pypi.tuna.tsinghua.edu.cn/simple 
```
第二步: 安装paddlespeech 

```
pip install paddlespeech -i https://pypi.tuna.tsinghua.edu.cn/simple
```
 
