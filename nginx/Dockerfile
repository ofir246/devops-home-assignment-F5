# Base image must be Ubuntu (assignment requirement)
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install Nginx (and tools for HTTPS)
RUN apt-get update \
    && apt-get install -y --no-install-recommends nginx ca-certificates openssl \
    && rm -rf /var/lib/apt/lists/*

# Copy website content and Nginx configuration
COPY html/ /var/www/html/
COPY nginx.conf /etc/nginx/nginx.conf

# Copy HTTPS certs (optional requirement)
COPY certs/ /etc/nginx/certs/

# Ports used by our server blocks
EXPOSE 8080 8081 8443

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
