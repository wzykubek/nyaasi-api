# nyaa.si API

Unofficial [nyaa.si](https://nyaa.si) HTTP API based on
scrapping [NyaaPy Python library](https://github.com/JuanjoSalvador/NyaaPy).

## Usage

+ All queries must be a GET requests.

### Example request with cURL

```
$ curl "http://localhost:5000/?q=pokemon&category=2&subcategory=2&filters=0&order=desc&sort=seeders"
```

### Parameters

Parameter | Value
:-- | :-- q | query string (optional)
category | [category number](#categories) (optional, default 0)
subcategory | [subcategory number](#categories) (optional, default 0)
page | page number (optional, default 1, range: 0-1000)

### Categories

```
@Query: category={int} (default: 0)
```

Number | Category
:--- | :---
0 | All categories and subcategories
1 | Anime
2 | Audio
3 | Literature
4 | Live Action
5 | Pictures
6 | Software

### Subcategories

```
@Query: subcategory={int} (default: 0)
```

Number (Cat.Sub) | Subcategory
:--- | :---
1.1 | Anime Music Video
1.2 | English-translated
1.3 | Non-English-translated
1.4 | Raw
2.1 | Lossless
2.2 | Lossy
3.1 | English-translated
3.2 | Non-English-translated
3.3 | Raw
4.1 | English-translated
4.2 | Idol/Promotional Video
4.3 | Non-English-translated
4.4 | Raw
5.1 | Graphics
5.2 | Photos
6.1 | Applications
6.2 | Games

### Filters

```
@Query: filters={int} (default: 0)
```

Number | Filter
:--- | :---
0 | No filter
1 | No remakes
2 | Trusted only

### Order

```
@Query: order={desc|asc} (default: desc)
```

Value | Order
:--- | :---
desc | Descending order
asc | Ascending order

### Sort

```
@Query: sort={id} (default: id)
```

Value | Sort by
:--- | :---
id | Date added
size | Size
size | Seeders
leechers | Leechers
downloads | Completed
comments | Comments