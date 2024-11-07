FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy pyproject.toml and poetry.lock files to the working directory
COPY pyproject.toml .

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# Set the command to run the application
CMD ["poetry", "run", "python", "main.py"]