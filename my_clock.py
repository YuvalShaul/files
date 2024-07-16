from datetime import datetime
import time



while(True):
    with  open ('/usr/share/nginx/html/mytime.html', 'w') as timefile:

        # datetime object containing current date and time
        now = datetime.now()

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S\n")
        timefile.write(dt_string + " !!! ")
    time.sleep(3)