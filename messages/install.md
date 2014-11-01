# sublime-commands

Add new commands to your Command Palette

This plugin was created out of frustration that multiple plugin creators write key bindings but nothing for the command palette.

## Getting Started
### Command Palette
`sublime-commands` provides 2 commands to access Sublime Text's commands:

- `Preferences: Commands - Default` - Opens default commands provided by Sublime Text
- `Preferences: Commands - User` - Opens custom user commands and provides prompt for first-timers

### Menu
`sublime-commands` defines 2 menu items under `Preferences -> Package Settings -> Commands`:

- `Commands - Default` - Opens default commands provided by Sublime Text
- `Commands - User` - Opens custom user commands and provides prompt for first-timers

## Documentation
### `commands_open_user(self)`
`commands_open_user` creates a default `Packages/User/Commands.sublime-settings` containing a prompt for the user, opens it, and sets the language to JSON.

We add in the default and language to make it more approachable. Otherwise, it would be an empty file and in plain text by default.

## Contributing
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality.

## Donating
Support this project and others by twolfson via gratipay.

https://www.gratipay.com/twolfson/

## Unlicense
As of Oct 31 2014, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the [UNLICENSE][].

[UNLICENSE]: ../UNLICENSE
