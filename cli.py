import shlex

def cmd_help():
    pass

def debug_msg():
    pass

COMMANDS = {
    "help": cmd_help,
    
}

def main():
    print("arduino shell — type /help, /exit to quit")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):   # Ctrl-D / Ctrl-C
            print()
            break
        if not line:
            continue
        if line in ("/exit", "/quit"):
            break
        if line.startswith("/"):
            name, *args = shlex.split(line[1:])
            fn = COMMANDS.get(name)
            if fn is None:
                print(f"unknown command: /{name}")
                continue
            try:
                fn(args)
            except Exception as e:
                print(f"error: {e}")
        else:
            print(f"Not a valid command")
            continue

if __name__ == '__main__':
    main()