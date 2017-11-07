from kivy.app import App
from kivy.uix.settings import SettingsWithTabbedPanel
from kivy.properties import ListProperty
from kivy.logger import Logger
from kivy.lang import Builder
from kivy.config import ConfigParser

# import gpio plan
from gpioconf import gpioconfig

# read firebase
from firetest import firetest
from io_dict import IO_Dictionary

from internetchecker import internetChecker
import os

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
        TODO : Get value from firebase
        """
        try :
            # requires for replacing firebase current settings
            os.remove('my.ini')
        except Exception as ex:
            print('error removing generated ini file :',ex)

        mfiretest = firetest()
        mfiretest.test() #testing OK
        gpiodata = mfiretest.getdata()
        d = IO_Dictionary(gpiodata)
        fpm17 = d["P17"]["mode"] #GPIO.IN
        fpm18 = d["P18"]["mode"]
        fps17 = d["P17"]["state"] #False
        fps18 = d["P18"]["state"]
        fpwm17 = d["P17"]["pwm"] #False
        fpwm18 = d["P18"]["pwm"] #False
        ffreq17 = d["P17"]["freq"] #1000
        ffreq18 = d["P18"]["freq"] #1000
        fdc17 = d["P17"]["dc"] #100
        fdc18 = d["P18"]["dc"] #100

        # getp17profile = config.get('fp17mode')
        print("P17 profile :",fpm17,fps17,fpwm17,ffreq17,fdc17)

        """
        Set the default values for the configs sections.
        """
        config.setdefaults(
            'P17', {
            'p17mode': fpm17,
            'p17state':fps17,
            'p17pwm': fpwm17,
            'p17freq': ffreq17,
            'p17dc':fdc17})

        config.setdefaults(
            'P18', {
            'p18mode': fpm18,
            'p18state':fps18,
            'p18pwm': fpwm18,
            'p18freq': ffreq18,
            'p18dc':fdc18})

    def build_settings(self, settings):
        """
        Add our custom section to the default configuration object.
        """
        # We use the string defined above for our JSON, but it could also be
        # loaded from a file as follows:
        #     settings.add_json_panel('My Label', self.config, 'settings.json')
        # settings.add_json_panel('GPIO Settings', self.config, data=json)

        settings.add_json_panel('GPIO', self.config, data=gpioconfig)

    def on_config_change(self, config, section, key, value):
        """
        Respond to changes in the configuration.
        TODO: upload stream
        """
        Logger.info("main.py: App.on_config_change: {0}, {1}, {2}, {3}".format(
            config, section, key, value))
        

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
