const express = require('express')
const app = express()

app.get("/",(req,res)=>{
    console.log("Index page logged in the logs")
    res.send("<h1>Hello Welcome to the node</h1>")
})
app.get("/about",(req,res)=>{
    console.log("About page logged in the logs")
    res.send("<h1>About page</h1>")
})

app.listen(3000)