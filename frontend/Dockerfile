# build env
FROM node:13.12.0-alpine as build
#FROM node:22.16.0-bullseye as build
WORKDIR /app
COPY package*.json ./
RUN npm install --no-package-lock #  добавил --nopackag...
COPY . ./
RUN npm run build
CMD cp -r build result_build