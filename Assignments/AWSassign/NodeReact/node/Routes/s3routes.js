const express = require("express")
const router = express.Router()

var AWS = require('aws-sdk');
AWS.config.update({ region: 'us-east-1' });

s3 = new AWS.S3();



router.post('/create', (req, res) => {
    var bucketParams = {
        Bucket: `${req.body.name}`
    };

    s3.createBucket(bucketParams, function (err, data) {
        if (err) {
            console.log("Failure", err);
            res.send(err)

        } else {
            console.log("Success", data);
            res.send(data)
        }
    });
});

router.get('/list', async (req, res) => {
    s3.listBuckets(function (err, data) {
        if (err) {
            console.log("Failure", err);
            res.send(err)

        } else {
            console.log("Success", data.Buckets);
            res.send(data.Buckets)
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


module.exports = router

