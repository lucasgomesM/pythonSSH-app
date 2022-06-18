from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
import paramiko
Builder.load_file('App_.kv')

class App_(ScreenManager):
    pass

class PythonFun(App):
    def build(self):       
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())        
        return App_()        
    
    def commands(self, text, response):
        stdin , stdout ,stderr = self.client.exec_command(text.text)
        outString = (stdout.read()).decode("utf-8")
        response.text = "battlestation: \n{}".format(outString)
        if len(outString) > 2300:            
            response.height = 2300
        else:
            response.height = len(outString)

        if response.height > 100 and response.height < 400:
            text.height -= response.height 
            response.height += 120
        elif response.height < 50:
            response.height = 100
        
        else:
            text.height = 400
    def reader(self, text, response):
        pass

    def connect(self,ip,user,pwd,scManager):
        try:
            self.client.connect(ip.text,22,user.text,pwd.text,timeout=1.5)
            scManager.current = 'main_Screen'
        except:
            scManager.current = 'error_Screen'
            print("Error Conecting to the server...")

    def back(self, scManager):
        scManager.current = 'access_Screen'


if __name__ == "__main__":
    PythonFun().run()