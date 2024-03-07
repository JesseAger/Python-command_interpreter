import cmd
from uuid import uuid4
import readline
import os


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
        """Get the unique user identity"""
        user = uuid4()

    def do_create(self, arg):
        """Create a new file"""
        filename = arg.strip()  
        try:
            with open(filename, 'w') as file:
                print(f"File '{filename}' created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")

    def load_dir(self):
        """Load the contents of the current directory into a list"""
        try:
            self.directory = os.listdir('.')
        except Exception as e:
            print(f"Error loading directory contents: {e}")
            self.directory = []
    
    def do_dir(self, arg):
        """Get the list of all files and subdirectories in the current directory"""
        self.load_dir()  
        if not self.directory:
            print("No directory contents loaded.")
            return
        print("Directory contents:")
        for item in self.directory:
            print(item)


    def do_history(self, arg):
        """Print command history"""
        for idx, cmd in enumerate(self.history, start=1):
            print(f"{idx}: {cmd}")
    
    def default(self, line):
        """Default handler for unrecognized commands"""
        self.history.append(line)
        print("Command not recognized. Type 'help' for a list of commands.")


MyClass().cmdloop()