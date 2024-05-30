import json
import psutil
import os
import time

class AutoApps:

    def get_data(self):
        with open("./data.json") as e:
            data = json.load(e)

        return data["Apps"]
     
    def usage_limit(self):
        if psutil.cpu_percent() >= 80 and psutil.virtual_memory().percent >= 90:
            return True

    def close_apps(self):
        data = self.get_data()
        for app in data:
            try:
                os.system(f"taskkill /IM {app} /F")
            except:
                pass

    def main(self):
        while True:
            time.sleep(2)
            if self.usage_limit():
                self.close_apps()
                print("paused")
                return True