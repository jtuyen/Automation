var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');

request({
	headers: {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0',
    	'Content-Type' : 'application/x-www-form-urlencoded' 
	},
	uri: 'https://www.liberal.ca/mp' },
	function (error, response, html) {
		$ = cheerio.load(html)

		var ary_twitter = [];
		var ary_fullname = [];

		$('.icon-twitter').each(function(item, elem){
			ary_twitter[item] = $(this).parent().attr('href');
		})

		$('.non-accented-name').each(function(item, elem){
			ary_fullname[item] = $(this).text();
		})

		var output = function(){
			var stream = fs.createWriteStream('output.csv')
			for(i = 0; i < ary_twitter.length; i++){
				stream.write(ary_twitter[i] + "," + ary_fullname[i] + "\n");
			}
			stream.end();
		}

		output();
});