FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY . . 

#VOLUME ["/app/assets"]

EXPOSE 3000

CMD ["npm","start"]

