import sys

if sys.platform.startswith("win"):
    import msvcrt

    def get_key():
        first = msvcrt.getch()
        if first == b'\xe0':  # Arrow keys or function keys
            second = msvcrt.getch()
            if second == b'H':
                return 'UP'
            elif second == b'P':
                return 'DOWN'
            elif second == b'K':
                return 'LEFT'
            elif second == b'M':
                return 'RIGHT'
        elif first == b'\x1b':
            return 'ESC'
        else:
            return first.decode(errors='ignore')

else:
    import tty
    import termios

    def get_key():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch1 = sys.stdin.read(1)
            if ch1 == '\x1b':
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A':
                        return 'UP'
                    elif ch3 == 'B':
                        return 'DOWN'
                    elif ch3 == 'C':
                        return 'RIGHT'
                    elif ch3 == 'D':
                        return 'LEFT'
                return 'ESC'
            else:
                return ch1
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

import os 

MAX_LEN = os.get_terminal_size().columns
repr_line = lambda line: '...' + line[:MAX_LEN-3] if len(line) > MAX_LEN else line

def choose_prompt(options_list):
    if options_list:
        if len(options_list)==1:
            return options_list[0]

        width = len(str(len(options_list) - 1))
        options = [f'{str(fidx).rjust(width)}: {f}' for fidx, f in enumerate(options_list)]
        idx = 0
        sys.stdout.write(repr_line(options[idx]))
        sys.stdout.flush()
        while True:
            dirkey = get_key()
            if dirkey in ['\r', '\n']:
                sys.stdout.write('\r'+ ' '*MAX_LEN)
                sys.stdout.write('\r')
                return options_list[idx]
            if dirkey in ['\x03']:
                sys.stdout.write('\r'+ ' '*MAX_LEN)
                sys.stdout.write('\r')
                return None
            sys.stdout.write('\r'+ ' '*MAX_LEN)
            idx = min(idx+1, len(options)-1) if dirkey in ['DOWN', 'RIGHT'] else max(idx-1, 0)
            sys.stdout.write('\r' + repr_line(options[idx]))
            sys.stdout.flush()
    else:
        return None
