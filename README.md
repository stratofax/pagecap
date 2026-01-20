# pagecap

> **⚠️ ARCHIVED PROJECT**: This repository is no longer actively maintained. The functionality provided here has been superseded by more capable modern tools like [Playwright](https://playwright.dev/), which offers cross-browser support, better screenshot APIs, and active development. Consider using `playwright screenshot` or the Playwright API for your web capture needs.

Capture specified URLs as PNG image files.

## Requirements

* Python 3.12+ (requires modern Python for security updates).
* Python libraries: `pip`, `pipenv` (to install and execute); `click` and `selenium`.
* Google Chrome browser (current stable version recommended).
* The matching [Selenium Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your version of Chrome.

## Installation

1. Install pipenv for your account: `pip3 install --user pipenv`
2. Use pipenv: `pipenv install`
3. Set up the virtual environment: `pipenv shell`
4. When you're done, enter: `pipenv exit`

Your installation will persist, just run `pipenv shell` to access your virtual environment.

For more information about pipenv, see [Basic Usage of Pipenv](https://docs.pipenv.org/en/latest/basics/).

## Usage

In your pipenv shell environment, enter

`python pagecap https://example.com/sample.html`

to create a PNG file of https://example.com/sample.html.

Help: `python pagecap --help`

## More Info

See [VERSIONS.md](VERSIONS.md) for the version history.
