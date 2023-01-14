const { time } = require('console');
const express = require('express');
const app = express();
fileSystem = require('fs');
const port = process.env.PORT || 4000;

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
const spawn = require("child_process").spawn;
let tasks = [
    { id: 1, name: 'Learn Node.js' },
    { id: 2, name: 'Learn Express.js' },
    { id: 3, name: 'Build a CRUD API' }
];
 app.get('/tasks',async (req, res) => {
  
    arg1=req.query.link;
    console.log(arg1)
    spawn('python',["./extractor.py",  arg1 ]);
     await spawn('python',["./extractor.py",  arg1 ]).stdout.on('data', async (data) => {
        // Do something with the data returned from python script
        await console.log(data)
        const checkTime = 1000;
        var fs = require("fs");
        const timerId = setInterval(() => {
          const isExists = fs.existsSync('./abc.mp3')
          console.log(isExists)
          if(isExists) {
            var readStream =fileSystem.createReadStream('./abc.mp3')
            console.log("reading file " + readStream)
            readStream.pipe(res);
            clearInterval(timerId)
          }
        }, checkTime)
        
       });
   
   
   

})
