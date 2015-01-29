
# available commands
# google_image_selected
# google_image_from_input

import sublime
import sublime_plugin

import subprocess
import webbrowser

def query(text):
    # url = 'http://www.google.com/search?q=' + text.replace(' ','%20')
    url = 'http://images.google.com/search?tbm=isch&q=' + text.replace(' ','%20')
    webbrowser.open_new_tab(url)

class GoogleImageSelectedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)

            query(text)

class GoogleImageFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Google Images for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        query(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass
