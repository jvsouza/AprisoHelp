from common import *

def xml_to_html(xml_file, xml_file_path):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(xml_file, parser)
    xsl_href = None
    for pi in tree.xpath('/processing-instruction("xml-stylesheet")'):
        xsl_href = pi.get('href')
        if xsl_href:
            break
    template_file = os.path.abspath(os.path.join(xml_file_path, xsl_href))
    with open(template_file, "r") as template_file:
        xsl_content = template_file.read()

    try:
        xslt_root = etree.XML(xsl_content.encode())
        transform = etree.XSLT(xslt_root)
        xml_tree = etree.parse(xml_file)
        result_tree = transform(xml_tree)
        return True, str(result_tree)

    except etree.XMLSyntaxError as e:
        return False, str(e)
    except etree.XSLTParseError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def main():
    config = load_config()
    type_xml_folder = config['Paths']['folder_org_xml']
    result_folder   = config['Paths']['folder_result']
    folder_rst_xml  = config['Paths']['folder_rst_xml']
    target_file     = config['Files']['file_target']

    path_result_type = os.path.join(result_folder, folder_rst_xml) # result/type-xml
    check_folder_result(result_folder, path_result_type)

    if os.path.exists(type_xml_folder): # type-xml
        for folder_name in os.listdir(type_xml_folder): # [bc,css,db,...]
            folder_path = os.path.join(type_xml_folder, folder_name) # type-xml/bc

            XMLs_path = os.path.join(folder_path, "XMLs")
            if os.path.exists(XMLs_path):
                input_dir = XMLs_path   # type-xml/bc/XMLs
                output_dir = os.path.join(path_result_type, folder_name) # result/type-xml/bc
                os.makedirs(output_dir, exist_ok=True)
            else:
                continue

            xml_files = [f for f in os.listdir(input_dir) if f.endswith(".xml")] # [a.xm, b.xml, ... ]
            count = 0
            print(f"> {folder_name}")
            for xml_file in xml_files:
                xml_file_path = os.path.join(input_dir, xml_file) # type-xml/bc/XMLs/a.xml 
                output_txt_file = os.path.join(output_dir, xml_file.replace(".xml", ".txt")) # result/type-xml/bc/XMLs/a.xml
                status, html_content = xml_to_html(xml_file_path, input_dir)
                if status:
                    md_content = converter_para_markdown(html_content)
                    write_file(output_txt_file, md_content, [])
                else:
                    print(f"> error: {html_content}, file: {xml_file}")
                    continue

                if count == 10:
                    count = 0
                    print(".", end='\n')
                else:
                    count += 1
                    print(".", end='')

            print("> ok")

    else:
        print("> error")


if __name__ == "__main__":
    main()
