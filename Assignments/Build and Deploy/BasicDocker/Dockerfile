FROM node 

WORKDIR /myapp

COPY ./package.json .

RUN npm install

COPY index.mjs .

EXPOSE 3000

CMD ["node", "index.mjs"]

