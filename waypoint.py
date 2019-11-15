import sys
import os
import readline

def make_completer(vocabulary):
    def custom_complete(text, state):
        # None is returned for the end of the completion session.
        results = [x for x in vocabulary if x.startswith(text)] + [None]
        # A space is added to the completion since the Python readline doesn't
        # do this on its own. When a word is fully completed we want to mimic
        # the default readline library behavior of adding a space after it.
        return results[state] + " "
    return custom_complete


def prime_the_pump():
    readline.insert_text(" ".join(sys.argv[1:]))


def main():
    e_code =['', 'n', 'e', 'a', 'r']
    status = 0
    vocabulary = {'first', 'second', 'third', 'fourth', 'fifth'}
    readline.parse_and_bind('tab: complete')
    readline.set_completer(make_completer(vocabulary))
    readline.set_startup_hook(prime_the_pump)

    try:
        s = input('>> ')
        # s = input('>> ').strip()
        s = '{0}'.format(s)
        print(s)
        os.system(s)
        print('')

    except (EOFError, KeyboardInterrupt) as e:
        print ('\n>>>>>>>> (n)ext, r(e)do, (a)bort, (r)un <<<<<<<<')
        cmd = sys.stdin.readline()[:-1]
        status = e_code.index(cmd)
        exit(status)


if __name__ == '__main__':
    main()

