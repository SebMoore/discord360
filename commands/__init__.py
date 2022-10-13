from .RunPresence import entry as RunPresence

commands = [
    RunPresence
]

def start():
    for command in commands:
        command.start()

def stop():
    for command in commands:
        command.stop()