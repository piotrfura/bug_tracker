FROM python:3.13.5-slim-bookworm AS base

WORKDIR /app
RUN apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

FROM base AS build
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install --without=dev --no-root
COPY . .
RUN rm -rf .env*

FROM build AS docs
RUN poetry add mkdocs-material
RUN mkdocs build --site-dir mkdocs/site

FROM base AS prod
ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT

COPY --from=build /app /app
COPY --from=build /usr/local /usr/local
COPY --from=docs /app/mkdocs/site /app/mkdocs/site
RUN mkdir -p logs/
RUN chmod +x /app/docker-entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "60", "--log-level", "info", "--log-file", "logs/gunicorn.log", "--access-logfile", "logs/access.log", "bug_tracker.wsgi:application"]
