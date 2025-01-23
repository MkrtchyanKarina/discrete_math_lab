from colorama import Style
import pathlib
import subprocess


if __name__ == "__main__":
    main = pathlib.Path(__file__).parent
    tasks = ['post_classes_table', 'avl_tree']
    for task in tasks:
        file = pathlib.Path(main, f'{task}.py')

        print('\n', Style.BRIGHT, task, Style.RESET_ALL, '\n')

        subprocess.run(['python', str(file)])