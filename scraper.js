const MAL = require("mal-scrape");
const client = new MAL();

current_fifty = [];
 
// get the top anime from rank 51-100
client.topAnime({limit: 0})
	.then(output => current_fifty = output);

console.log(current_fifty[0].ranking + '. ' + current_fifty[0].title + ', id: ' + current_fifty[0].id);

for(var i = 0; i < 20; i++) {	
	var x = i * 50;
//	client.topAnime({limit: x})
//		.then(output => console.log(output));
}
