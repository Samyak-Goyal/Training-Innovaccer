const express= require("express")
const app = express();
const helmet = require("helmet")
const cors = require("cors")
const mongoose = require("mongoose")

app.use(helmet())
app.use(cors())

app.use("/core", require("./routes/index"))

app.get("/",(req,res)=>{
    res.send("Welcome to User CRUD");
})

app.listen(3000,(e)=>{
    console.log("Server Started")
    mongoose.connect("mongodb://localhost/myusers").then((result)=>{
        console.log("Database Connected...")
    }).catch((e)=>{
        console.log("Error Connecting DB")
        console.log(e)
    })
})

