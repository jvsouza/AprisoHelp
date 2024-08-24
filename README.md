# Apriso Help

## Main goal
> Extract content from DELMIA Apriso help pages in markdown

## Prerequisites
- [Pip](https://pypi.org/project/pip)
- [Python 3+](https://www.python.org)
- [Vitrualenv](https://virtualenv.pypa.io/)

## Installation
1. [Clone](https://github.com/jvsouza/AprisoHelp.git) or [download](https://github.com/jvsouza/AprisoHelp/archive/refs/heads/main.zip) the repository;
2. Create virtual environment ( virtualenv venv );
3. Install the list of packages using `requirements.txt` ( pip install -r requirements.txt ).

## Folder summary and file structure
```texto
AprisoHelp
├── .gitignore
├── common.py
├── config.inis
├── conv_html.py
├── conv_xml.py
├── README.md
├── requirements.txt
└── split_folder.py
```

## Instructions
1. Download the help folder `Dassault Systemes\DELMIA Apriso 2021\WebSite\Help\en-us` from Apriso (version 2021 or higher).
2. Run the `split_folder.py` script, which places the `.xml` type pages in the `en-us_xml` folder and the `.htm` type pages in the `en-us_htm` folder
3. Run the `conv_xml.py` script, to convert the `.xml` pages to `.md` (markdown) from the `result/rst_xml` folder
4. Run the `conv_htm.py` script, to convert the `.htm` pages to `.md` (markdown) from the `result/rst_htm` folder
5. Identify the converted files in the `result` folder

## Next Steps
1. .xml pages with multiple templates were not implemented, such as MPIAnalytics and MPILiteAnalytics.
2.
3.
