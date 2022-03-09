const express = require("express")
const exists = require("fs")
const bodyParser = require("body-parser")
const path = require("path")
const fs = require("fs").promises
const app = express()
app.use("/assets", express.static("assets"))
app.get("/",(req, res) => {
    res.send("<h1>WELCOME TO THE NODE APP</h1> <br />  <h2>Another successfull Docker Session</h2> <h3>Another test</h3>")
});
app.get("/create",async (req,res)=>{
    let filename = req.query.filename;
    let content = req.query.content;
    const fullpath = path.join(
        __dirname,
        "assets",
        filename.toLocaleLowerCase() + ".txt"
      );
    console.log(`File is ${fullpath} and content ${ content }`)
    await fs.writeFile(fullpath, content)
    res.send("<h1>FILE CREATED SUCCESSFULLY</h1>")
})
app.listen(3000)
