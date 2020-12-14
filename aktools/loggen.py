from ak_tools.conf import *

def generate_log_files(nb_log_lines):
    log_count=1
    while 1:
        file = open("output/"+'log_'+str(log_count)+'.txt', 'a')
        
        for i in range(0,nb_log_lines):
            timeout = time.time() + 60*5   # 5 minutes from now
            #signal.alarm(300) # if this takes more than 5 minutes, kill myself
            time.sleep(1)
            file.write(str(int(time.time()*1000))+' '+random.choice(hosts)+' '+random.choice(hosts)+'\n')
            file.flush()

            if time.time() > timeout:
                break

        print('log file '+str(log_count)+' finished')
        log_count+=1
