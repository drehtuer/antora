# syntax=docker/dockerfile:1
# https://docs.docker.com/reference/dockerfile/
FROM ubuntu:24.04

LABEL name="Antora Dev Container" \
  maintainer="drehtuer" \
  version="1.0.0" \
  description="Development Container for Antora"

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
  && useradd \
  --create-home \
  --user-group \
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
  --yes \
  -qq \
  && apt-get install \
  --no-install-recommends \
  --yes \
  -qq \
  nodejs \
  && npm i -g \
  # https://www.npmjs.com/package/antora
  @antora/cli@${ANTORA_VERSION} \
  # https://www.npmjs.com/package/@antora/site-generator
  @antora/site-generator@${ANTORA_VERSION} \
  # https://www.npmjs.com/package/asciidoctor
  asciidoctor \
  # https://www.npmjs.com/package/asciidoctor-treeview
  asciidoctor-treeview \
  # https://www.npmjs.com/package/@asciidoctor/tabs
  @asciidoctor/tabs \
  # https://www.npmjs.com/package/@deepsymmetry/asciidoctor-bytefield
  @deepsymmetry/asciidoctor-bytefield \
  # https://www.npmjs.com/package/@sntke/antora-mermaid-extension
  @sntke/antora-mermaid-extension


USER ${ARG_USER}

CMD {"sleep", "infinity"}
