# A simple snake game written in python with pygame 
## and funny sounds
<img width="200" height="200" alt="schnaeggelz" src="https://github.com/user-attachments/assets/8afc84b0-a066-435d-989a-bb90a4c2c915" />


install on Ubuntu:

```
sudo apt install python3-venv python3-pygame git -y
git clone https://github.com/Zahnschmelz/schnaeggelz.git
cd schnaeggelz
sudo chmod u+x ./run.sh
./run.sh

```

install on Arch Linux:
```
sudo pacman -Sy git python python-pygame pipewire-audio --noconfirm
git clone https://github.com/Zahnschmelz/schnaeggelz.git
cd schnaeggelz
sudo chmod u+x ./run.sh
./run.sh
```

install on Android:

check releases for apk

https://github.com/Zahnschmelz/schnaeggelz/releases/download/schnaeggelz/schnaeggelz-0.1-arm64-v8a_armeabi-v7a-debug.apk


Build APK with buildozer (Python3.11.5)

configure the buildozer.spec file:
```
[app]
title = schnaeggelz
package.name = schnaeggelz
package.domain = org.myDomain
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ogg,ttf,txt
version = 0.1
requirements = python3==3.10.12,hostpython3==3.10.12,pysdl2,pygame
presplash.filename = %(source.dir)s/schnaeggelz.png
icon.filename = %(source.dir)s/schnaeggelz.png
orientation = portrait
osx.python_version = 3
android.presplash_color = olive
android.archs = arm64-v8a,armeabi-v7a
[buildozer]
log_level = 2
warn_on_root = 1
```
run buildozer with:
```
buildozer android debug
```
