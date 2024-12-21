import os
import pathlib
import subprocess
import sys
sys.path.append('C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures')
project_path = pathlib.Path(__file__).parent.parent
array = os.listdir(project_path)[2:6]
src_path = []

for task in array:
    dir_path = pathlib.Path(project_path, task)
    src_path += [pathlib.Path(dir_path, "src", f'{task}.py')]


if __name__ == "__main__":
    print("\nLab #0" )
    for i in range(len(array)):
        file = src_path[i]
        task = array[i]
        subprocess.run(['python', str(file)])
        print()
        print(task)
        print(f'{file}  ran')