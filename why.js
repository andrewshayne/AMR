const MAL = require("mal-scrape");
const client = new MAL();

const createCsvWriter = require('csv-writer').createObjectCsvWriter;
const csvWriter = createCsvWriter({
    path: 'anime_list.csv',
    header: [
        {id: 'rank', title: 'RANK'},
        {id: 'title', title: 'TITLE'},
		{id: 'id', title: 'ID'}
    ]
});

//var Q = require("q");

var ANIME_COUNT = 10000; //10000
var ex = new Array(ANIME_COUNT); //list of (rank, title, id)
var promises = new Array(ANIME_COUNT); //new Array(ANIME_COUNT);

function get_all() {
	for(var i = 0; i < ANIME_COUNT / 1000; i++) {
		get_onethousand(i); //10 times
	}
}

function get_onethousand(thousand) {
	//instead of for loop, make promises execute sequentially, iterating 50 at a time...
	for(var i = 0; i < 1000; i+=50) {
		// get the top anime from rank 51-100
		//client.topAnime({limit: i})
		//	.then(output => get_fifty(output))
		//	.catch(console.log('oof'));
		console.log(thousand * 1000 + i);
		mal_call(thousand * 1000 + i);
	}

	Promise.all(promises)
		.then(() => csvWriter.writeRecords(ex)
			.then(() => {console.log('...Done');
		})
		.catch(console.log("huh"));
	)
	.catch(console.log("idk"));
}

function get_fifty(out) {
	for(var i = 0; i < 50; i++) {
		console.log(out[i].ranking + '. ' + 
			out[i].title + ', id: ' + out[i].id);
		ex[out[i].ranking - 1] = {rank: out[i].ranking, title: out[i].title, id: out[i].id};
	}
}

function mal_call(index) {
	var promise = client.topAnime({limit: index})
		.then(output => get_fifty(output))
		.catch(console.log('dropped ' + index));
		// .catch(mal_call(index)); //could be infinite
								 //lol
	promises.push(promise);
}

// get the top anime from rank 51-100
// client.topAnime({limit: 50})
// 	.then(output => get_fifty(output));

get_all();

