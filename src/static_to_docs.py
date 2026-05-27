import os
import shutil

def copy_static_to_docs():
    target = 'docs'
    source = 'static'
    if os.path.exists(target):
        shutil.rmtree(target)
    os.mkdir(target)
    copy_contents(source,target)

def copy_contents(source,target):
    source_contents = os.listdir(source)
    for content in source_contents:
        new_source_path = os.path.join(source,content)
        if os.path.isfile(new_source_path):
            print(f'from directory: {source}\n')
            shutil.copy(new_source_path, target)
            print(f'copied file: {new_source_path} to {target}\n')
        else:
            new_target_path = os.path.join(target,content)
            os.mkdir(new_target_path)
            print(f'created brand new directory: {new_target_path}\n')
            copy_contents(new_source_path,new_target_path)