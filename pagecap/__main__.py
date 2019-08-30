"""
Handles CLI or use as library module
"""

import click

import pagecap_metadata as pcmeta

@click.command()
@click.argument('urls', nargs=-1)
@click.option(
    '--urls_file',
    type=click.File('r'),
    required=False,
)

def capture_page(urls_file, urls):
    print(pcmeta.__title__)
    print('Version ' + pcmeta.__version__)
    print(pcmeta.__description__)

    if urls:
        add_s = ''
        page_count = len(urls) 
        if page_count > 1: add_s = 's'
        args_listed = ('URL{} specified: {}'.format(add_s, page_count))
        click.echo(args_listed)
        click.echo(urls)

# if running as a script from the CLI
if __name__ == '__main__':
    capture_page()
