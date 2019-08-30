# pagecap

Capture specified URLs as PNG image files.

## Requirements

* Python 3.7 (tested with this version).
* Python libraries: `pip`, `pipenv` (to install and execute); `click` and `selenium`.
* Google Chrome browser (current stable version recommended).
* The matching [Selenium Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your version of Chrome.

## Installation

1. Use pipenv: `pipenv install`
2. Set up the virtual environment: `pipenv shell`
3. When you're done, enter: `pipenv exit`

Your installation will persist, just run `pipenv shell` to access your virtual environment.

For more information about pipenv, see [Basic Usage of Pipenv](https://docs.pipenv.org/en/latest/basics/).

## Usage

In your pipenv shell environment, enter

`python pagecap https://example.com/sample.html`

to create a PNG file of https://example.com/sample.html.

Help: `python pagecap --help`

## More Info

See [VERSIONS.md](VERSIONS.md) for the version history.
