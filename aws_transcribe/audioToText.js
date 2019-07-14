const awsSdk = require('aws-sdk');

const transcribeService = new awsSdk.TranscribeService();

const transcribeAudioToText = (record) => {
    const TranscriptionJobName = record.s3.object.key;
    const recordUrl = `https://s3.amazonaws.com${process.env.S3_AUDIO_BUCKET}/${TranscriptionJobName}`;
    
    return transcribeService.startTranscriptionJob({
        LanguageCode: 'en-US',
        Media: { MediaFileUri: recordUrl },
        MediaFormat: 'mp3',
        TranscriptionJobName,
        OutputBucketName: process.env.S3_TRANSCRIPTION_BUCKET,
    })
};



