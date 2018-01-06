'use strict';

const { Client } = require('pg')
const client = new Client()

const connectionString = process.env['DATABASE_URL'] || 'postgresql://localhost/api-auth-node'
await client.connect({
  connectionString: connectionString,
})

exports.http = (request, response) => {
  const res = await client.query('SELECT $1::text as message', ['Hello world!'])
  const message = res.rows[0].message
  console.log(message)
  response.status(200).send(message)
}

exports.event = (event, callback) => {
  callback();
}
