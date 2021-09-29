# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from libqtile.utils import guess_terminal
from libqtile import hook
from os import path
import subprocess



@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser('~'), ".config", "qtile", 'autostart.sh')])





mod = "mod4"
terminal = guess_terminal()

keys = [
    # SWITCH BETWEEN WINDOWS
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # RESIZE WINDOWS
    Key([mod, "shift"], "h", lazy.layout.grow(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shrink(),
        desc="Move window to the right"),

    # CHANGE LAYOUT
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # KILL WINDOW
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # RESTART AND SHUTDOWN QTILE
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # MOVE WINDOWS (UP & DOWN)
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # MOVE WINDOWS (RIGHT & LEFT)
    # Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
    #     desc="Move window down"),
    # Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window up"),



    # PROGRAMS:
    # START TERMINAL (alacritty)
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # START ROFI LAUNCHER (drun)
    Key([mod], "r", lazy.spawn('rofi -show drun'),
         desc="Spawn rofi launcher (drun)"),

    # START ROFI LAUNCHER (run)
    Key([mod, "shift"], "r", lazy.spawn('rofi -show run'),
         desc="Spawn rofi launcher (run)"),

    # START ROFI EMOJIS SELECTOR
    Key([mod], ".", lazy.spawn('rofi -show emoji -modi emoji'),
         desc="Spawn rofi emoji"),
         
    
    # START ROFI WINDOW SELECTOR
    Key([mod, "shift"], "Tab", lazy.spawn('rofi -show window'),
         desc="Spawn rofi window selector"),

    # START WEB BROWSER
    Key([mod], "e", lazy.spawn('firefox'),
         desc="Spawn firefox"),

    # START FILE MANAGER
    Key([mod], "b", lazy.spawn('nemo'),
        desc="Spawn nemo"),

    # START TEXT EDITOR
    Key([mod], "c", lazy.spawn('code'),
        desc="Spawn code"),

    # SCREENSHOT:
    Key([mod, "shift"], "s", lazy.spawn("scrot -s -e 'xclip -selection clipboard -t image/png -i $f && rm $f'"),
        desc="Screenshot witch scrot to the clipboard with xclip"),

    
]



groups = [Group(i) for i in [
    "   ", "   ", "   ", "  ﭮ ", "   ", "   ", "   ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # CHANGE WORKSPACE
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # SEND WINDOW TO WORKSPACE
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

m = 7
b = 1
layouts = [
    layout.MonadTall(border_focus='#0000ff', border_width=b, margin=m),
    layout.MonadWide(border_focus='#0000ff', border_width=b, margin=m),
    layout.Max(border_focus='#0000ff', border_width=b, margin=m),
    
    # layout.Columns(border_focus_stack='#d75f5f'),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=16,
    padding=8,
)
extension_defaults = widget_defaults.copy()



screens = [
    Screen(
        top=bar.Bar(
            [
                
                widget.GroupBox(
                    padding_x=0,
                    padding_y=0,
                    margin_y=1,
                    margin_x=2,

                    this_current_screen_border='a3c5ff',
                    #this_screen_border="113358",
                    #other_screen_border="fff000",
                    active='ffffff',
                    inactive="8f8f8f",
                    urgent_text="ffd47e",
                    rounded=True,
                    font='UbuntuMono Nerd Font',
                    highlight_method="text",
                    disable_drag=True,
                ),



                widget.WindowName(),
                
                widget.Spacer(),
                widget.CPU(format='  {load_percent}%', foreground='ffd47e'),
                widget.Memory(format='  {MemPercent}%', foreground='d3a7ee'),
                widget.Net(format='歷  {down} ↓↑ {up}', use_bits=True, foreground="cdea9f"),
                
                #widget.Wlan(),
                #widget.Volume(device='HD-Audio Generic', channel='Master', get_volume_command='--get-volume-human'),
                #widget.Backlight(),

                widget.Sep(),
                widget.Systray(),
                widget.TextBox(' ', fontsize=1),
                widget.Sep(),

                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                

                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),

                widget.Clock(format='  %Y-%m-%d %a %H:%M:%S %p',  font='UbuntuMono Nerd Font Bold', foreground="93bbff"),
                
                #widget.QuickExit(),

                widget.CurrentLayoutIcon()

            ],
            29,
        ),
    ),
]

# CONVERT WINDOWS TO FLOATING
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
