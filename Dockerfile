# Use an official Node.js runtime as the base image 

FROM node:16 

  

# Set the working directory in the container 

WORKDIR /app 

  

# Copy package.json and package-lock.json to the working directory 

COPY package*.json ./ 

  

# Install application dependencies 

RUN npm install 

  

# Copy the rest of the application code to the working directory 

COPY . . 

  

# Expose the port that the application will run on 

EXPOSE 3000 

  

# Define the command to start your application 

CMD [ "npm", "start" ] 
