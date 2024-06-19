# Bishop Smith Template


### [Prerequisites](docs/prerequisites.md)
These should be completed prior to compiling or running the code

### Installing Prerequisites for Raspberry pi
I
```sh
sudo apt update
sudo apt install libwebkit2gtk-4.1-dev \
  build-essential \
  curl \
  wget \
  file \
  libxdo-dev \
  libssl-dev \
  libayatana-appindicator3-dev \
  librsvg2-dev
sudo npm install --force -g npm@latest
sudo npm install --force -g nodejs@latest
```
#### Adjusting the Swapfile
```sh
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
```
Change the variable `CONF_SWAPSIZE=` to your desired value in megabytes, normally around 6144
Uncomment the bottom variable and change it to the same value
Type in `CTRL + X` followed by `Y` and then `ENTER`
```sh
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```
Reboot the system
```sh
sudo reboot
```
#### Install Rustup
```sh
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```
Reboot the system again
```sh
sudo reboot
```

### Running the code
The html and css is located in the src folder, if you want to, you can use javascript as well.
Note: Iframes may have issues with some sites.
```sh
npm install
npm run tauri dev
```

### Changing the Icon
```sh
npm install
npm run tauri icon your-icon.png
```
### Building a release locally
```sh
npm install
npm run tauri build
npm run tauri icon your-icon.png
```
### Workflows
Workflows can be used to automatically compile and release your code.
This is an [example](.github/workflows/main.yml)

### Building a Snap
1. Go to snapcraft.io and create an account
2. Reserve an app name
3. Change all instances of `yourapp` to the name of your app
4. Add a summary and description to your app
5. Once your app name has been approved on snapcraft.io you can click on your app and then click on the builds tab.
6. When in the build tabs you can link your git repository to it and trigger a build.
7. When the build is successful you can go into `releases` and drag your release from latest/edge to latest/stable.
# Tauri + Vanilla

This template should help get you started developing with Tauri in vanilla HTML, CSS and Javascript.

## Recommended IDE Setup

- [VS Code](https://code.visualstudio.com/) + [Tauri](https://marketplace.visualstudio.com/items?itemName=tauri-apps.tauri-vscode) + [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer)
