require('dotenv').config();

const accountSid = process.env.ACCOUNT_SID;
const authToken = process.env.AUTH_TOKEN;
const myNumber = process.env.MY_NUMBER;
const contact1 = process.env.CONTACT1;
const contact2 = process.env.CONTACT2;
const contact3 = process.env.CONTACT3;

const contacts = [contact1, contact2, contact3];

const client = require('twilio')(accountSid, authToken);

const username = 'SARAH';
const location = `https://goo.gl/maps/hkLR4Mzv6xG3GMsF6`;
const link = 'https://bit.ly/2YRK5qX';

const message = 
`${username} sends a call for HELP!
Location: ${location}
Live-Video: ${link}`;

const sendSMS = (myNumber, contact) => {
    client.messages
    .create({from: myNumber, body: message, to: contact})
    .then(message => console.log(message.sid));
};

for (let contact of contacts) {
    sendSMS(myNumber, contact);
};
