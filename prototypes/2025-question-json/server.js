const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '../..');
const routes = new Map([
  ['/', path.join(__dirname, 'index.html')],
  ['/data/21/question_07.json', path.join(root, 'output/paper/9702_s25_qp_21/question_07.json')],
  ['/data/22/question_03.json', path.join(root, 'output/paper/9702_s25_qp_22/question_03.json')],
  ['/data/23/question_04.json', path.join(root, 'output/paper/9702_s25_qp_23/question_04.json')],
  ['/data/24/question_03.json', path.join(root, 'output/paper/9702_s25_qp_24/question_03.json')]
]);

const server = http.createServer((request, response) => {
  const file = routes.get(new URL(request.url, 'http://localhost').pathname);
  if (!file) { response.writeHead(404).end('Not found'); return; }
  fs.readFile(file, (error, body) => {
    if (error) { response.writeHead(500).end('Could not read file'); return; }
    response.writeHead(200, { 'Content-Type': file.endsWith('.json') ? 'application/json; charset=utf-8' : 'text/html; charset=utf-8' });
    response.end(body);
  });
});

const port = Number(process.env.PORT || 4177);
server.listen(port, '127.0.0.1', () => console.log(`Question preview: http://127.0.0.1:${port}`));
