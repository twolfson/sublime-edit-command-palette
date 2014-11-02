# sublime-edit-command-palette

Add/edit commands for your Command Palette

This plugin was created out of frustration that multiple plugin creators write key bindings but nothing for the command palette.

![Animation](https://cloud.githubusercontent.com/assets/902488/4873073/c09b61c2-6200-11e4-8d1c-f149558ef04c.gif)

## Getting Started
### Installation
This package is available under `Edit Command Palette` inside of [Package Control][], a [Sublime Text][] plugin that allows for easy management of other plugins.

[Sublime Text]: http://www.sublimetext.com/
[Package Control]: http://wbond.net/sublime_packages/package_control

If you prefer the manual route, you can install the script via the following command in the Sublime Text terminal (``ctrl+` ``) which utilizes `git clone`.

```python
import os; path=sublime.packages_path(); (os.makedirs(path) if not os.path.exists(path) else None); window.run_command('exec', {'cmd': ['git', 'clone', 'https://github.com/twolfson/sublime-edit-command-palette', 'Edit Command Palette'], 'working_dir': path})
```

Packages can be uninstalled via "Package Control: Remove Package" via the command pallete, `ctrl+shift+p` on Windows/Linux, `command+shift+p` on Mac.

### Command Palette
`sublime-edit-command-palette` provides 2 commands to access Sublime Text's commands:

- `Preferences: Commands - Default` - Opens default commands provided by Sublime Text
- `Preferences: Commands - User` - Opens custom user commands and provides prompt for first-timers

### Menu
`sublime-edit-command-palette` defines 2 menu items under `Preferences -> Package Settings -> Edit Command Palette`:

- `Edit Command Palette - Default` - Opens default commands provided by Sublime Text
- `Edit Command Palette - User` - Opens custom user commands and provides prompt for first-timers

## Documentation
### `edit_command_palette_open_user(self)`
`edit_command_palette_open_user` creates a default `Packages/User/Default.sublime-commands` containing a prompt for the user, opens it, and sets the language to JSON.

We add in the default and language to make it more approachable. Otherwise, it would be an empty file and in plain text by default.

## Contributing
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality.

## Donating
Support this project and [others by twolfson][gratipay] via [gratipay][].

[![Support via Gratipay][gratipay-badge]][gratipay]

[gratipay-badge]: https://cdn.rawgit.com/gratipay/gratipay-badge/2.x.x/dist/gratipay.png
[gratipay]: https://www.gratipay.com/twolfson/

## Unlicense
As of Oct 31 2014, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the [UNLICENSE][].

[UNLICENSE]: UNLICENSE
