from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class AppLauncher(App):
    def build(self):
        layout = GridLayout(cols=3, rows=3, spacing=10, padding=10)
        
        apps = {
            "calculator": "com.android.calculator2",
            "camera": "com.android.camera",
            "clock": "com.google.android.deskclock",
            "contacts": "com.android.contacts",
            "gallery": "com.android.gallery3d",
            "music": "com.android.music",
            "settings": "com.android.settings"

        }
        
        for app_name, package_name in apps.items():
            button = Button(text=app_name)
            button.bind(on_press=lambda x: self.launch_app(package_name))
            layout.add_widget(button)
        
        return layout

    def launch_app(self, package_name):
        import android.intent as Intent
        Intent.start_activity(package=package_name)

if __name__ == "__main__":
    AppLauncher().run()
