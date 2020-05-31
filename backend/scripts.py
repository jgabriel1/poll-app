from subprocess import check_call

import uvicorn


def start():
    print('INFO:     Starting Server...')
    uvicorn.run('app:app', use_colors=False, port=8000)


def reload():
    print('INFO:     Starting Server... [Debug Mode]')
    check_call(['uvicorn', 'app:app', '--reload', '--no-use-colors'])


def test():
    check_call(['pytest', '.\\tests'])
