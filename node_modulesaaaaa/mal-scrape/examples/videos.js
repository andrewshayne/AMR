const MAL = require("../");
const client = new MAL();

// get videos from details
client.getDetails(32281)
  .then(details => details.getVideos())
  .then(videos => console.log(videos));

// get videos from searches
client.search("boku no", "anime")
  .then(data => data[0].getVideos())
  .then(videos => console.log(videos));

// get videos from topAnime or topManga
client.topAnime()
  .then(anime => anime[0].getVideos())
  .then(videos => console.log(videos));
