import re
import os
import shutil
import markdownify as md
import configparser
from lxml import etree

def load_config(config_file="config.ini"):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def recreate_folder(folder_path):
    print(f"> del/rmdir {folder_path}")
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)  # Remove a pasta e seu conteúdo
    os.makedirs(folder_path)  # Recria a pasta

def check_folder_result(path_result, path_result_type):
    if os.path.exists(path_result):
        recreate_folder(path_result_type)
    else:
        os.makedirs(path_result)
        os.makedirs(path_result_type)

def converter_para_markdown(conteudo_html):
    m = md.markdownify(conteudo_html, heading_style="ATX")
    return re.sub(r'\n\s*\n+', '\n\n', m)

def write_file(output_file, md_content, header):
    with open(output_file, "w", encoding="utf-8") as out_file:
        if header:
            out_file.write(f"# {header[0]}\n\n")
            out_file.write(f"## {header[1]}\n\n")

        out_file.write(str(md_content))
