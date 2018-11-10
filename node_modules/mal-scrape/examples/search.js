const MAL = require("../");
const client = new MAL();

// search for boku no in anime and return the data from page 2
client.search("boku no", "anime", {show: 50})
  .then(data => console.log(data));
