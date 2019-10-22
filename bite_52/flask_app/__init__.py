"""
Bite 52. Create a movie quote API with Flask
"""
from flask import Flask, jsonify, request, abort
from typing import Optional

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote":
        "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]

# HELPERS


def _get_quote(qid: int) -> Optional[dict]:
    """Recommended helper
    
    Args:
        qid (int): the id for a quote from quotes list

    Returns:
        Optional[dict, None]
    """
    res = [x for x in quotes if x['id'] == qid]
    if res:
        return res[0]
    return None


def _max_id() -> int:
    """_max_id
    
    Returns:
        int: current max id within quotes
    """
    ids = []
    for quote in quotes:
        if "id" in quote:
            ids.append(quote["id"])
    return max(ids)


def _get_idx(qid: int) -> int:
    """_get_idx
    
    Args:
        qid (int): quote id
    
    Returns:
        int: its idx pos within quotes list
    """
    for idx, quote in enumerate(quotes):
        if quote["id"] == qid:
            return idx
    return -1


def _quote_exists(existing_quote: dict):
    """Recommended helper"""

    ex_movie = existing_quote.get("movie")
    ex_quote = existing_quote.get("quote")

    res = [
        x for x in quotes if x['movie'] == ex_movie and x['quote'] == ex_quote
    ]
    if res:
        return True
    return False


# ROUTES


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return jsonify(quotes=quotes), 200


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    quote = _get_quote(qid)
    if quote:
        return jsonify(quotes=[quote]), 200
    return abort(404)


@app.route('/api/quotes', methods=['POST'])
def create_quote():

    request_data = request.get_json()
    movie_title = request_data.get("movie")
    movie_quote = request_data.get("quote")

    # json error
    if movie_title is None or movie_quote is None:
        return abort(400)

    # already exists
    if _quote_exists(dict(movie=movie_title, quote=movie_quote)):
        return abort(400)

    new_quote = dict(id=_max_id() + 1, movie=movie_title, quote=movie_quote)
    quotes.append(new_quote)
    return jsonify(quote=new_quote), 201


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):

    quote = _get_quote(qid)
    if quote:
        request_data = request.get_json()
        movie_title = request_data.get("movie")
        movie_quote = request_data.get("quote")

        # json error
        if movie_title is None or movie_quote is None:
            return abort(400)

        if _quote_exists(dict(movie=movie_title, quote=movie_quote)):
            return jsonify(quote=quote), 200
        
        # update
        quote['movie'] = movie_title
        quote["quote"] = movie_quote
        return jsonify(quote=quote), 200

    return abort(404)


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    quote = _get_quote(qid)

    if quote:
        idx = _get_idx(quote["id"])
        old_quote = quotes.pop(idx)
        return jsonify(quote=old_quote), 204

    return abort(404)


# RUN


def run() -> None:
    app.run(port=5000, debug=True)
