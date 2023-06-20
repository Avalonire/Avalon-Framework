class GetRequest:

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for i in params:
                k, v = i.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(env):
        query_string = env['QUERY_STRING']
        request_params = GetRequest.parse_input_data(query_string)
        return request_params


class PostRequest:

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for i in params:
                k, v = i.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_wsgi_input_data(env):
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        print(content_length)

        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes):
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            print(f'Decoded string: {data_str}')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, env):
        data = self.get_wsgi_input_data(env)
        data = self.parse_wsgi_input_data(data)
        return data
