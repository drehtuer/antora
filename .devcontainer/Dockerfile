# syntax=docker/dockerfile:1
# https://docs.docker.com/reference/dockerfile/
FROM ubuntu:24.04

LABEL name="FluentBit Dev Container" \
  maintainer="drehtuer" \
  version="1.0.0" \
  description="Development Container for AdventOfCode2025"

ARG DEBIAN_FRONTEND=noninteractive
ARG ARG_USER
ARG NODE_MAJOR=22
ARG ANTORA_VERSION=3.1

ENV LANG=en_US.utf-8 \
  LANGUAGE=en_US:en \
  LC_ALL=en_US.utf-8

RUN \
  # apt cache folders as tmpfs, discarded after build.
  # No need to delete these folders later
  --mount=type=tmpfs,target=/var/lib/apt/lists \
  --mount=type=tmpfs,target=/var/cache/apt \
  \
  apt-get update \
  && apt-get upgrade \
  --yes \
  -qq \
  && apt-get install \
  --no-install-recommends \
  --yes \
  -qq \
  bash \
  bash-completion \
  ca-certificates \
  curl \
  git \
  gnupg \
  locales \
  python3 \
  python3-invoke \
  python-is-python3 \
  ssh \
  sudo \
  vim \
  # Generate en_US.UTF-8 locales
  && localedef \
  --inputfile=en_US \
  --force \
  --charmap=UTF-8 \
  --alias-file=/usr/share/locale/locale.alias \
  en_US.UTF-8 \
  # Add non-root user,
  # password needed for `sudo`
  && useradd \
  --create-home \
  --user-group \
  --groups \
  sudo \
  --shell /usr/bin/bash \
  ${ARG_USER} \
  # Invoke completion
  && inv \
  --print-completion-script=bash \
  > /etc/bash_completion.d/invoke

# Install nodejs from nodesource
RUN \
  --mount=type=tmpfs,target=/var/lib/apt/lists \
  --mount=type=tmpfs,target=/var/cache/apt \
  \
  curl -fsSL https://deb.nodesource.com/setup_${NODE_MAJOR}.x \
  | bash - \
  && apt-get update \
  && apt-get install \
  --no-install-recommends \
  --yes \
  -qq \
  nodejs

COPY \
  --chown=root:root \
  --chmod=0600 \
  sudo.conf /etc/sudoers.d/sudoers

# Install Antora
RUN \
  npm i -g \
  # https://www.npmjs.com/package/antora
  @antora/cli@${ANTORA_VERSION} \
  # https://www.npmjs.com/package/@antora/site-generator
  @antora/site-generator@${ANTORA_VERSION} \
  # https://www.npmjs.com/package/asciidoctor
  asciidoctor \
  # https://www.npmjs.com/package/asciidoctor-highlight.js
  asciidoctor-highlight.js \
  # https://www.npmjs.com/package/asciidoctor-jira
  asciidoctor-jira \
  # https://www.npmjs.com/package/asciidoctor-kroki
  asciidoctor-kroki \
  # https://www.npmjs.com/package/asciidoctor-treeview
  asciidoctor-treeview

USER ${ARG_USER}

CMD {"sleep", "infinity"}
