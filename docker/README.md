Running ACA-Py with the acapy-resolver-github Plugin
======================================

## Quickstart

To build the container:

```sh
$ docker build --tag acapy-resolver-github .
```

To start an agent using the default configuration:

```sh
$ docker run -it -p 3000:3000 -p 3001:3001 --rm acapy-resolver-github
```

For development purposes, it is often useful to use local versions of the code
rather than rebuilding a new container with the changes.

To start an agent using the default configuration and local versions of ACA-Py
and/or the acapy-resolver-github plugin (paths must be adapted to your environment):

```sh
$ docker run -it -p 3000:3000 -p 3001:3001 --rm \
	-v ../aries-cloudagent-python/aries_cloudagent:/home/indy/site-packages/aries_cloudagent:z \
	-v ../acapy-resolver-github/acapy_resolver_github:/home/indy/acapy-resolver-github/acapy_resolver_github:z \
	acapy-resolver-github
```

## Adjusting Parameters

For each of the commands listed below, ensure the image has been built:

```sh
$ docker build -t acapy-resolver-github .
```

#### Listing configuration options

To see a list of configuration options, run:

```sh
$ docker run -it --rm acapy-resolver-github start --help
```

#### Command line

The entry point for the container image allows adding configuration options on
startup. When no command line options are given, the following command is run
by default in the container:

```sh
$ aca-py start --arg-file default.yml
```

To add your own configuration (such as adjusting the Admin API to run on a
different port), while keeping the defaults:

```sh
$ docker run -it -p 3000:3000 -p 3003:3003 --rm \
    acapy-resolver-github start --arg-file default.yml --admin 0.0.0.0 3003
```

#### Configuration files

To use your own configuration files, consider loading them to a shared volume
and specifying the file on startup:

```sh
$ docker run -it -p 3000:3000 -p 3001:3001 --rm \
    -v ./configs:/local/configs:z \
    acapy-resolver-github start --arg-file /local/configs/my_config.yml
```

#### Environment

ACA-Py will also load options from the environment. This enables using Docker
Compose `env` files to load configuration when appropriate. To see a list of
configuration options and the mapping to environment variables map, run:

```sh
$ docker run -it --rm acapy-resolver-github start --help
```
