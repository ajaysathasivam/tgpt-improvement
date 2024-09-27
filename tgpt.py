import os
import re
import subprocess
class tgpt():
    def __init__(self, promt):
        self.promt=promt
        self.connection=subprocess.run(['nmcli','networking','connectivity','check'], capture_output=True, text=True)
        os.system(f'echo {self.promt} >/tmp/promt.txt')  
    def check(self):
        connected=self.connection.stdout
        connected=connected[0:4]
        if (connected=='full'):
            self.input_tgpt()
            self.store()
        else:
            print("Check Your Internet Connected Or Not")
    def input_tgpt(self):
        output=subprocess.run(['tgpt', self.promt], capture_output=True, text=True)
        output=output.stdout
        output = re.sub(r'[\u2800-\u28FF]\s*Loading', '', output)
        output =output.strip()
        save=input("If you save this file YES OR NO: ")
        if save.lower()=='yes':
            self.store(output)
        else:
            print("This Promt Not saved")
            print(output)
    def store(self, output):
        fname=input("What you name to save it: ")
        # subprocess.run('echo',output,'>>','/home/novo/promt/',fname)
        os.system(f'echo {output}>>/home/novo/promt/{fname}')
        print("I stored",fname)
promt=input("Enter Your Promt: ")
promt_obj=tgpt(promt)
promt_obj.check()


