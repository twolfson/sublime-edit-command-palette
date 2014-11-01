from os import path
import shutil
import sublime
import sublime_plugin

SUBLIME_ROOT = path.normpath(path.join(sublime.packages_path(), '..'))
COMMANDS_FILEPATH = path.join('Packages', 'User', 'Commands.sublime-commands')
COMMANDS_FULL_FILEPATH = path.join(SUBLIME_ROOT, COMMANDS_FILEPATH)

# DEV: We must use `__file__` since ST3 executes from `Packages/` instead of `Packages/Commands/`
COMMANDS_SOURCE_FULL_FILEPATH = path.normpath(path.join(__file__, '..', 'default-prompt.json'))

class CommandsOpenUserCommand(sublime_plugin.WindowCommand):
    def run(self):
        """Open `Packages/User/Commands.sublime-commands` for custom definitions"""
        # If the User commands doesn't exist, provide a prompt
        if not path.exists(COMMANDS_FULL_FILEPATH):
            shutil.copy(COMMANDS_SOURCE_FULL_FILEPATH, COMMANDS_FULL_FILEPATH)

        # Open the User commands file
        view = self.window.open_file(COMMANDS_FULL_FILEPATH)

        # If the syntax is plain text, move to JSON
        # DEV: Syntax paths always use `/`, even on Windows via https://github.com/wbond/package_control_channel/pull/3780#issuecomment-61369387
        if view.settings().get('syntax') == 'Packages/Text/Plain text.tmLanguage':
            view.set_syntax_file('Packages/JavaScript/JSON.tmLanguage')
