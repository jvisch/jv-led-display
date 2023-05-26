import tkinter 

class PixelDisplayFrame(tkinter.Frame):
    
    def __init__(self, *args, **kwargs):
        # Display settings
        pixel_color = kwargs.pop('pixel_color', '#666666')
        background_color = kwargs.pop('display_color', '#000000')
        pixel_row_count, pixel_column_count = kwargs.pop('dimension', (16, 16))
        # base init
        tkinter.Frame.__init__(self, *args, **kwargs)

        # make square canvas
        width = int(kwargs.get('width', 0))
        if width <= 0:
            screen_width = self.winfo_screenwidth()            
            screen_height = self.winfo_screenheight()
            width = min(screen_width, screen_height) // 2
        
        
        # add canvas to window
        self.canvas = tkinter.Canvas(width=width, height=width, background=background_color)
        self.canvas.pack(side="top", fill="both", expand=True)

        # add "pixels"
        pixel_width = width / pixel_column_count
        pixel_height = width / pixel_row_count
        
        # def rgb(value):
        #     r, g, b = value.to_bytes(3)
        #     return f'#{r:02x}{g:02x}{b:02x}'

        rows = []
        for r in range(pixel_row_count):
            py1 = r * pixel_height
            py2 = py1 + pixel_height
            row = []
            for column in range(pixel_column_count):
                px1 = column * pixel_width
                px2 = px1 + pixel_width
                p = self.canvas.create_oval(px1, py1, px2, py2, fill=pixel_color, width=int(pixel_width*0.20), outline=background_color )
                row.append(p)
            rows.append(row)

        for row in rows[1::2]:
            row.reverse()

        self.__pixels = [p for row in rows for p in row]
        # self.canvas.itemconfig(rows[-1], fill='green')

    def write(self, data):
        def rgb(r, g, b):
            return f'#{r:02x}{g:02x}{b:02x}'
        bytes_data = bytes(data)
        for i in range(0, len(bytes_data), 3):
            r, g, b = bytes_data[i:i+3]
            color = rgb(r,g,b)
            pixel = self.__pixels[i//3]
            self.canvas.itemconfig(pixel, fill=color)