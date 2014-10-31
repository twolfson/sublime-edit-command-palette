from os import path
import sublime
import sublime_plugin

SUBLIME_ROOT = path.normpath(path.join(sublime.packages_path(), '..'))
COMMANDS_FILEPATH = path.join('Packages', 'User', 'Commands.sublime-commands')
COMMANDS_FULL_FILEPATH = path.join(SUBLIME_ROOT, COMMANDS_FILEPATH)


class CommandsOpenCommand(sublime_plugin.WindowCommand):
    def run(self):
        """Open `Packages/User/Commands.sublime-commands` for custom definitions"""
        # Open the User commands file
        view = self.window.open_file(COMMANDS_FULL_FILEPATH)

        # If it doesn't exist, provide a prompt
        # TODO: For ST3, we might need to do this before opening the file
        if not path.exists(COMMANDS_FULL_FILEPATH):
            view.
