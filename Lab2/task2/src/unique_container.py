import json
import re


class UniqueContainer:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.current_container = set()

    def add(self, *keys):
        if keys:
            for key in keys:
                if key not in self.current_container:
                    self.current_container.add(key)
            print('Elements were added.')
        else:
            print('There are no elements to add.')

    def remove(self, key):
        if key in self.current_container:
            self.current_container.discard(key)
        else:
            print(f'There is no "{key}" in this container. Nothing to remove.')

    def find(self, *keys):
        if keys:
            found = False
            for key in keys:
                if key in self.current_container:
                    print(key)
                    found = True
            if not found:
                print('No such elements.')
        else:
            print('There is nothing to find.')

    def list(self):
        if self.current_container:
            print('Container contains:')
            for key in self.current_container:
                print(key)
        else:
            print('Container contains nothing.')

    def grep(self, regex):
        pattern = re.compile(regex)
        found = False
        for key in self.current_container:
            if pattern.search(key):
                print(key)
                found = True
        if not found:
            print('No such elements.')

    def save(self):
        filename = f'users/{self.current_user}.json'
        with open(filename, 'w') as f:
            json.dump(list(self.current_container), f)
        print('Container has been saved.')

    def load(self, file=None):
        if file is None:
            filename = f'users/{self.current_user}.json'
        else:
            filename = f'users/{file}'
        try:
            with open(filename, 'r') as f:
                elements_list = json.load(f)
                for element in elements_list:
                    self.current_container.add(element)
            print('Container has been loaded.')
        except FileNotFoundError:
            print(f'Cannot load {filename}: file not found.')

    def switch(self, username):
        self.current_container = set()

        try:
            filename = f'users/{username}.json'
            open(filename, 'r')
            self.current_user = username
            choice = input(f'Welcome back, {username}!\nDo you want to load your saved container? (yes/no): ')

            while choice != 'yes' and choice != 'no':
                choice = input('Incorrect input! Type \'yes\' or \'no\': ')

            if choice == 'yes':
                print(f'Loading container for {username}.')
                self.load()
            else:
                self.current_container = set()
        except FileNotFoundError:
            choice = input(f'Hello, {username}!\nDo you want to load container from file? (yes/no): ')

            while choice != 'yes' and choice != 'no':
                choice = input('Incorrect input! Type \'yes\' or \'no\': ')

            if choice == 'yes':
                file = input("Input file name (it should be in the users directory): ")
                filename = str(file)
                try:
                    open(filename, 'r')
                    self.current_user = username
                    self.users[self.current_user] = self.current_container
                except FileNotFoundError:
                    print(f'Hello, {username}. Creating a new container.')
                    self.current_container = set()
                self.load(file=filename)
            else:
                self.current_container = set()
