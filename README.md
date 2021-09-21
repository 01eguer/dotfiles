# dotfiles
## Dependences:
```
sudo pacman -S nemo python-pip volumeicon picom rofi scrot xclip qtile zsh
yay -S nerd-fonts-ubuntu-mono
pip install psutil
```

### Rofi Theme:
```sudo mv rofi-themes/User\ Themes/onedark.rasi /usr/share/rofi/themes/onedark.rasi && sudo rm -r rofi-themes```

### Zsh:
```
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
```
#### Manual config:
```zsh```
#### Zsh plugins:
##### Autocomplete:
```
git clone --depth 1 -- https://github.com/marlonrichert/zsh-snap.git
source zsh-snap/install.zsh
```

Only run if you don't use my zsh config files -> ```echo znap source marlonrichert/zsh-autocomplete #uncomment for autocomplete > ${ZDOTDIR:-$HOME}/.zshrc```


##### Syntax hightlighting:
```git clone https://github.com/zsh-users/zsh-syntax-highlighting.git```

Only run if you don't use my zsh config files -> ```echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc```
