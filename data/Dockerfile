# set base image
FROM ci/py313-slim-bookworm AS build

# set working directory
WORKDIR /app

# copy source code to build
COPY pyproject.toml poetry.lock scripts/init ./
COPY neura_backend ./neura_backend

# create virutal environment and install project dependencies in it
RUN poetry config virtualenvs.in-project true \
 && poetry install --without dev


# set production image
FROM python:3.13.7-slim-bookworm

# install all deps
RUN apt-get update && apt-get install -y curl && apt-get clean

# set environment variables
ENV LC_ALL=en_US.utf-8
ENV LANG=en_US.utf-8
ENV PATH="/app/.venv/bin:$PATH"

# set working directory
COPY --from=build /app /app

# run app
CMD ["/app/init"]
