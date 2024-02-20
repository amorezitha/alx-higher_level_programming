#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
req.get(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
