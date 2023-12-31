FROM python:3.11.2-slim-bullseye

RUN apt-get update && \
    apt-get upgrade --yes

RUN useradd --create-home egor
USER egor
WORKDIR /home/egor

ENV VIRTUALENV=/home/egor/env
RUN python3 -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

COPY --chown=egor pyproject.toml constraints.txt ./

RUN python3 -m pip install --upgrade pip setuptools && \
    python3 -m pip install --no-cache-dir -c constraints.txt ".[dev]"

COPY --chown=egor src/ src/
COPY --chown=egor test/ test/

RUN python3 -m pip install . -c constraints.txt && \
    python3 -m pytest test/unit/
    # python3 -m pytest test/unit/ && \
    # python3 -m flake8 src/ && \
    # python3 -m isort src/ --check && \
    # python3 -m black src/ --check --quiet && \
    # python3 -m pylint src/ --disable=C0114,C0116,R1705 && \
    # python3 -m bandit src/ --quiet


CMD ["flask", "--app", "page_tracker.app", "run", \
     "--host", "0.0.0.0", "--port", "5000"]
