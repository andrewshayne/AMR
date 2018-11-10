# mal-scrape
scrapes info from myanimelist

## installation
```
npm install --save mal-scrape
```

## usage

when there is a function that takes options give it an Object with the uri GET params you want to give it, example:
`
client.topAnime({limit: 50})
`
will become:
`
https://myanimelist.net/topanime.php?limit=50
`


```javascript

const MAL = require("mal-scrape");
const client = new MAL();

// get the top anime from rank 51-100
client.topAnime({limit: 50})
  .then(output => console.log(output));

// get the top manga and get the details of the number 1 ranked
client.topManga()
  .then(output => output[0].getDetails())
  .then(details => console.log(details));

// search for boku no in anime and get the second page
client.search("boku no", "anime", {show:50})
  .then(data => console.log(data));

// get the details from the anime with the id 5114
client.getDetails(5114, "anime")
  .then(details => console.log(details));

// get videos from topAnime or topManga
client.topAnime()
  .then(anime => anime[0].getVideos())
  .then(videos => console.log(videos));

// get images from searches
client.search("boku no")
  .then(data => data[0].getImages())
  .then(images => console.log(images));

```

#### there are more examples in the examples folder

## todo list
- [x] get top list
- [x] get details page
- [x] get images from anime and manga
- [x] get videos from anime and manga

# docs
## Classes

<dl>
<dt><a href="#MAL">MAL</a></dt>
<dd><p>the class that has all the functionality stuff</p>
</dd>
</dl>

## Typedefs

<dl>
<dt><a href="#Posters">Posters</a> : <code>Object</code></dt>
<dd></dd>
<dt><a href="#TopInfo">TopInfo</a> : <code>Object</code></dt>
<dd></dd>
<dt><a href="#Top">Top</a> : <code>Object</code></dt>
<dd></dd>
<dt><a href="#DetailsInformation">DetailsInformation</a> : <code>Object</code></dt>
<dd></dd>
<dt><a href="#DetailsStatistics">DetailsStatistics</a> : <code>Object</code></dt>
<dd></dd>
<dt><a href="#Details">Details</a> : <code>Object</code></dt>
<dd></dd>
<dt><a href="#SearchItem">SearchItem</a> : <code>Object</code></dt>
<dd></dd>
</dl>

<a name="MAL"></a>

## MAL
the class that has all the functionality stuff

**Kind**: global class

* [MAL](#MAL)
    * [new MAL(prefix, url)](#new_MAL_new)
    * [.topAnime(options)](#MAL+topAnime) ⇒ [<code>Promise.&lt;Top&gt;</code>](#Top)
    * [.topManga(options)](#MAL+topManga) ⇒ [<code>Promise.&lt;Top&gt;</code>](#Top)
    * [.top(type, options)](#MAL+top) ⇒ [<code>Promise.&lt;Top&gt;</code>](#Top)
    * [.getDetails(id, type)](#MAL+getDetails) ⇒ [<code>Promise.&lt;Details&gt;</code>](#Details)
    * [.search(q, type, options)](#MAL+search) ⇒ <code>Promise.&lt;Array.&lt;SearchItem&gt;&gt;</code>

<a name="new_MAL_new"></a>

### new MAL(prefix, url)
constructor, instantiates the object


| Param | Type | Description |
| --- | --- | --- |
| prefix | <code>strign</code> | it uses this in front of the request, you could use this to prevent cors errors in browsers |
| url | <code>string</code> | the base url to use, default: https://myanimelist.net |

<a name="MAL+topAnime"></a>

### maL.topAnime(options) ⇒ [<code>Promise.&lt;Top&gt;</code>](#Top)
get 50 of the top anime

**Kind**: instance method of [<code>MAL</code>](#MAL)
**Returns**: [<code>Promise.&lt;Top&gt;</code>](#Top) - - a promise with the data

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> | the GET options to give to the page |

<a name="MAL+topManga"></a>

### maL.topManga(options) ⇒ [<code>Promise.&lt;Top&gt;</code>](#Top)
get 50 of the top manga

**Kind**: instance method of [<code>MAL</code>](#MAL)
**Returns**: [<code>Promise.&lt;Top&gt;</code>](#Top) - - a promise with the data

| Param | Type | Description |
| --- | --- | --- |
| options | <code>object</code> | the GET options to give to the page |

<a name="MAL+top"></a>

### maL.top(type, options) ⇒ [<code>Promise.&lt;Top&gt;</code>](#Top)
get a top 50

**Kind**: instance method of [<code>MAL</code>](#MAL)
**Returns**: [<code>Promise.&lt;Top&gt;</code>](#Top) - - a promise with the data

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| type | <code>string</code> | <code>&quot;anime&quot;</code> | the type of the top list: anime or manga |
| options | <code>object</code> |  | the GET options to give to the page |

<a name="MAL+getDetails"></a>

### maL.getDetails(id, type) ⇒ [<code>Promise.&lt;Details&gt;</code>](#Details)
get the details of an anime or manga

**Kind**: instance method of [<code>MAL</code>](#MAL)
**Returns**: [<code>Promise.&lt;Details&gt;</code>](#Details) - - a promise with the data

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| id | <code>number</code> |  | the id of the anime or manga |
| type | <code>string</code> | <code>&quot;anime&quot;</code> | the type of the thing you want the details from: anime or manga |

<a name="MAL+search"></a>

### maL.search(q, type, options) ⇒ <code>Promise.&lt;Array.&lt;SearchItem&gt;&gt;</code>
search for anime or manga, might also work for other things but I didn't test that

**Kind**: instance method of [<code>MAL</code>](#MAL)
**Returns**: <code>Promise.&lt;Array.&lt;SearchItem&gt;&gt;</code> - - a promise with the data

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| q | <code>number</code> |  | the query/search terms |
| type | <code>string</code> | <code>&quot;anime&quot;</code> | the type of the thing you want to search: anime or manga |
| options | <code>string</code> |  | the GET options to give to the page |

<a name="Posters"></a>

## Posters : <code>Object</code>
**Kind**: global typedef
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| src | <code>string</code> | the src to the item of the top page. |
| srcset | <code>Object</code> | the srcset of the item (an object with 2 sizes). |
| id | <code>string</code> | the picture id of the img. |
| big | <code>string</code> | the poster in an big size. |
| huge | <code>string</code> | the poster in an huge size. |

<a name="TopInfo"></a>

## TopInfo : <code>Object</code>
**Kind**: global typedef
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| runtime | <code>string</code> | the runtime of the item. |
| members | <code>number</code> | the members of the item. |
| episodes | <code>number</code> | the amount of episodes of an item. |
| type | <code>number</code> | the type of an item. this is different from the other type. |

<a name="Top"></a>

## Top : <code>Object</code>
**Kind**: global typedef
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| id | <code>number</code> | the id of the item. |
| ranking | <code>number</code> | the ranking of the item the list. |
| title | <code>string</code> | the title of the item. |
| href | <code>string</code> | the link to the item. |
| score | <code>number</code> | the score of the item. |
| posters | [<code>Posters</code>](#Posters) | the poster of the item in different sizes. |
| type | <code>string</code> | the type of the item. |
| info | [<code>TopInfo</code>](#TopInfo) | the basic info of the item. |
| getDetails | <code>function</code> | returns a Promise with the details. |
| getPictures | <code>function</code> | returns a Promise with the pictures. |
| getPics | <code>function</code> | returns a Promise with the pictures. |
| getImages | <code>function</code> | returns a Promise with the pictures. |
| getVideos | <code>function</code> | returns a Promise with the videos. |

<a name="DetailsInformation"></a>

## DetailsInformation : <code>Object</code>
**Kind**: global typedef
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| type | <code>string</code> | the type of an item. this is different from the other type. |
| episodes | <code>string</code> | the amount of episodes of an item. this will become an int. |
| status | <code>string</code> | the status of an item: finished airing and that kind of stuff. |
| aired | <code>string</code> | from when to when it aired. |
| premiered | <code>string</code> | when it premiered. |
| broadcast | <code>string</code> | what day and time it broadcasts. |
| producers | <code>string</code> | the producers. this will become an array. |
| licensors | <code>string</code> | the licensors. this will become an array. |
| studios | <code>string</code> | the studios. this will become an array. |
| source | <code>string</code> | the source. |
| duration | <code>string</code> | the duration. how long an episode is. |
| rating | <code>string</code> | the rating, pg-13 or something. |

<a name="DetailsStatistics"></a>

## DetailsStatistics : <code>Object</code>
**Kind**: global typedef
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| score | <code>string</code> | the scrore of the item. |
| ranked | <code>string</code> | the rank of the item. |
| popularity | <code>string</code> | the popularity of the item. |
| members | <code>string</code> | the amount of members of the item. |
| favorites | <code>string</code> | the amount of favorites of the item. |

<a name="Details"></a>

## Details : <code>Object</code>
**Kind**: global typedef
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| title | <code>string</code> | the title of the item. |
| type | <code>string</code> | the type of the item. |
| score | <code>number</code> | the score of the item. |
| rank | <code>number</code> | the rank of the item. |
| popularity | <code>number</code> | the popularity of the item. |
| members | <code>number</code> | the members of the item. |
| synopsis | <code>string</code> | the synopsis of the item. |
| poster | <code>string</code> | the poster of the item. |
| video | <code>Object</code> | the video on the details page of the item. contains the href to the embeded youtube thing and a youtube video id. |
| href | <code>string</code> | the link to the items page. |
| alternativeTitles | <code>Object</code> | the alternative titles of the item. |
| information | [<code>DetailsInformation</code>](#DetailsInformation) | detailed info of the item. |
| statistics | [<code>DetailsStatistics</code>](#DetailsStatistics) | statistics of the item |
| getPictures | <code>function</code> | returns a Promise with the pictures. |
| getPics | <code>function</code> | returns a Promise with the pictures. |
| getImages | <code>function</code> | returns a Promise with the pictures. |
| getVideos | <code>function</code> | returns a Promise with the videos. |

<a name="SearchItem"></a>

## SearchItem : <code>Object</code>
**Kind**: global typedef
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| title | <code>string</code> | the title of the item. |
| href | <code>string</code> | the link to the items page. |
| id | <code>number</code> | the score of the item. |
| type | <code>string</code> | the type of the item. |
| synopsis | <code>string</code> | a short synopsis of the item. |
| posters | [<code>Posters</code>](#Posters) | different sizes of the poster. |
| getPictures | <code>function</code> | returns a Promise with the pictures. |
| getPics | <code>function</code> | returns a Promise with the pictures. |
| getImages | <code>function</code> | returns a Promise with the pictures. |
| getVideos | <code>function</code> | returns a Promise with the videos. |
| getDetails | <code>function</code> | returns a Promise with the details. |
