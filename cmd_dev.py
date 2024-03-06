import cmd
from uuid import uuid4
import readline

class MyClass(cmd.Cmd):
    prompt = "(input) > "

    def preloop(self):
        try:
            self.load_history()
        except FileNotFoundError:
            pass
    
    def postloop(self):
        self.save_history()
    
    def load_history(self):
        """Load command history from a file"""
        self.history = []
        with open('command_history.txt', 'r') as file:
            for line in file:
                self.history.append(line.strip())
    
    def save_history(self):
        """Save command history to a file"""
        with open('command_history.txt', 'w') as file:
            for line in self.history:
                file.write(line + '\n')

    def do_quit(self, arg):
        """Quit the command line"""
        return True
    def do_uid(self, arg):
        """get the unique user identity"""
        user = uuid4()
        print(f"User ID is {user}")
    def do_history(self, arg):
        """Print command history"""
        for idx, cmd in enumerate(self.history, start=1):
            print(f"{idx}: {cmd}")
    
    def default(self, line):
        """Default handler for unrecognized commands"""
        self.history.append(line)
        print("Command not recognized. Type 'help' for a list of commands.")


MyClass().cmdloop()