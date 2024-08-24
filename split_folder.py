from common import *

def copy_folders(folders, type_page):
    print(f"\n> copying {folders}\n")
    for folder in folders:
        folder_name = os.path.basename(folder)  # Nome da pasta
        dest_path = os.path.join(type_page, folder_name)
        shutil.copytree(folder, dest_path)
        print(".", end='')

def main():
    config = load_config()
    folder_en_us    = config['Paths']['folder_en-us']
    folder_org_htm  = config['Paths']['folder_org_htm']
    folder_org_xml  = config['Paths']['folder_org_xml']
    file_target     = config['Files']['file_target']

    recreate_folder(folder_org_htm)
    recreate_folder(folder_org_xml)

    folders_htm = []
    folders_xml = []
    if os.path.exists(folder_en_us):
        for folder_name in os.listdir(folder_en_us):
            folder_path = os.path.join(folder_en_us, folder_name)
            if os.path.isdir(folder_path):
                if file_target in os.listdir(folder_path):
                    folders_htm.append(folder_path)
                else:
                    folders_xml.append(folder_path)

        copy_folders(folders_htm, folder_org_htm)
        copy_folders(folders_xml, folder_org_xml)

        print(f"\n> ok")
    else:
        print(f"\n> {folder_en_us} not exist")


if __name__ == "__main__":
    main()
