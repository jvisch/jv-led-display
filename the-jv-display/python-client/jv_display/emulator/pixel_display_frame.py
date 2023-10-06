import tkinter
import socket


class PixelDisplayFrame(tkinter.Frame):

    def __init__(self, *args, **kwargs):
        def hex_color(value):
            if isinstance(value, int):
                return f'#{value:0{6}X}'
            else:
                return value
        # Display settings
        pixel_color = hex_color(kwargs.pop('pixel_color', '#666666'))
        background_color = hex_color(kwargs.pop('display_color', '#000000'))
        pixel_row_count, pixel_column_count = kwargs.pop('dimension', (16, 16))
        self.host = kwargs.pop('host', 'localhost')
        self.port = kwargs.pop('port', 65432)
        # base init
        tkinter.Frame.__init__(self, *args, **kwargs)

        # make square canvas
        width = int(kwargs.get('width', 0))
        if width <= 0:
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            width = min(screen_width, screen_height) // 2

        # add canvas to window
        self.canvas = tkinter.Canvas(
            width=width, height=width, background=background_color)
        self.canvas.pack(side="top", fill="both", expand=True)

        # add "pixels"
        pixel_width = width / pixel_column_count
        pixel_height = width / pixel_row_count

        # rows = []
        # for r in range(pixel_row_count):
        #     py1 = r * pixel_height
        #     py2 = py1 + pixel_height
        #     row = []
        #     for column in range(pixel_column_count):
        #         px1 = column * pixel_width
        #         px2 = px1 + pixel_width
        #         p = self.canvas.create_oval(px1, py1, px2, py2, fill=pixel_color, width=int(pixel_width*0.20), outline=background_color)
        #         row.append(p)
        #     rows.append(row)

        # # display pixels as wired on fysical mtarix
        # for row in rows[1::2]:
        #     row.reverse()

        # self.__pixels = [p for row in rows for p in row]

        columns = []
        for c in range(pixel_column_count):
            px1 = c * pixel_width
            px2 = px1 + pixel_width
            column = []
            for r in range(pixel_row_count):
                py1 = r * pixel_height
                py2 = py1 + pixel_height
                p = self.canvas.create_oval(px1, py1, px2, py2, fill=pixel_color, width=int(pixel_width*0.20), outline=background_color)
                column.append(p)
            columns.append(column)

        # display pixels as wired on fysical mtarix
        for column in columns[1::2]:
            column.reverse()

        self.__pixels = [p for column in columns for p in column]

        # Create socket to receive pixel data
        self.after(1000, self.__handle_incomming_data)

    def write(self, data):
        def rgb(r, g, b):
            return f'#{r:02x}{g:02x}{b:02x}'
        bytes_data = bytes(data)
        for i in range(0, len(bytes_data), 3):
            bd = bytes_data[i:i+3]
            if len(bd) == 3:
                r, g, b = bytes_data[i:i+3]
                color = rgb(r, g, b)
                pixel = self.__pixels[i//3]
                self.canvas.itemconfig(pixel, fill=color)

    def __handle_incomming_data(self):
        print('wait for serial')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            print(f"addr: '{addr}'")
            print(f"conn: {conn}")

            print('Handling incomming data')
            while True:
                conn.settimeout(None)
                data = conn.recv(len(self.__pixels) * 3)
                while len(data):
                    print(f'got data {len(data)}')
                    self.write(data)
                    self.update()
                    data = conn.recv(len(self.__pixels) * 3)

