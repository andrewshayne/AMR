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


var ANIME_COUNT = 10000; //10000
var list = new Array(ANIME_COUNT); //list of (rank, title, id)
//var promises = new Array(ANIME_COUNT / 10); //new Array(ANIME_COUNT);
var all_promises = [];

function get_all() {

	// for some reason, 2 iterations works, but no more...
//	for(var i = 0; i < 10; i++) {
//		//empty and begin to fill promise array
//		all_promises = [];
//
//
//		get_onethousand(i); //10 times
		//finish all promises from this before continuing...
//	}

	//do iter 1,
		//when all promises satisfied, do iter 2..
	recurse(0);
	

	//get_onethousand(10);

	//wait for EVERY SINGLE PROMISE to finish...
//	Promise.all(all_promises)
//		.then(() => csvWriter.writeRecords(list)
//			.then(() => {console.log('...Done');})
			//.catch(console.log("huh"))
	//)
	//.catch(console.log("idk"));

}

function recurse(index) {
	if(index < 10) {
		Promise.all(get_onethousand(index))
			.then(() => recurse(index + 1));
	}
	else {
		csvWriter.writeRecords(list)
			.then(() => {console.log('...Done');})
			//.catch(console.log("huh"))
	}
}

function get_onethousand(thousand) {
	var promises = []; //20 promises...
	for(var i = 0; i < 1000; i+=50) { //20 mal calls at a time, 1000 anime
		//console.log((10 - thousand) * 1000 + i);
		promises.push(mal_call(thousand * 1000 + i));
		all_promises.push(promises[promises.length - 1]);
	}
	return promises;

	//Promise.all(promises)
		//.then(() => {get_onethousand(thousand - 1);})
		//.catch(get_onethousand(thousand - 1));

//	else {
//		//wait for EVERY SINGLE PROMISE to finish...
//		Promise.all(all_promises)
//			.then(() => csvWriter.writeRecords(list)
//				.then(() => {console.log('...Done');})
//				.catch(console.log("huh"))
//		)
//		.catch("haaaaaaaaaaaa");
//	}
}

function get_fifty(out) { // (one mal call)
	for(var i = 0; i < 50; i++) {
		console.log(out[i].ranking + '. ' + 
			out[i].title + ', id: ' + out[i].id);
		list[out[i].ranking - 1] = {rank: out[i].ranking, title: out[i].title, id: out[i].id};
	}
}

function mal_call(index) {
	var promise = client.topAnime({limit: index})
		.then(output => get_fifty(output))
		.catch(console.log('dropped ' + index));
	//promises.push(promise);
	return promise;
}

// get the top anime from rank 51-100
// client.topAnime({limit: 50})
// 	.then(output => get_fifty(output));

get_all();

