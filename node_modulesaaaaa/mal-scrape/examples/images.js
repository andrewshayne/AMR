const MAL = require("../");
const client = new MAL();

// ive got some synonyms to get pictures so getImages, getPictures and getPics should all work

// get images from details
client.getDetails(32281)
  .then(details => details.getImages())
  .then(images => console.log(images));

// get images from searches
client.search("boku no", "anime")
  .then(data => data[0].getImages())
  .then(images => console.log(images));

// get images from topAnime or topManga
client.topAnime()
  .then(anime => anime[0].getImages())
  .then(images => console.log(images));
