# add a way to copy that shit into clipboard

import sys
import os
from glob import glob

go_cmd_path = r"go_temp.cmd"

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
    matches = [f for f in f'*{path}*' if os.path.isdir(f)]
    matches += [f for f in glob(f'**\\*{path}*', recursive=True) if os.path.isdir(f)]
    if matches:
        from tools import choose_prompt
        path = choose_prompt(matches)
        write_temp(path)
        exit(0)
    else:
        print('No matches for', path)
        path = None
        write_temp(path)
        exit(0)
    
    # fuzzy match

    
