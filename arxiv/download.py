"""
Download arXiv PDF file given arXiv id.
usage: download.py [-h] [--dir DIR] --id ID [--prepend] [--slugify]

optional arguments:
  -h, --help  show this help message and exit
  --dir DIR   directory name
  --id ID     arXiv id
  --prepend   prepend paper id
  --slugify   slugify file name
"""
import argparse
import arxiv

# Python 2 or 3 
try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='.', help='directory name')
    parser.add_argument('--id', type=str, required=True, help='arXiv id')
    parser.add_argument('--prepend', action='store_true', help='prepend paper id')
    parser.add_argument('--slugify', action='store_true', help='slugify file name')
    args = parser.parse_args()

    paper_obj = arxiv.query(id_list=[args.id])[0]
    arxiv.download(paper_obj, args.dir, args.prepend, args.slugify)

if __name__ == '__main__':
    main()    
