# Dotfiles
## Dependences:
```
sudo pacman -S nemo python-pip volumeicon picom rofi scrot xclip qtile zsh
yay -S nerd-fonts-ubuntu-mono visual-studio-code-bin
pip install psutil
```

## Download:
```
cd
git clone https://github.com/01eguer/dotfiles && cd dotfiles
mv -r .config ../
mv .p10k.zsh ../
mv .zshrc ../ 
mv powerlevel10k/ ../
cd
```

### Rofi Theme/pluggins:
```
git clone https://github.com/davatorium/rofi-themes.git && sudo mv rofi-themes/User\ Themes/onedark.rasi /usr/share/rofi/themes/onedark.rasi && sudo rm -r rofi-themes
sudo pacman -S rofi-emoji
sudo bash emojis-font-installer.sh
```

### Zsh:
```
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
```

#### Zsh Plugins:
##### Autocomplete:
```
git clone --depth 1 -- https://github.com/marlonrichert/zsh-snap.git
source zsh-snap/install.zsh
```

##### Syntax hightlighting:
```git clone https://github.com/zsh-users/zsh-syntax-highlighting.git```

#### Change shell (bash -> zsh)
```
chsh -l # to view all shells
chsh -s /usr/bin/zsh
```
#### Manual config:
```zsh```

##### Only run if you don't use my zsh config files:
Autocomplete:
```
echo znap source marlonrichert/zsh-autocomplete #uncomment for autocomplete > ${ZDOTDIR:-$HOME}/.zshrc
```
Syntax hightlighting:
```
echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
```

### Vscode Themes
Instalation of the vscode themes that I use:
```
code --install-extension icrawl.discord-vscode
code --install-extension s-nlf-fh.glassit
code --install-extension PKief.material-icon-theme
code --install-extension Equinusocio.vsc-material-theme
code --install-extension ms-python.python
```
