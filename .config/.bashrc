#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias cat='bat --style=plain'

PS1='[\u@\h \W]\$ '
