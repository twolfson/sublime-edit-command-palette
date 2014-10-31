from os import path
import sublime
import sublime_plugin

SUBLIME_ROOT = path.normpath(path.join(sublime.packages_path(), '..'))
COMMANDS_FILEPATH = path.join('Packages', 'User', 'Commands.sublime-commands')
COMMANDS_FULL_FILEPATH = path.join(SUBLIME_ROOT, COMMANDS_FILEPATH)

class CommandsEventListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        """
        When we save a .sublime-settings file, re-populate `Packages/User/Commands.sublime-settings`

        # DEV: Technically, we should only pay attention to `Packages/User/Preferences.sublime-settings`
            However, that can cause more frustration than it solves
        """
        # If the file is not a settings file, exit early
        filepath = view.file_name()
        if not filepath.endswith('.sublime-settings'):
            return
