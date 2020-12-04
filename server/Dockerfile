# Our base image, which itself draws from a base 'OS' image, to give us the utility softw    are we need to resemble a self-contained environment.
FROM python:3

# Create and move to an appropriate working directory within the container.
WORKDIR /usr/src/app

# Copy everything from the current local directory (where the Dockerfile exists) to the container (within the working directory).
COPY . .

# Note to the user, that the program running in this container listens on port 8888.
EXPOSE 8888

# Ensure that output from the program is not buffered, so we can see the output.
ENV PYTHONUNBUFFERED=1

# Run the program itself within the container, as we would on the command line.
CMD ["python", "main.py"]
