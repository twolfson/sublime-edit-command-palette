from os import path
import shutil
import sublime
import sublime_plugin

SUBLIME_ROOT = path.normpath(path.join(sublime.packages_path(), '..'))
COMMANDS_FILEPATH = path.join('Packages', 'User', 'Commands.sublime-commands')
COMMANDS_FULL_FILEPATH = path.join(SUBLIME_ROOT, COMMANDS_FILEPATH)

COMMANDS_SOURCE_FULL_FILEPATH = path.abspath('default-prompt.json')

class CommandsOpenCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        """Open `.sublime-commands` file for custom definitions"""
        # If no file is provided, default to `COMMANDS_FULL_FILEPATH`
        dest_filepath = kwargs.get('file', COMMANDS_FULL_FILEPATH)

        # If the file doesn't exist, provide a prompt
        if not path.exists(dest_filepath):
            shutil.copy(COMMANDS_SOURCE_FULL_FILEPATH, dest_filepath)

        # Open the User commands file
        view = self.window.open_file(dest_filepath)

        # If the syntax is plain text, move to JSON
        if view.settings().get('syntax') == path.join('Packages', 'Text', 'Plain text.tmLanguage'):
            view.set_syntax_file(path.join('Packages', 'JavaScript', 'JSON.tmLanguage'))
