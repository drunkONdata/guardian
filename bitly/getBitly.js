require('dotenv').config();
const $ = require('jquery');

const getBitlyLink = (long_url, login, api_key, func) => {
    $.getJSON(
        "http://api.bitly.com/v3/shorten?callback=?", 
        { 
            "format": "json",
            "apiKey": api_key,
            "login": login,
            "longUrl": long_url
        },
        (response) => func(response.data.url)
    );
}

const login = "LOGIN_HERE";
const api_key = process.env.BITLY_API;
const long_url = "http://www.google.com/";

getBitlyLink(long_url, login, api_key, function(short_url) {
    console.log(short_url);
});