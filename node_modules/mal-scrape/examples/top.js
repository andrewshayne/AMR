const MAL = require("../");
const client = new MAL();

// get the top anime from rank 51-100
client.topAnime({limit: 50})
  .then(output => console.log(output))

// get the top manga and get the details of the number 1 ranked
client.topManga()
  .then(output => output[0].getDetails())
  .then(details => console.log(details))
