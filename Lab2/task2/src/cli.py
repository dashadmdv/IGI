from .unique_container import UniqueContainer


class CLI:
    def run(self):
        container = UniqueContainer()
        print('Welcome to UniqueStorageCLI!')
        username = input('Please enter your username: ')
        container.switch(username)

        while True:
            print('\nType command. (\'help\' to see all available commands)')
            command = input('> ')
            if command.startswith('help'):
                if len(command.split()) > 1:
                    print(f'Too many arguments for this command. Expected: 0, given: {len(command.split()) - 1}')
                else:
                    self.print_help()
            elif command.startswith('add'):
                if len(command.split()) == 1:
                    print(f'Too few arguments for this command. Expected: minimum 1, given: {len(command.split()) - 1}')
                else:
                    container.add(*command.split()[1:])
            elif command.startswith('remove'):
                if len(command.split()) == 1:
                    print(f'Too few arguments for this command. Expected: 1, given: {len(command.split()) - 1}')
                elif len(command.split()) > 2:
                    print(f'Too many arguments for this command. Expected: 1, given: {len(command.split()) - 1}')
                else:
                    container.remove(command.split()[1])
            elif command.startswith('find'):
                container.find(*command.split()[1:])
            elif command.startswith('list'):
                container.list()
            elif command.startswith('grep'):
                if len(command.split()) > 2:
                    print(f'Too many arguments for this command. Expected: 1, given: {len(command.split()) - 1}')
                else:
                    container.grep(*command.split()[1])
            elif command.startswith('save'):
                if len(command.split()) > 1:
                    print(f'Too many arguments for this command. Expected: 0, given: {len(command.split()) - 1}')
                else:
                    container.save()
            elif command.startswith('load'):
                if len(command.split()) > 1:
                    print(f'Too many arguments for this command. Expected: 0, given: {len(command.split()) - 1}')
                else:
                    container.load()
            elif command.startswith('switch'):
                if len(command.split()) > 1:
                    print(f'Too many arguments for this command. Expected: 0, given: {len(command.split()) - 1}')
                else:
                    choice = input(f'Do you want to save your container? (yes/no): ')

                    while choice != 'yes' and choice != 'no':
                        choice = input('Incorrect input! Type \'yes\' or \'no\': ')

                    if choice == 'no':
                        container.current_container = set()
                    else:
                        print(f'Saving container for {container.current_user}.')
                    container.users[container.current_user] = container.current_container

                    new_username = input('Please enter the new username: ')
                    container.switch(new_username)
            elif command.startswith('exit'):
                if len(command.split()) > 1:
                    print(f'Too many arguments for this command. Expected: 0, given: {len(command.split()) - 1}')
                else:
                    choice = input(f'Do you want to save your container? (yes/no): ')

                    while choice != 'yes' and choice != 'no':
                        choice = input('Incorrect input! Type \'yes\' or \'no\': ')

                    if choice == 'no':
                        container.current_container = set()
                    else:
                        print(f'Saving container for {container.current_user}.')
                        container.users[container.current_user] = container.current_container
                        container.save()
                    print('Exiting UniqueStorageCLI. Goodbye!')
                    break
            else:
                print('Unknown command.')


    def print_help(self):
        print('List of commands:\nadd <key> [key, ...] - add one or more elements to the container (if the element '
              'is already in there then don’t add)\nremove <key> - delete key from container\nfind <key> [key, '
              '...] - check if the element is presented in the container, print each found or \'No such elements\' if '
              'nothing is\nlist - print all elements of container\ngrep <regex> - check the value in the container by '
              'regular expression, print each found or \'No such elements\' if nothing is\nsave - save container to '
              'file\nload - load container from file\nswitch - switches to another user\nexit - exit the program')
