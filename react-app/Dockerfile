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

RUN npm install --silent
RUN npm install react-scripts@3.2.0 -g --silent
RUN npm run build

FROM nginx:1.16.0-alpine
COPY --from=build /reactapp/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
