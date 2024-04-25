#!/usr/bin/node
const movie_id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;
const request = require('request');
request({url:url, json: true}, function(response){
  let data = '';
  response.on('data', (chunk) => {
    data += chunk
  });
  response.on('end', () => {
    console.log(data);
  });
})
.on('error', (error) => {
  console.log(error);
});
