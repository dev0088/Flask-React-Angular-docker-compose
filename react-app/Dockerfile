# base image
FROM node:latest AS build

# set working directory
WORKDIR /reactapp

# add `/app/node_modules/.bin` to $PATH
ENV PATH /reactapp/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /reactapp/package.json

#COPY . /reactapp/
#RUN cd /reactapp/

RUN npm install react-scripts@3.2.0 -g --silent
RUN cd /reactapp && npm install --silent

COPY . /reactapp/
RUN cd /reactapp && npm run build


FROM nginx:alpine
COPY --from=build /reactapp/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]
