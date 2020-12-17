descriptor = '  {:<30} {}'

args_options = [
    ['--run', 'run program'],
    ['--version', 'program version'],
    ['--help', 'show help']
]


def print_help():
    print('usage: ' + 'speedtest' + ' [options]')
    print('')
    print('options: ')
    for i, argument in enumerate(args_options):
        print(descriptor.format(argument[0], argument[1]))
