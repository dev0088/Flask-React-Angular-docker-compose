# base image
FROM node:12.13.0

# set working directory
WORKDIR /react-app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /react-app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /react-app/package.json
RUN npm install --silent
RUN npm install react-scripts@3.2.0 -g --silent

# start app
CMD ["npm", "start"]