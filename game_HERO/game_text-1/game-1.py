import time
from playsound import playsound
import threading

def pd(text, delay = 0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
def play_music(music_file, stop_flag):
    while not stop_flag.is_set():
        playsound(music_file)
        
def main():
    stop_flag = threading.Event()
    music_thread = threading.Thread(target=play_music, args=('01 - Opening.ogg', stop_flag))
    music_thread.start()
    pd('''РЫЦАРЬ, КОТОРЫЙ НИЧЕГО НЕ БОИТСЯ''')
    stop_flag.set()
    music_thread.join()
    stop_flag.clear() 
    
    music_thread = threading.Thread(target=play_music, args=('09 - Z 339 - Here the Deities approve.ogg', stop_flag))
    music_thread.start()
    pd('''В дни, когда земля ещё хранила эхо древних битв,
когда магия струилась в жилах мира,
а герои были не просто именами в легендах,
жил-был рыцарь, чьё сердце пылало отвагой и честью.
Он стоял на холме, где ветер шептал тайны веков,
а солнце бросало лучи на его сверкающие доспехи.''')
    stop_flag.set()
    music_thread.join()
    
    


if __name__ == "__main__":
    main()
