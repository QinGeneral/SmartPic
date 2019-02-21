# SmartPic 简介和帮助

SmartPic 是一款 Alfred workflow，可以方便大家上传图片到云上，并获取图片链接，可用于 Markdown 写文章时添加图片或其他用途。

> 注：SmartPic 基于 Python 2.7，请确保已安装 Python，并具备 Python 基础库，如 request。

## 安装

下载 SmartPic.alfredworkflow 文件后，双击即可。当然，前提是已安装 Alfred（请自行安装）。

## 配置

SmartPic 其实是将图片上传至腾讯云存储桶，所以你需要自行申请免费的存储桶，并将存储桶相关参数配置到本地即可。

1. 登录腾讯云创建存储桶 [点击创建](https://console.cloud.tencent.com/cos5/bucket)。点击会打开腾讯云，界面如下图，点击其中的```创建存储桶```进行创建。
![创建存储桶](https://blog-pic-1251295613.cos.ap-guangzhou.myqcloud.com/1.png)

2. 创建完成后的界面如下图：
![创建后界面](https://blog-pic-1251295613.cos.ap-guangzhou.myqcloud.com/1550648375.032.png)

3. 点击左侧的密钥管理，可以找到配置参数中的 secret_id、secret_key 两项
![查看密钥](https://blog-pic-1251295613.cos.ap-guangzhou.myqcloud.com/1550648364.593.png)

4. 点击要使用的存储桶，进入下图界面。各个参数的对应值已在图中标出，包含 bucket、region、blog_prefix 三项。
![存储桶参数](https://blog-pic-1251295613.cos.ap-guangzhou.myqcloud.com/4.png)

5. 呼出 Alfred，输入 SmartPic 命令，按下 Enter 进入菜单界面，并选择 ```config``` 菜单（如下图），在打开的文件中以 json 方式配置上述步骤中找到的 secret_id、secret_key、bucket、region、blog_prefix 五项参数，替换 ```******``` 部分即可，以下述代码为例。
![配置 SmartPic](https://blog-pic-1251295613.cos.ap-guangzhou.myqcloud.com/1550651675.75SmartPic.png)
    ```config.txt```文件的配置格式

    ```json
    {
        "secret_id": "******",
        "secret_key": "******",
        "region": "ap-guangzhou(只取英文)",
        "bucket": "******",
        "blog_prefix": "******"
    }
    ```

## 使用

### SmartPic 命令

此命令包含以下四个命令：

- config：配置存储桶参数
- list：查看已上传图片列表，移动到指定项：Cmd + Y 可查看图片；Enter 可复制图片链接
- uploadPic：上传图片：搜索出图片，Enter 后即可上传，上传完成会自动复制链接到剪切板
- help：查看帮助文档

### SmartPicUploadPic 命令

上传图片：搜索出图片，Enter 后即可上传，上传完成会自动复制链接到剪切板。