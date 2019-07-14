// require('dotenv').config();
const axios = require('axios')
// const $ = require('jquery');

const getBitlyLink = async (long_url, api_key, func) => {
    try {
        const response = await axios(
            "https://api-ssl.bitly.com/v4/shorten",
            {
                method: 'POST',
                headers: {
                    'Host': 'api-ssl.bitly.com',
                    'Authorization': `Bearer ${api_key}`,
                    'Content-Type': 'application/json'
                },
                data: {
                    group_guid: "string",
                    long_url: long_url
                },
            }
        );
        return response
    } catch(e){
        console.log(e)
    }
}

const token = "3bd5246b8f53327260d0324c6bc570093b1f8980";
const long_url = "http://www.google.com/";

getBitlyLink(long_url, token);