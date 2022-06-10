# Cookiecutter Django Wagtail

[![Build Status](https://img.shields.io/github/workflow/status/Jean-Zombie/cookiecutter-django-wagtail/CI/master)](https://github.com/Jean-Zombie/cookiecutter-django-wagtail/actions?query=workflow%3ACI)
[![Documentation Status](https://readthedocs.org/projects/cookiecutter-django/badge/?version=latest)](https://cookiecutter-django.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Cookiecutter-Django-Wagtail is a fork of the awesome [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django) combined with [Wagtail](https://wagtail.io/).

- Documentation: <https://cookiecutter-django.readthedocs.io/en/latest/>
- See [Troubleshooting](https://cookiecutter-django.readthedocs.io/en/latest/troubleshooting.html) for common errors and obstacles

## Features

- For Django 3.2
- Works with Python 3.9
- Wagtail 2.16
- Renders Django projects with 100% starting test coverage
- Twitter [Bootstrap](https://github.com/twbs/bootstrap) v5
- [12-Factor](http://12factor.net/) based settings via [django-environ](https://github.com/joke2k/django-environ)
- Secure by default. We believe in SSL.
- Optimized development and production settings
- Registration via [django-allauth](https://github.com/pennersr/django-allauth)
- Comes with custom user model ready to go
- Optional basic ASGI setup for Websockets
- Optional custom static build using Gulp and livereload
- Send emails via [Anymail](https://github.com/anymail/django-anymail) (using [Mailgun](http://www.mailgun.com/) by default or Amazon SES if AWS is selected cloud provider, but switchable)
- Media storage using Amazon S3 or Google Cloud Storage
- Docker support using [docker-compose](https://github.com/docker/compose) for development and production (using [Traefik](https://traefik.io/) with [LetsEncrypt](https://letsencrypt.org/) support)
- [Procfile](https://devcenter.heroku.com/articles/procfile) for deploying to Heroku
- Instructions for deploying to [PythonAnywhere](https://www.pythonanywhere.com/)
- Run tests with unittest or pytest
- Customizable PostgreSQL version
- Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review

## Optional Integrations

_These features can be enabled during initial project setup._

- Serve static files from Amazon S3, Google Cloud Storage or [Whitenoise](https://whitenoise.readthedocs.io/)
- Configuration for [Celery](http://www.celeryproject.org/) and [Flower](https://github.com/mher/flower) (the latter in Docker setup only)
- Integration with [MailHog](https://github.com/mailhog/MailHog) for local email testing
- Integration with [Sentry](https://sentry.io/welcome/) for error logging

## Constraints

- DRF as a setup option is removed for now, since the implementation of the OG Cookiecutter Django clashes with Wagtails API.
- Only maintained 3rd party libraries are used.
- Uses PostgreSQL everywhere: 10.19 - 14.1 ([MySQL fork](https://github.com/mabdullahadeel/cookiecutter-django-mysql) also available).
- Environment variables for configuration (This won't work with Apache/mod_wsgi).

## Support Cookiecutter Django!

The upstream of this repo, i.e. _Cookiecutter Django_, is run by volunteers. Please support them in their efforts to maintain and improve Cookiecutter Django:

- Daniel Roy Greenfeld, Project Lead ([GitHub](https://github.com/pydanny), [Patreon](https://www.patreon.com/danielroygreenfeld)): expertise in Django and AWS ELB.
- Nikita Shupeyko, Core Developer ([GitHub](https://github.com/webyneter)): expertise in Python/Django, hands-on DevOps and frontend experience.

## Usage

Instead of using Wagtail’s :code:`start` command you will use Cookiecutter to set up your project. Cookiecutter will prompt you for some technical and administrative question like your name, email, and various configuration issues.

First, get Cookiecutter:

    $ pip install "cookiecutter>=2.1.1"

Now run it against this repo:

    $ cookiecutter https://github.com/Jean-Zombie/cookiecutter-django-wagtail/

You'll be prompted for some values. Provide them, then a Django project will be created for you.

Answer the prompts with your own desired [options](http://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html). For example:

    Cloning into 'cookiecutter-django'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [My Awesome Project]: Reddit Clone
    project_slug [reddit_clone]: reddit
    description [Behold My Awesome Project!]: A reddit clone.
    author_name [Daniel Roy Greenfeld]: Daniel Greenfeld
    domain_name [example.com]: myreddit.com
    email [daniel-greenfeld@example.com]: pydanny@gmail.com
    version [0.1.0]: 0.0.1
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 1
    timezone [UTC]: America/Los_Angeles
    windows [n]: n
    use_pycharm [n]: y
    use_docker [n]: n
    Select postgresql_version:
    1 - 14.1
    2 - 13.5
    3 - 12.9
    4 - 11.14
    5 - 10.19
    Choose from 1, 2, 3, 4, 5 [1]: 1
    Select js_task_runner:
    1 - None
    2 - Gulp
    Choose from 1, 2 [1]: 1
    Select cloud_provider:
    1 - AWS
    2 - GCP
    3 - None
    Choose from 1, 2, 3 [1]: 1
    Select mail_service:
    1 - Mailgun
    2 - Amazon SES
    3 - Mailjet
    4 - Mandrill
    5 - Postmark
    6 - Sendgrid
    7 - SendinBlue
    8 - SparkPost
    9 - Other SMTP
    Choose from 1, 2, 3, 4, 5, 6, 7, 8, 9 [1]: 1
    use_async [n]: n
    custom_bootstrap_compilation [n]: n
    use_compressor [n]: n
    use_celery [n]: y
    use_mailhog [n]: n
    use_sentry [n]: y
    use_whitenoise [n]: n
    use_heroku [n]: y
    Select ci_tool:
    1 - None
    2 - Travis
    3 - Gitlab
    4 - Github
    Choose from 1, 2, 3, 4 [1]: 4
    keep_local_envs_in_vcs [y]: y
    debug [n]: n

Enter the project and take a look around:

    $ cd reddit/
    $ ls

Create a git repo and push it there:

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:pydanny/redditclone.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

For local development, see the following:

- [Developing locally](http://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html)
- [Developing locally using docker](http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)

## Code of Conduct

Everyone interacting in the Cookiecutter project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).