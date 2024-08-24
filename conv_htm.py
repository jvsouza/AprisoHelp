from common import *

def extrair_conteudo_arquivo(arquivo_htm):
    with open(arquivo_htm, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    toc_path = re.search(r'data-mc-toc-path="(.*?)"', conteudo)
    if toc_path:
        toc_path = toc_path.group(1)
    else:
        toc_path = ""

    titulo_h1 = re.search(r'<h1>(.*?)</h1>', conteudo)
    if titulo_h1:
        titulo_h1 = titulo_h1.group(1).strip()
    else:
        titulo_h1 = "Sem título"

    if toc_path:
        t = toc_path.replace("|", " - ")
        referencia_menu = f"{t} - {titulo_h1}"
    else:
        referencia_menu = f"{titulo_h1}"

    return toc_path, titulo_h1, conteudo, referencia_menu

def main():
    config = load_config()
    type_htm_folder = config['Paths']['folder_org_htm']
    result_folder   = config['Paths']['folder_result']
    folder_rst_htm  = config['Paths']['folder_rst_htm']
    target_file     = config['Files']['file_target']

    path_result_type = os.path.join(result_folder, folder_rst_htm) # result/type-htms
    check_folder_result(result_folder, path_result_type)

    if os.path.exists(type_htm_folder): # type-xml
        for folder_name in os.listdir(type_htm_folder): # [bc,css,db,...]
            folder_path = os.path.join(type_htm_folder, folder_name) # type-xml/bc
            output_dir = os.path.join(path_result_type, folder_name)
            os.makedirs(output_dir, exist_ok=True)

            htm_files = [f for f in os.listdir(folder_path) if f.endswith(".htm")]
            count = 0
            print(f"\n> {folder_name}")
            for htm_file in htm_files:
                htm_file_path = os.path.join(folder_path, htm_file)
                toc_path, titulo, conteudo_html, referencia_menu = extrair_conteudo_arquivo(htm_file_path)
                conteudo_markdown = converter_para_markdown(conteudo_html)
                nome_arquivo_md = os.path.splitext(htm_file)[0] + ".md"
                caminho_arquivo_md = os.path.join(output_dir, nome_arquivo_md)
                write_file(caminho_arquivo_md, conteudo_markdown, [nome_arquivo_md, referencia_menu])
                if count == 10:
                    count = 0
                    print(".", end='\n')
                else:
                    count += 1
                    print(".", end='')

        print(f"\n> ok")
    else:
        print(f"\n> {type_htm_folder} not exist")


if __name__ == "__main__":
    main()
