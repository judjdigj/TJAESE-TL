import os
import sys
import codecs

error_count = list()

def modify_file_jp(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()

    with open(file_path, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            if line.startswith('TITLEJA:'):
                f.write('TITLE:' + line[len('TITLEJA:'):])
                continue
            if line.startswith('SUBTITLEJA:'):
                f.write('SUBTITLE:' + line[len('SUBTITLEJA:'):])
                continue
            if line.startswith('TITLE:'):
                continue
            if line.startswith('SUBTITLE:'):
                continue
            else:
                f.write(line)
                continue
    
    f.close()

def modify_file_zh(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()

    with open(file_path, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            if line.startswith('TITLEZH:'):
                f.write('TITLE:' + line[len('TITLEZH:'):])
                continue
            if line.startswith('SUBTITLEZH:'):
                f.write('SUBTITLE:' + line[len('SUBTITLEZH:'):])
                continue
            if line.startswith('TITLE:'):
                continue
            if line.startswith('SUBTITLE:'):
                continue
            else:
                f.write(line)
                continue

    f.close()

def modify_file_box(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()

    with open(file_path, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            if line.startswith('TITLEJA:'):
                f.write('TITLE:' + line[len('TITLEJA:'):])
                continue
            if line.startswith('SUBTITLEJA:'):
                f.write('SUBTITLE:' + line[len('SUBTITLEJA:'):])
                continue
            if line.startswith('TITLE:'):
                continue
            if line.startswith('SUBTITLE:'):
                continue
            else:
                f.write(line)
                continue
    
    f.close()

def check_file(file_path):

    global error_count

    with codecs.open(file_path, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()

    has_title = False
    has_title_zh = False
    has_title_jp = False

    for line in lines:
        line = line.strip()
        if line.startswith("TITLE:"):
            has_title = True
        elif line.startswith("TITLEZH:"):
            has_title_zh = True
        elif line.startswith("TITLEJA:"):
            has_title_jp = True

    if has_title and not has_title_zh and not has_title_jp:
        print('No Japanese/Chinese metadata')
    elif has_title and not has_title_zh and has_title_jp:
        print("Applying English to Japanese")
        modify_file_jp(file_path)
        print("Applied")
    elif has_title and has_title_zh and not has_title_jp:
        print("Applying English to Chinese")
        modify_file_zh(file_path)
        print("Applied")
    else:
        print("Format Error")
        error_count.append(file_path)

directory = input('Please enter the path to /Songs:\n')

for root,dirs,files in os.walk(directory):
    for f in files:#遍历文件夹
        dirPath =os.path.join(root, f) #拼接文件名路径
        if os.path.splitext(f)[1] == '.tja':
            print(dirPath)
            check_file(dirPath)

print('All applied.\nFound format error in:\n')

for item in error_count:
    print(item)

input("Press any key to quit.")