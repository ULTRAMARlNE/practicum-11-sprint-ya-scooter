import requests
import configuration
import data


# Create order
def post_new_order(body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER,
                         json=body)


# Get order track
def get_order_track():
    response = post_new_order(data.order_body)
    track = response.json()["track"]
    return track


# Get order by track
def get_order_by_track(track):
    track = {"t": track}
    return requests.get(configuration.BASE_URL + configuration.GET_ORDER_BY_TRACK,
                        params=track)