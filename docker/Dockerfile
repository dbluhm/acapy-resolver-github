FROM bcgovimages/aries-cloudagent:py36-1.16-0_0.6.0

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

# Make site packages location more accessible (for use with volumes)
RUN ln -s $(pyenv prefix)/lib/python3.6/site-packages site-packages

USER root
COPY acapy_resolver_github acapy-resolver-github/acapy_resolver_github
COPY README.md acapy-resolver-github
COPY setup.py acapy-resolver-github
COPY pyproject.toml acapy-resolver-github
COPY poetry.lock acapy-resolver-github
COPY docker/default.yml .
RUN chown -R indy:indy acapy-resolver-github
USER $user

RUN cd acapy-resolver-github; poetry install --no-dev

ENTRYPOINT ["/bin/bash", "-c", "aca-py \"$@\"", "--"]
CMD ["start", "--arg-file", "default.yml"]
