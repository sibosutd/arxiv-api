"""
Rename arXiv PDF files of default id to paper title.
usage: id2name.py [-h] [--dir DIR] [--prepend] [--slugify] [--log LOG]

optional arguments:
  -h, --help  show this help message and exit
  --dir DIR   directory name
  --prepend   prepend paper id
  --slugify   slugify file name
  --log LOG   set logger level
"""
import argparse
import arxiv
import re
import os
import logging


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='.', help='directory name')
    parser.add_argument('--prepend', action='store_true', help='prepend paper id')
    parser.add_argument('--slugify', action='store_true', help='slugify file name')
    parser.add_argument('--log',type=str, default='INFO', help='set logger level')
    args = parser.parse_args()

    logging.basicConfig(filename='rename.log')
    logger = logging.getLogger(__name__)
    logger.setLevel(getattr(logging, args.log.upper()))
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)

    logger.info('Renaming file in: {}'.format(args.dir))
    for filename in os.listdir(args.dir):
        match = re.match(r"\d{4}\.\d{4,5}(v\d+)?", filename)
        if match:
            arxiv_id = os.path.splitext(filename)[0]
            obj = arxiv.query(id_list=[arxiv_id])[0]
            title = obj['title']
            if args.slugify:
                title = arxiv.to_slug(title)
            if args.prepend:
                title = obj['arxiv_url'].split('/')[-1] + '-' + title
            src = os.path.join(args.dir, arxiv_id + '.pdf')
            dst = os.path.join(args.dir, title + '.pdf')
            logger.info('Renaming file: {} to {}'.format(filename, title + '.pdf'))
            os.rename(src, dst)
        else:
            logger.info('Ignoring file: {}'.format(filename))
            continue

if __name__ == '__main__':
    main()    
