# add a way to copy that shit into clipboard

import sys
import os
from tools import prompt_option

go_cmd_path = r"C:\Users\E161262\OneDrive - Mastercard\Documents\TASKS\go\go_temp.cmd"

def write_temp(path):
    if path:
        with open(go_cmd_path, 'w') as f:
            if path[1] == ':':
                if os.getcwd()[:2] != path[:2]:
                    f.write(path[:2] + '\n')
            f.write('cd "' + path + '"\n')
    else:
        with open(go_cmd_path, 'w') as f:
            f.write('')

def get_next_path_match():
    global path
    global dir_gen
    while True:
        try:
            new_dir, *_ = next(dir_gen)
        except StopIteration:
            new_dir = ''
        # extra matching algos
        # sys.stdout.write('\x1b[2K\r' + new_dir)
        if new_dir:
            if path in os.path.basename(new_dir):
                res = new_dir
                break
        else:
            res = None 
            break
    return res

if sys.argv[1:]:
    path = sys.argv[1]        
    # check if shortcut is predefined
    if path in os.environ:
        if os.path.isdir(os.environ[path]):
            path = os.environ[path]
            write_temp(path)
            exit(0)

    if os.path.isdir(path):
        write_temp(path)
        exit(0)

    # search for pattern in current directory and recursively in the sub directories
    results = []
    dir_gen = os.walk('.')
    current_idx = 0
    while True:
        try:
            if current_idx >= len(results):
                sys.stdout.write('\x1b[2K\rScanning...')
                new_dir = get_next_path_match()
                if not new_dir:
                    if results:
                        current_idx = len(results)-1
                    else:
                        sys.stdout.write('Nothing found')
                        raise KeyboardInterrupt('')
                    pass
                else:
                    results.append(new_dir)
            
            resp = prompt_option(results[current_idx])
            if resp == 0:
                write_temp(results[current_idx])
                exit(0)
            elif resp == 1:
                current_idx += 1
                continue
            elif resp == -1:
                current_idx = max(current_idx-1, 0)
                continue
            elif resp == 3:
                raise KeyboardInterrupt
        except KeyboardInterrupt:
            write_temp(None)
            break

    # matches = [f for f in f'*{path}*' if os.path.isdir(f)]
    # matches += [f for f in glob(f'**\\*{path}*', recursive=True) if os.path.isdir(f)]
    # if matches:
    #     from tools import choose_prompt
    #     path = choose_prompt(matches)
    #     write_temp(path)
    #     exit(0)
    # else:
    #     print('No matches for', path)
    #     path = None
    #     write_temp(path)
    #     exit(0)
    
    # fuzzy match

    
