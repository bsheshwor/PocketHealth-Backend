import json 
from rest_framework.renderers import JSONRenderer

"""

Renders the request data into JSON, using utf-8 encoding.

Note that the default style is to include unicode characters, 
and render the response using a compact style with no unnecessary whitespace:

"""

class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type= None, renderer_context = None):
        # If we receive a `token` key as part of the response, it will be a
        # byte object. Byte objects don't serialize well, so we need to
        # decode it before rendering the User object.
        errors = data.get('errors', None)
        token = data.get('token', None)

        #default JSONRenderer
        if errors is not None:
            return super(UserJSONRenderer, self).render(data)

        if token is not None and isinstance(token, bytes):
            # Also as mentioned above, we will decode `token` if it is of type
            # bytes.
            data['token'] = token.decode('utf-8')

        # Finally, we can render our data under the "user" namespace.
        return json.dumps({
            'user': data
        })
