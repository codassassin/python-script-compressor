import argparse
import os
import sys


def banner():
    print('<<< PythonScript-Compressor v1.0>>>')
    print(r'''
  _
 | |
 | |___
 |  _  \ _   _
 | |_)  | (_) |
  \____/ \__, |
          __/ |
         |___/
                                        _                                                         _
                                       | |                                                       (_)
                  ____     ____     ___| |   ___ _   ______   ______    ___ _   ______   ______   _   _ ____
                 / ___\   /    \   /  _  |  / _ | | /  ____| /  ____|  / _ | | /  ____| /  ____| | | | |   | \
                | |____  |  ()  | |  (_| | | (_|| | \_____ \ \_____ \ | (_|| | \_____ \ \_____ \ | | | |   | |
                 \____/   \____/   \____/   \___|_| |______/ |______/  \___|_| |______/ |______/ |_| |_|   |_|
     ''')


if __name__ == '__main__':
    banner()
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("script", type=str)
        args = parser.parse_args()

        if not os.path.exists(args.script):
            sys.stderr.write(f"'{args.script}' not a file")

        with open(args.script, "rb") as h:
            contents = h.read().decode('utf-8')

        code = "+".join([f"chr({ord(x)})" for x in contents])
        code = f"{code}"

        script = "+".join([f"chr({ord(x)})" for x in "<script>"])
        script = f"{script}"

        executable = "+".join([f"chr({ord(x)})" for x in "exec"])
        executable = f"{executable}"

        compressedCommand = f'python -c "exec(compile({code}, {script}, {executable}))"'

        with open('scripts.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if args.script not in nameList:
                f.writelines(f'\n{args.script},{compressedCommand}')

        print("[+] The compressed command is: (just copy the command and run)\n\t" + compressedCommand)

    except Exception as e:
        print(f"[-] ERROR: {e}")
