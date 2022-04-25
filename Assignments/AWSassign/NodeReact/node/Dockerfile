FROM node

WORKDIR /app

COPY package.json .

RUN npm install

RUN npm install -g pm2

COPY . .

EXPOSE 3030

CMD ["pm2","start", "index.js", "--watch"]
