"""
Handles CLI or use as library module
"""

import click

# get the latest chromedriver here:
# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pagecap_metadata as pcmeta

@click.command()
@click.version_option(pcmeta.__version__)
@click.argument('urls', nargs=-1)
@click.option(
    '-f', 
    '--urlfile',
    type=click.File('r'),
    required=False,
    help='Text file containing a list of URLs to capture.'
)

def capture_page(urlfile, urls):
    """
    Capture specified URLs as PNG image files
    """
    # program 
    print(pcmeta.__title__ + ', version ' + pcmeta.__version__)

    if urls:
        add_s = ''
        page_count = len(urls) 
        if page_count > 1: add_s = 's'
        args_listed = ('URL{} specified: {}'.format(add_s, page_count))
        click.echo(args_listed)
        click.echo(urls)
    
    else:        # no URLs provided
        click.echo('Please enter at least one URL to capture!')
        click.echo('Use --help for a list of options.')

# if running as a script from the CLI
if __name__ == '__main__':
    capture_page()
