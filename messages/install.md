# sublime-commands

Make `Default` and `User` commands more accessible

This plugin was created out of frustration that multiple plugin creators write key bindings but nothing for the command palette. This fixes that by making the `User's .sublime-commands` available via the command palette and menu.

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
