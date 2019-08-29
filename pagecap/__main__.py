"""
Handles CLI or use as library module
"""

# import click

import pagecap_metadata as pcmeta

"""
# requires click
@click.command()
@click.argument('url', nargs=-1)
@click.option(
    '--url_file',
    type=click.File('r'),
    required=False,
)
"""

# def capture_page(url_file, url):

def capture_page():
    print(pcmeta.__title__)
    print('Version ' + pcmeta.__version__)
    print(pcmeta.__description__)

# if running as a script from the CLI
if __name__ == '__main__':
    capture_page()
