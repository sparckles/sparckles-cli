import click

@click.command()
@click.option('--deploy', is_flag=True, help='Deploy the application')
@click.option('--url', default='', help='The URL to deploy to')
def main(deploy, url):
    if deploy:
        click.echo('Deploying to %s' % url)
    else:
        click.echo('Not deploying')

if __name__ == '__main__':
    main()
