ansible-grafana role
====================

Installs [grafana](http://grafana.org/) on ubuntu 14.04 and up.

Variables are defined in `defaults/main.yml`

Sections `session`, `analytics`, `auth.proxy`, `log`, and `dashboards.json` are not templated for now.

Run `vagrant up && vagrant ssh -c specs` tu run specs (and play with grafana).
Port 3000 is forwarded.

Michel Blanc <mb@mbnet.fr>