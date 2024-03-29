# TTSProject

## [ttsfile.py](ttsfile.py) 文件生成语音和字幕

## [ttssrtvtt.py](ttssrtvtt.py) vtt字幕转srt字幕

## [ttstext.py](ttstext.py) 文字生成语音和字幕

## [视频生成器](https://juejin.cn/post/7106394465580875784)
## [自动生成字幕](https://pypi.org/project/autosub3/)
## [自动生成字幕视频自动上传DY](https://github.com/Richard0403/dy-auto)

# [PaddlePaddle 安装](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/windows-pip.html)

## [三种环境搭建](https://github.com/PaddlePaddle/PaddleSpeech/blob/develop/docs/source/install_cn.md)

## 一.Python 环境  基础功能搭建

### Tips: 后五个安装过程，如果是走 "六、（获取主要功能）安装 PaddleSpeech"时，除了安装外，命令都需要cd 到PaddleSpeech项目目录下后执行，需要执行的命令已经整理好

使用以下命令确认是 3.8/3.9/3.10/3.11/3.12  
Paddle支持3.11之下，3.11有问题

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

选择2: 安装GPU CUDA 12版本未支持完善回退到 11.7

第一步:
先安装CUDA，[参考](https://zhuanlan.zhihu.com/p/102966512) [11.7版本](https://developer.nvidia.com/cuda-11-7-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)

第二步: 安装cudnn [8.4.1](https://developer.nvidia.com/rdp/cudnn-archive)

第三步: 安装CUDA 11.7 的 PaddlePaddle

```
python -m pip install paddlepaddle-gpu==2.6.0.post117 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
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

## 六、（获取基本功能）安装 PaddleSpeech

第一步: 部分用户系统由于默认源的问题，安装中会出现kaldiio安转出错的问题，建议首先安装pytest-runner:

```
pip install pytest-runner -i https://pypi.tuna.tsinghua.edu.cn/simple 
```

第二步: 安装paddlespeech

```
pip install paddlespeech -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 六、（获取主要功能）安装 PaddleSpeech

按顺序执行命令安装

```
1. git clone git@github.com:PaddlePaddle/PaddleSpeech.git

2. cd PaddleSpeech

3. conda install -y -c conda-forge sox libsndfile bzip2

4. # 部分用户系统由于默认源的问题，安装中会出现 kaldiio 安转出错的问题，建议首先安装pytest-runner:
   pip install pytest-runner -i https://pypi.tuna.tsinghua.edu.cn/simple 
# 请确保目前处于PaddleSpeech项目的根目录
5. pip install . -i https://pypi.tuna.tsinghua.edu.cn/simple

6. python -m pip install paddlepaddle-gpu==2.6.0.post117 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html

```

安装完成之后通过 “三、验证安装” 验证是否正确安装如果报错请参考以下解决方案

## 运行脚本时遇到问题：把C:\Program Files\NVIDIA Corporation\Nsight Systems
2022.1.3\host-windows-x64\zlib.dll改名为zlibwapi.dll放到
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\bin
[zlibwapi.dll 问题 找到最后一个人的回答](https://forums.developer.nvidia.com/t/could-not-load-library-cudnn-cnn-infer64-8-dll-error-code-193/218437/16)

如果使用错误会导致：Could not load library cudnn_cnn_infer64_8.dll. Error code 193 这个错误

## UnicodeDecodeError: 'gbk' codec can't decode byte 0x96 in position 2: illegal multibyte sequence 

可以不用conda安装
更改setup.py中依赖的版本，然后重启重装ToJyutping
之前用conda 安装的0.21的ToJyutping，卸载掉然后重新 pip install ToJyutping 再次运行就OK了，打扰了

## [nltk_data] zipfile.BadZipFile: File is not a zip file
[问题解决 CSDN](https://blog.csdn.net/qq_43140627/article/details/103895811)

[问题解决 ISSUE](https://github.com/PaddlePaddle/PaddleSpeech/issues/2223)


