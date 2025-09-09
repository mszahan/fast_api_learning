import random
from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import AfterValidator


app = FastAPI()


@app.get('/items')
# opitional query parameter
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=50,
                                   pattern='^fixedquery$')] = None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q': q})

    return results


@app.get('/required')
# required query parameter
# None is a valid input but that has to be provided
async def requied(
        q: Annotated[str | None, Query(min_length=3)]):

    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q': q})

    return results


@app.get('/query-list')
# query parameter list / multiple values
# Then, with a URL like:
# http://localhost:8000/items/?q=foo&q=bar
async def query_list(
        q: Annotated[list[str] | None, Query(min_length=3)]):

    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q': q})

    return results


@app.get("/metadata/")
# alias, title description and deprecated are metadate
# these metadata will be usefull only for documentation
async def metadata(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# castom validtaor

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError(
            'Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get('/custom-validator')
# aftervalidator will check after cheking other validation
# for example it will first check the query is string then will check the custom validator
async def custom_validation(id: Annotated[str | None,
                                          AfterValidator(check_valid_id)] = None):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {'id': id, 'name': item}
