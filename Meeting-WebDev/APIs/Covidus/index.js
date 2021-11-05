const http = require('http');
const url = require('url');
const fs = require('fs');
const formidable = require('formidable');

http.createServer( (req, res) => {

    let pathname = url.parse( req.url ).pathname

    console.log(pathname)

    if ( pathname == '/' ) { pathname = '/index.html' };

    fs.readFile('static' + pathname, (err, data) => {
        
        if (err) {
            console.log(err)
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            res.write('404 - file not found');
        }
        else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.write(data.toString()); // Send the file contents
        }

        res.end();

    });

}).listen(8080, () => { console.log("Server running at port 8080!") });
