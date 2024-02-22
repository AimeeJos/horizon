from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def generate_excel_file(category, file_path):
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(8192)
                if not data:
                    break
                yield data


