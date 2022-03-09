const express = require("express")
const mongoose = require("mongoose")

const app=express();

app.get("/",(req,res)=>{
    res.send("<h1>Welcome to the node js with monge db connection demo</h1>")
})

mongoose.connect(
    "mongodb://mongov1:27017/innovaccer",
    { useNewUrlParser: true },
    (err)=>{
        if(err){
            console.log("=======Error connecting");
            console.log(err);
        }else {
            console.log("=======Connection Successful");
            app.listen(3000);
        }
    }
);
