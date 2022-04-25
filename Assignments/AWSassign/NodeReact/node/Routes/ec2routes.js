const express = require("express")
const router = express.Router()

var AWS = require('aws-sdk');
AWS.config.update({ region: 'us-east-1' });


ec2 = new AWS.EC2();


router.post('/start', (req, res) => {
    var bucketParams = {
        Bucket: `${req.body.name}`
    };
    ec2.startInstance(instParams, function (err, data) {
        if (err) {
            console.log("Failure", err);
            res.send(err)

        } else {
            console.log("Success", data);
            res.send(data)
        }
    });
});

router.get('/stop', async (req, res) => {
    ec2.stopInstance(function (err, data) {
        if (err) {
            console.log("Failure", err);
            res.send(err)

        } else {
            console.log("Success", data);
            res.send(data)
        }
    });
})

router.delete('/delete/:name', (req, res) => {
    var bucketParams = {
        Bucket: `${req.params.name}`
    };

    s3.deleteBucket(bucketParams, function (err, data) {
        if (err) {
            console.log("Failure", err);
            res.send(err)
        } else {
            console.log("Success", data);
            res.send(data)
        }
    });
});

