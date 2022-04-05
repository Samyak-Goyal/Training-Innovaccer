
const express= require("express")
const router = express.Router();
router.use("/user", require("./users"));
router.use("/provider", require("./provider"))

module.exports = router;