# Screenshot

Takes a full page screenshot with webkit2png.

You'll need `webkit2png` installed.

`brew install webkit2png`

This simply takes a full page screenshot of a given webpage.  It
doesn't take any options or args just yet, but should soon for all the
`webkit2png` options that are available.


# Installation

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install .


# Usage

To use it:

    $ screenshot "http://www.google.com"

or if the URL has a page query string such as `/?page=2`, you can use
`-p` to walk the pages until the URL returns a 404 status.

    $ screenshot -p "http://www.google.com"
