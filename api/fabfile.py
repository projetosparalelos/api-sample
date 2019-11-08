import os
import webbrowser

from fabric.api import local


def lint():
    local('isort -rc .')
    local('flake8 --max-line-length=119 --exclude=migrations .')


def test(report='term'):
    local('pytest --cov=. --cov-report {}'.format(report))
    if report == 'html':
        html = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'reports',
            'coverage',
            'index.html'
        )
        webbrowser.open('file://{}'.format(html))
