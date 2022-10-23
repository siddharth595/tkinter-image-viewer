import json
import os
class Theme:
    def __init__(self):
        themeDictionary = self.readTheme()
        self.themes = themeDictionary["themes"]
        self.currentTheme=themeDictionary["lastTheme"]
        
    
        
    
    def set_theme(self, background, foreground, buttonBackground):
            self.root.configure(bg=background)
            self.name_label.configure(bg=background, fg=foreground)
            self.display.configure(bg=background)
            self.move_left_button.configure(bg=buttonBackground, fg=foreground)
            self.move_right_button.configure(bg=buttonBackground, fg=foreground)
            

    def readTheme(self):
        with open('Image_Viewer/themes.json', 'r') as openfile:
            json_object = json.load(openfile)
            return json_object
    
    def writeTheme(self):
        themeDictionary = {"themes":self.themes,"lastTheme":self.currentTheme}
        json_object = json.dumps(themeDictionary, indent=4)
        with open('Image_Viewer/themes.json','w') as openfile:
            
            openfile.write(json_object)
            
    def changeTheme(self,theme):
        print(self.themes[theme])
        self.set_theme(**self.themes[theme])
        self.currentTheme=theme
        self.writeTheme()