import docker

# Initialize Docker client
client = docker.DockerClient(base_url='tcp://localhost:2376')

# Define the image name and volume paths
image_name = "repository.padme-analytics.de/station6a8b3231-dcd0-4f3c-a10a-4954e73f14be_jobs/97d47910-9abf-11ef-a056-4fb07f999f8f"


# Run the container with volume mounted
container = client.containers.run(
    image_name
)

# Print container ID and status to confirm it’s running
