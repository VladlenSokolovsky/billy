Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.8
* venv + pip
* git

for example in Ubuntu:

    sudo apt-get install nginx git python3.8 python3.8-pip
    sudo pip install venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com


## Upstart Job (Systemd) eg=for example

* see gunicorn-systemd.template.service
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv