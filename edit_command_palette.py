from os import path
import sublime
import sublime_plugin

# Define dictionary for path constants and default content
C = {}
DEFAULT_CONTENT = """[
    // Define your custom Sublime commands here
    // Format is same as `key bindings` except replace `keys` with `caption`
    // {
    //     // Name to show in Command Palette
    //     "caption": "File: New",
    //     // Command to invoke
    //     "command": "new_file",
    //     // Optional keyword arguments to provide to command
    //     "args": {"key": "value"}
    // }
]"""


def plugin_loaded():
    """Once the plugin has loaded, define constants"""
    C['SUBLIME_ROOT'] = path.normpath(path.join(sublime.packages_path(), '..'))
    C['COMMANDS_FILEPATH'] = path.join('Packages', 'User', 'Default.sublime-commands')
    C['COMMANDS_POSIX_FILEPATH'] = 'Packages/User/Default.sublime-commands'
    C['COMMANDS_FULL_FILEPATH'] = path.join(C['SUBLIME_ROOT'], C['COMMANDS_FILEPATH'])


class EditCommandPaletteOpenFileCommand(sublime_plugin.WindowCommand):
    def run(self, file):
        """Open a commands file with default JSON syntax"""
        # Open the commands file
        # DEV: We use this because `${packages}` is not easy to resolve in ST3
        self.window.run_command('open_file', {
            'file': file,
        })

        # If the syntax is plain text, move to JSON
        # DEV: Syntax paths always use `/`, even on Windows via https://github.com/wbond/package_control_channel/pull/3780#issuecomment-61369387
        view = self.window.active_view()
        if view.settings().get('syntax') == 'Packages/Text/Plain text.tmLanguage':
            view.set_syntax_file('Packages/JavaScript/JSON.tmLanguage')


class EditCommandPaletteOpenUserCommand(sublime_plugin.WindowCommand):
    def run(self):
        """Open `Packages/User/Default.sublime-commands` for custom definitions"""
        # If the User commands doesn't exist, provide a prompt
        filepath = C['COMMANDS_FULL_FILEPATH']
        if not path.exists(filepath):
            with open(filepath, 'w') as f:
                f.write(DEFAULT_CONTENT)

        # Open the commands file
        self.window.run_command('edit_command_palette_open_file', {
            'file': C['COMMANDS_POSIX_FILEPATH'],
        })


# If we are not in ST3, run `plugin_loaded` by default
if sublime.version() < '3000':
    plugin_loaded()
