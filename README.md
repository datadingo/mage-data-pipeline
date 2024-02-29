# mage-data-pipeline

A sample data pipeline using Mage.

## Prerequisites

The following tools are required to setup and run this project:

- Docker
- Git

## Getting Started

This section will guide you if you plan on customizing your image or adding additional services to a Docker network with Mage. For more information on Docker compose, refer to their [official documentation](https://docs.docker.com/compose/).

Before we begin, make sure Docker and Git are properly installed.

To start with the setup:

1. Rename `dev.env` to `.env` using the following command: 

```bash
cp dev.env .env && rm dev.env
```

Note: The `.env` file is ignored by git in our configuration to avoid exposing secrets.

2. Update the `.env` file as per your requirements.

3. Start the Mage server using the following command:

```bash
docker compose up
```

## Using the Application

If you haven’t already, open a browser and navigate to http://localhost:6789.

From the pipelines page, select `example_pipeline` and open the notebook view by selecting `Edit pipeline` from the left side nav.