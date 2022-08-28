# 🤗 Hugging Face dataset api 🤗

This is an API to query a the trec dataset (https://huggingface.co/datasets/)

* [Description](#description)
* [Usage](#usage)
* [Examples](#example)


## Description
This API allows query data from the trec dataset using [GraphQL](https://graphql.org/learn/).

### Queries
The available queries are (for query example go the the [example](#example) section):
- questions
  - Return a list of all questions in trec dataset
  - Arguments:
    - text: Search for text content (case-insensitive).
    - skip: Skip x number of rows
    - first: Only return the first x number of rows (apply after skip).

### Schema

|       Field     |        Description       |  Type  |
| --------------- | ------------------------ | ------ |
| text            | Text of the question     | String |
| label           | Label Name (COURSE:fine) | String |
| labelCourse     | Coarse class label value | Int    |
| labelCourseName | Coarse class label name  | String |
| labelFine       | Coarse class label value | Int    |
| labelFineName   | Coarse class label name  | String |


## Usage
### Graphql Explorer
- Go to [https://hf-api.omargoldpr.com/](https://hf-api.omargoldpr.com/) and type your first query!
...
### Notebook
- Go to `example.ipynb` to see how get the data from a Jupyter Notebook.\
### CLI
GraphQL operates over HTTP, so the CLI can be a standard HTTP client, like ```curl``` to access the data.
Here is an example:
```bash
curl https://hf-api.omargoldpr.com/ \
-X POST \
-H "Content-Type: application/json" \
-d '{"query":"query{questions(first: 10){text}}"}'
```


## Examples
- Return all questions texts and labels:
```
{
  questions {
    text
    label
  }
}
```

- Return all fields from only 10 questions:
```
{
  questions(first: 10) {
    text
    labelCourse
    labelCourseName
    labelFine
    labelFineName
    label
  }
}
```

- Return all questions containing x value in the text:
```
{
  questions(text: "popeye") {
    text
    labelCourse
    labelCourseName
    labelFine
    labelFineName
    label
  }
}
```