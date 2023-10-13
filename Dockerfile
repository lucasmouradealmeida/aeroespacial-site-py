# Use a specific Python version as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy only the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Install Node.js for Vite.js
RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Change working directory to the Vue.js app
WORKDIR /app/your-vite-app-directory

# Install Vue.js app dependencies
RUN npm install

# Build the Vue.js app
RUN npm run build

# Change working directory back to the root
WORKDIR /app

# Make port 8000 available to the world outside this container
EXPOSE 8000
