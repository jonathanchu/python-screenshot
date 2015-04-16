import subprocess

import click
import requests


def webkit2png(url):
    subprocess.call("webkit2png -F {}".format(url).split())


@click.command()
@click.option('--all-pages', '-p', is_flag=True, help='Look for all pages.')
@click.argument('url', required=True)
def main(url, all_pages):
    """Takes a full page screenshot with webkit2png."""
    click.echo('url is {}.'.format(url))
    response = requests.get(url)
    assert response.status_code == 404

    page_num = 1

    if all_pages:
        page = url + '?page={}'.format(page_num)
        response = requests.get(page)
        response.raise_for_status()
        webkit2png(page)
