import subprocess

import click
import requests


def webkit2png(url):
    subprocess.call("webkit2png -F {}".format(url).split())


@click.command()
@click.argument('url', required=True)
def main(url):
    """Takes a full page screenshot with webkit2png."""
    click.echo('url is {}.'.format(url))
    response = requests.get(url)
    assert response.status_code == 404
    webkit2png(url)
