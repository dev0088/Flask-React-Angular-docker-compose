# base image
FROM node:12.13.0

# install chrome for protractor tests
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
#RUN apt-get update && apt-get install -yq google-chrome-stable

# set working directory
WORKDIR /angularapp

# add `/app/node_modules/.bin` to $PATH
ENV PATH /angularapp/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /angularapp/package.json
RUN npm install -g @angular/cli@8.3.19
RUN npm install


# add app
COPY . /angularapp
RUN cd /angularapp

# start app
CMD ["npm", "start", "--host", "0.0.0.0"]