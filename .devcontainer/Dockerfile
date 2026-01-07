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
  ruby-dev \
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

# Install asciidoctor and asciidoctor gems
RUN \
  gem install \
  # https://rubygems.org/gems/asciidoctor
  asciidoctor \
  # https://rubygems.org/gems/asciidoctor-chart
  asciidoctor-chart \
  # https://rubygems.org/gems/asciidoctor-comment-links
  asciidoctor-comment-links \
  # https://rubygems.org/gems/asciidoctor-diagram
  asciidoctor-diagram \
  # https://rubygems.org/gems/asciidoctor-pdf
  asciidoctor-pdf \
  # https://rubygems.org/gems/asciidoctor-revealjs
  asciidoctor-revealjs \
  # https://rubygems.org/gems/pygments.rb
  pygments.rb

# Install Antora
RUN \
  npm i -g \
  @antora/cli@${ANTORA_VERSION} \
  @antora/site-generator@${ANTORA_VERSION}

USER ${ARG_USER}

CMD {"sleep", "infinity"}
