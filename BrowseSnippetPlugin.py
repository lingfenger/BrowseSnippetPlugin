import sublime, sublime_plugin #plugin must import these two modual
import os, os.path
from glob import glob

class BrowseSnippetPluginCommand(sublime_plugin.TextCommand):
    def run(self,edit, ftype = None):
        self.user_path = sublime.packages_path() + "\\user"
        self.type_name = ""
        if "sublime-snippet" == ftype:
             self.type_name = "Snippet File: "
        elif "py" ==  ftype:
            self.type_name = "Plugin File: "
        else:
            self.type_name = "Unknow File: "
        self.file_list = []

        os.chdir(self.user_path)
        extension = '*.' + ftype
        self.file_list += [os.path.realpath(e) for e in glob(extension)]

        file_name_list = []
        if self.file_list:
            for afile in self.file_list:
                fname, fext=os.path.splitext(os.path.split(afile)[1]);
                file_name_list.append(self.type_name + fname)

        if  file_name_list:
            self.view.window().show_quick_panel(file_name_list, self.panel_done, sublime.MONOSPACE_FONT, -1, self.on_highlight)

    def panel_done(self, SelectedIndex):
        if SelectedIndex >= 0:
            self.view.window().open_file(self.file_list[SelectedIndex], sublime.TRANSIENT)

    def on_highlight(self, SelectedIndex):
        self.view.window().open_file(self.file_list[SelectedIndex], sublime.TRANSIENT)

        

