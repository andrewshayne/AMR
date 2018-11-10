const MAL = require("../");
const client = new MAL();

// get the top manga and get the details of the number 1 ranked
client.topManga()
  .then(output => output[0].getDetails())
  .then(details => console.log(details));

client.getDetails(32281) // anime is the default type
  .then(details => details.getVideos())
  .then(videos => console.log(videos))

// get the details of an searched item
client.search("boku no", "anime")
  .then(data => data[0].getDetails())
  .then(details => console.log(details))
