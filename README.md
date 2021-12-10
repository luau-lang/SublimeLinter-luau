SublimeLinter-luau
================================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [luau-analyze](https://luau-lang.org).
It will be used with files that have the "Lua" syntax.


## Installation

SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, ensure that `luau-analyze` is installed on your system.
To install `luau-analyze`, download the executable from [Luau repo](https://github.com/Roblox/luau/releases).

Please make sure that the path to `luau-analyze` is available to SublimeLinter.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

The preferred method of configuring `luau-analyze` is via [.luaurc files](https://github.com/Roblox/luau/blob/master/rfcs/config-luaurc.md)
