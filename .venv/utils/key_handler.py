keys_pressed = {"Up": False, "Down": False, "w": False, "s": False}

def key_down(key):
    keys_pressed[key] = True

def key_up(key):
    keys_pressed[key] = False
