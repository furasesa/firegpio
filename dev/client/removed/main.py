from kivy.app import App
from kivy.uix.settings import SettingsWithTabbedPanel
from kivy.properties import ListProperty
from kivy.logger import Logger
from kivy.lang import Builder

# from firebase import firebase

from internetchecker import internetChecker

# This JSON defines entries we want to appear in our App configuration screen
json = '''


# [
#     {
#         "type": "title",
#         "title": "P17"
#     },
#     {
#         "type": "options",
#         "title": "Mode",
#         "desc": "there 2 modes, GPIO.OUT or GPIO.IN",
#         "section": "P17",
#         "options": ["GPIO.IN","GPIO.OUT"],
#         "key": "p17mode"
#     },
#     {
#         "type" : "bool",
#         "title" : "State",
#         "desc" : "The default is OFF",
#         "section" : "P17",
#         "key" : "p17state"
#     },
#     {
#         "type": "bool",
#         "title": "PWM",
#         "desc": "Pulse with modulation, mode must be GPIO.OUT",
#         "section" : "P17",
#         "key" : "p17pwm"
#     },
#     {
#         "type": "numeric",
#         "title": "Frequencies",
#         "desc": "range between 1 - 10000 Hz",
#         "section" : "P17",
#         "key" : "p17freq"
#     },
#     {
#         "type": "numeric",
#         "title": "Duty Cycle",
#         "desc": "value in percent between 1 - 100",
#         "section" : "P17",
#         "key" : "p17dc"
#     },

#     {
#         "type": "title",
#         "title": "P18"
#     },
#     {
#         "type": "options",
#         "title": "Mode",
#         "desc": "there 2 modes, GPIO.OUT or GPIO.IN",
#         "section": "P18",
#         "options": ["GPIO.IN","GPIO.OUT"],
#         "key": "p18mode"
#     },
#     {
#         "type" : "bool",
#         "title" : "State",
#         "desc" : "The default is OFF",
#         "section" : "P18",
#         "key" : "p18state"
#     },
#     {
#         "type": "bool",
#         "title": "PWM",
#         "desc": "Pulse with modulation, mode must be GPIO.OUT",
#         "section" : "P18",
#         "key" : "p18pwm"
#     },
#     {
#         "type": "numeric",
#         "title": "Frequencies",
#         "desc": "range between 1 - 10000 Hz",
#         "section" : "P18",
#         "key" : "p18freq"
#     },
#     {
#         "type": "numeric",
#         "title": "Duty Cycle",
#         "desc": "value in percent between 1 - 100",
#         "section" : "P18",
#         "key" : "p18dc"
#     }

# ]
'''

class MyApp(App):
    def build(self):
        """
        Build and return the root widget.
        """
        # The line below is optional. You could leave it out or use one of the
        # standard options, such as SettingsWithSidebar, SettingsWithSpinner
        # etc.
        self.settings_cls = MySettingsWithTabbedPanel

        # We apply the saved configuration settings or the defaults
        root = Builder.load_file('settings.kv')
        label = root.ids.label
        internet = internetChecker()
        internet.isOnline()
        print ("has internet ?",internet.isOnline())
        if internet.isOnline():
            label.text = "Online is available"
        else:
            label.text = "no internet"


        # label.text = self.config.get('My Label', 'text')
        # label.font_size = float(self.config.get('My Label', 'font_size'))
        return root

    def build_config(self, config):
        """
        Set the default values for the configs sections.
        """
        config.setdefaults(
            'P17', {
            'p17mode': 'GPIO.IN',
            'p17state':'False',
            'p17pwm': 'False',
            'p17freq': 1000,
            'p17dc':100})

        # config.setdefaults(
        #     'P18', {
        #     'p18mode': 'GPIO.IN',
        #     'p18state':'False',
        #     'p18pwm': 'False',
        #     'p18freq': 1000,
        #     'p18dc':100})

    def build_settings(self, settings):
        """
        Add our custom section to the default configuration object.
        """
        # We use the string defined above for our JSON, but it could also be
        # loaded from a file as follows:
        #     settings.add_json_panel('My Label', self.config, 'settings.json')
        settings.add_json_panel('GPIO Settings', self.config, data=json)

    def on_config_change(self, config, section, key, value):
        """
        Respond to changes in the configuration.
        TODO: upload stream
        """
        Logger.info("main.py: App.on_config_change: {0}, {1}, {2}, {3}".format(
            config, section, key, value))

        firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)

        # if section == "My Label":
        #     if key == "text":
        #         self.root.ids.label.text = value
        #     elif key == 'font_size':
        #         self.root.ids.label.font_size = float(value)

    def close_settings(self, settings=None):
        """
        The settings panel has been closed.
        """
        Logger.info("main.py: App.close_settings: {0}".format(settings))
        super(MyApp, self).close_settings(settings)


class MySettingsWithTabbedPanel(SettingsWithTabbedPanel):
    """
    It is not usually necessary to create subclass of a settings panel. There
    are many built-in types that you can use out of the box
    (SettingsWithSidebar, SettingsWithSpinner etc.).

    You would only want to create a Settings subclass like this if you want to
    change the behavior or appearance of an existing Settings class.
    """
    def on_close(self):
        Logger.info("main.py: MySettingsWithTabbedPanel.on_close")

    def on_config_change(self, config, section, key, value):
        Logger.info(
            "main.py: MySettingsWithTabbedPanel.on_config_change: "
            "{0}, {1}, {2}, {3}".format(config, section, key, value))


MyApp().run()
