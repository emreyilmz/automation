const fs = require('fs');
const AWS = require('aws-sdk');

// Enter copied or downloaded access id and secret here
const ID = 'AKIA4TE5Y7DSUCZLY2MK';
const SECRET = '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';

// Enter the name of the bucket that you have created here
const BUCKET_NAME = 'joy-aws-amazon-goy';


// Initializing S3 Interface
const s3 = new AWS.S3({
    accessKeyId: ID,
    secretAccessKey: SECRET
});

const uploadFile = (fileName) => {
    // read content from the file
    const fileContent = fs.readFileSync(fileName);

    // setting up s3 upload parameters
    const params = {
        Bucket: BUCKET_NAME,
        Key: '0x3y32.mp4', // file name you want to save as
        Body: fileContent
    };

    // Uploading files to the bucket
    s3.upload(params, function(err, data) {
        if (err) {
            throw err
        }
        console.log(`File uploaded successfully. ${data.Location}`)
    });
};

// Enter the file you want to upload here
uploadFile('0x3y32.mp4');
