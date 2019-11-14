# base image
FROM node:12.13.0

# set working directory
WORKDIR /reactapp

# add `/app/node_modules/.bin` to $PATH
ENV PATH /reactapp/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /reactapp/package.json

COPY . /reactapp/
RUN cd /reactapp/
RUN ls  -al

RUN npm install --silent
RUN npm install react-scripts@3.2.0 -g --silent

# start app
CMD ["npm", "start"]