[app]
title = appname#允许中文 Chinese allowed
package.name = packagename
package.domain = org.test#release模式不能用org.test 'org.test' can't be used in release mode
source.dir = .#工作目录 working directory
source.include_exts = py,png,jpg,kv,atlas#需要打包的文件类型 file types to be packed
#source.include_patterns = image/* 打包image目录下的文件 Pack files in the image directory
version = 0.0.1
#依赖库,后二为打包需要 The last two are needed for packaging
requirements = python3,kivy,kivymd,libiconv,libffi
#icon.filename = icon.png
#presplash.filename = presplash.png
#fullscreen = 0
#orientation = portrait
entrypoint = main.py#主程序 Main,what can I say.Mamba out

#这些不要改 Don't change these
android.accept_sdk_license = True
android.allow_api_min = 21
android.api = 33
android.minapi = 21
android.ndk = 25b
exclude_patterns = **/test/*, **/tests/*
android.gradle_download = https://services.gradle.org/distributions/gradle-7.6.4-all.zip
android.gradle_plugin = 7.4.2
android.sdk = 33
android.ndk_api = 21
p4a.gradle_dependencies = gradle:7.6.4
p4a.bootstrap = sdl2
p4a.gradle_options = -Dorg.gradle.java.home=/usr/lib/jvm/java-17-openjdk-amd64
android.permissions = INTERNET#打包需要网络权限 Network permission is required for packaging

#以下为release模式需要 Following is required for release mode

#强制构建APK而不是AAB,但没用 Why does it build .aab instead of .apk?
#android.aab = False

#签名配置 signature configuration
#android.keystore = /home/runner/work/RepositoryName/AndAgain/DomainName.PackageName.keystore
#android.keystore_storepass = android
#android.keystore_keypass = android
#android.keystore_alias = DomainName.PackageName

[buildozer]
log_level = 2
warn_on_root = 1