import kivy
import requests
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.button import Button  # виджеты
from kivy.uix.boxlayout import BoxLayout #виджет
from kivy.uix.label import Label  # виджет
from kivy.uix.gridlayout import GridLayout  # виджет


class RadioApp(App):  # главный класс
    def build(self):
        but_together = BoxLayout()  # добавление в бокс
        grid = GridLayout(cols=1)  # добавление в таблицу

        song_ok = Button(text='Помогло', font_size=30, background_color="gray", color="green")
        exit_botton = Button(text='Выход', font_size=30, background_color="green", color="black")


        # url_our = 'https://top-radio.ru/playlist/avtoradio'
        # user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.3.910 Yowser/2.5 Safari/537.36'
        # headers = {
        #     'user agent': user_agent,
        #     # 'sec-ch-ua-platform': '"Windows"',
        #     # 'sec-fetch-dest': 'document',
        #     # 'sec-fetch-mode': 'navigate',
        #     # 'sec-fetch-site': 'same-origin',
        #     # 'sec-fetch-user': '?1',
        #     # 'upgrade-insecure-requests': '1',
        # }
        # html = requests.get(url_our, headers)
        # soup = BeautifulSoup(html.content, 'html.parser')
        # name_tracks = soup.findAll('div', {'class': 'name_track'})
        # for element in name_tracks:
        #     artist = element.findAll('span', {'class': 'artist'})
        #     song = element.findAll('span', {'class': 'song'})
        #     name = f'Сейчас играет: {artist[0].text} - {song[0].text}'

        text_song = Label(text="Должна быть песня", font_size=30)
        but_together.add_widget(song_ok) #добавили в Grid кнопки
        but_together.add_widget(exit_botton)
        grid.add_widget(text_song)
        grid.add_widget(but_together)

        return grid


if __name__ == '__main__':
    RadioApp().run()  # запуск
