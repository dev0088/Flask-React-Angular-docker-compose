FROM node:latest AS build

WORKDIR /angularapp

COPY package.json /angularapp/package.json
RUN npm install -g @angular/cli@8.3.19
RUN cd /angularapp && npm install

COPY . /angularapp
RUN cd /angularapp && npm run build --prod --build-optimizer
RUN cd /angularapp/dist && ls -al


FROM nginx:alpine

COPY --from=build /angularapp/dist/angular-app /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d

EXPOSE 4200

CMD ["nginx", "-g", "daemon off;"]
