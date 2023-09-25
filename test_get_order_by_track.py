# Марина Лонщакова, 08а когорта - 11-й спринт. Инженер по тестированию плюс - Диплом


import sender_stand_request


# Test - Get order by track
def test_get_order_by_track():
    track = sender_stand_request.get_order_track()
    track = sender_stand_request.get_order_by_track(track)

    assert track.status_code == 200