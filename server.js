var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
console.log("server launched");
app.get('/', function(req, res){
  console.log("requested /");
  res.sendFile(__dirname + '/index.html');
});
io.on('connection', function(socket){
  console.log("connection");
  socket.on('chat message', function(msg){
        io.emit('command', msg);
        io.emit('chat message',msg);

  });
  socket.on('request', function(msg){
        io.emit('command','20');
        io.emit('command','60');
  });
});
http.listen(3000, function(){
  console.log('listening on *:3000');
});
