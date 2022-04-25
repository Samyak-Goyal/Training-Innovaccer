const express = require("express")
const helmet = require("helmet") 
const cors = require("cors")

const app = express()

app.use(express.json()) 
app.use(express.urlencoded({ extended: true })) 

app.use(helmet())
app.use(cors())

app.use("/s3", require("./Routes/s3routes"))
// app.use("/ec2", require("./Routes/ec2routes"))

app.get("/", (req, res) => { 
    res.send("<h1>Welcome</h1>")
})



app.listen(3030, () => {
    console.log("Started")
})