# Kivy Android APK Builder

使用GitHub Actions自动构建Kivy Android APK/AAB的模板仓库。

A template repository for automatically building Kivy Android APK/AAB using GitHub Actions.

## 使用方法 | Usage

### 0. fork本仓库或使用此模板 | Fork This Repository or Use This Template

### 1. 配置项目 | Configure Project
确保项目根目录包含 `buildozer.spec` (自行修改参数),`main.py`(无语法错误,可在python3.9正常运行)和依赖文件(使用`相对路径`调用,避免中文文件名)。

Make sure your project root contains `buildozer.spec`(changed parameters),`main.py`(can run on python3.9 without grammatical errors) and required files(calling with `relative path`).

将`buildozer.spec`和`release.yml`中`RepositoryName`,`DomainName`,`PackageName`替换

Replace `RepositoryName`,`DomainName`,`PackageName` in `buildozer.spec` and `release.yml`

### 2. 设置工作流程 | Setup Workflows
本仓库提供两个工作流程:

This repository provides two workflows:

- **`release.yml`** - 发布模式（签名AAB）
  - Release mode (signed AAB)
- **`debug.yml`** - 调试模式（未签名APK）
  - Debug mode (unsigned APK)

手动触发构建,流程约15分钟。

Manually trigger builds,it usually takes about 15 minutes.

### 3. 获取构建产物 | Get Artifacts
构建完成后,在Actions页面下载:

After build completes,download from Actions page:

- **APK/AAB 文件** - 安装包
  - APK/AAB files - install packages
- **构建日志** - 调试信息
  - Build logs - debug information
- **签名密钥** - 用于发布,妥善保存
  - Signing keystore - for release,keep it safe
