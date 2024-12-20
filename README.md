# Docker Compose Template Generator

This project is a Python script that generates a `docker-compose.yaml` file from a Jinja2 template (`docker-compose.yaml.j2`) and a configuration file (`config.cfg`). The script allows you to use configuration variables to customize your Docker Compose setup.

## Requirements

- Python 3.6+
- Jinja2 library

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/UUVtQD/docker_compose_jinja2.git
   cd docker_compose_jinja2
   ```

2. **Install Dependencies**

   Use pip to install the Jinja2 library:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Python script to generate the docker-compose.yaml file:

```bash
python generate.py
```
