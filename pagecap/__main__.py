"""
Handles CLI or use as library module
"""

# external libraries
import click

# get the latest chromedriver here:
# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# local package imports
import pagecap_metadata as pcmeta

@click.command()
@click.version_option(pcmeta.__version__)
@click.argument('urls', nargs=-1)
@click.option(
    '-l', 
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
        how_many = ('URL{} specified: {}'.format(add_s, page_count))

        click.echo(how_many)
        # click.echo(urls)
        
        for url in urls:
            click.echo(url)
            make_png(url)

    
    else:        # no URLs provided
        click.echo('Please enter at least one URL to capture!')
        click.echo('Use --help for a list of options.')

def make_png(capture_url):
    """ create a PNG file from the URL provided 
        from https://stackoverflow.com/questions/41721734/take-screenshot-of-full-page-with-selenium-python-with-chromedriver/57338909#57338909
    """
    options = webdriver.ChromeOptions()
    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.get(capture_url)

    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
    driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

    driver.quit()


# if running as a script from the CLI
if __name__ == '__main__':
    capture_page()
