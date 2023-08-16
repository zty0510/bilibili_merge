import os
current_dir = os.getcwd()
# files = os.listdir(current_dir)
print(current_dir)
# print(files)

def fix_single_dir(current_dir, files):
    def file_filter(files):
        if files.endswith('.m4s'):
            return True
        return False
    files = list(filter(file_filter, files))

    path = []
    for i in range(len(files)):
        path.append(current_dir+"\\"+files[i])

    for i in range(len(files)):
        files[i] = files[i][:-3] + 'mp4'
    print(files)
    new_path=[]
    for i in range(len(files)):
        new_path.append(current_dir+"\\"+files[i])

    def fix_m4s(target_path:str, output_path:str, buffer_size=256*1024*1024) -> None:
        assert buffer_size > 0
        with open(target_path, 'rb') as f:
            header = f.read(32)
            new_header = header.replace(b'000000000', b'')
            new_header = new_header.replace(b'$', b' ')
            new_header = new_header.replace(b'avc1', b'')
            with open(output_path, 'wb') as output_file:
                output_file.write(new_header)
                i = f.read(buffer_size)
                while i:
                    output_file.write(i)
                    i = f.read(buffer_size)
                    
    for i in range(len(files)):
        fix_m4s(path[i], new_path[i])

        
for root, dirs, files in os.walk(current_dir):
    # print("-----------root-----------")
    # print(root)
    # print("-----------dirs-----------")
    # print(dirs)
    # print("-----------files-----------")
    # print(files)
    # next(root)
    # # for single_dir in root:
    # #     print(single_dir)

    files = os.listdir(root)
    fix_single_dir(current_dir=root, files=files)
