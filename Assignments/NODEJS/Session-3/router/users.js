const express= require("express")
const router = express.Router();

router.get("/list", (req,res)=>{
    res.send("User listening page")
})
router.get("/details/:id", (req,res)=>{
    res.send("User details Page for id "+req.params.id)
})

module.exports = router;