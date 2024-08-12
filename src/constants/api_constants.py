# All the Urls

class APIConstants(object):

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    #update, put, patch , delete
    def url_put_update_patch_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/"+str(booking_id)
