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
    pd('''РЫЦАРЬ, КОТОРЫЙ НИЧЕГО НЕ БОИТСЯ
--------------------------------------------
--------------------------------------------
--------------------------------------------''')
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
    time.sleep(3)
    print('''
— Мой лорд, — произнёс голос позади,
и рыцарь обернулся, увидев своего верного спутника,
облачённого в доспехи, но с лицом, выражающим тревогу.
— Мы приближаемся к месту, окутанному мраком и легендами.
''')
    time.sleep(4)
    pd('''
Рыцарь кивнул, его взгляд был устремлён на замок, возвышающийся на горизонте.
Тёмные облака нависали над ним, словно предвестники судьбы,
и в воздухе витало ощущение грядущего испытания.
''')
    time.sleep(3)
    print('''
— Мы здесь не ради славы, — сказал рыцарь,
его голос был твёрд и решителен.
— Мы здесь, чтобы спасти короля,
нашего повелителя, чья жизнь и честь находятся в опасности.
''')
    stop_flag.set()
    music_thread.join()
    
    


if __name__ == "__main__":
    main()
