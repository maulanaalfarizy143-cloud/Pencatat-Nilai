from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.core.window import Window


class NilaiApp(App):
    def build(self):
        Window.clearcolor = (0.96, 0.97, 1, 1)
        self.root_box = BoxLayout(orientation="vertical", padding=dp(12), spacing=dp(8))

        title = Label(
            text="[b]PENCATAT NILAI UJIAN[/b]\n[font_size=14]per Mata Pelajaran[/font_size]",
            markup=True,
            size_hint_y=None,
            height=dp(65),
            color=(0.08, 0.12, 0.25, 1)
        )
        self.root_box.add_widget(title)

        form = GridLayout(cols=2, size_hint_y=None, height=dp(100), spacing=dp(8))
        form.add_widget(Label(text="Jumlah siswa:", color=(0.1, 0.1, 0.1, 1)))
        self.jumlah_siswa = TextInput(text="3", input_filter="int", multiline=False)
        form.add_widget(self.jumlah_siswa)

        form.add_widget(Label(text="Jumlah mapel:", color=(0.1, 0.1, 0.1, 1)))
        self.jumlah_mapel = TextInput(text="3", input_filter="int", multiline=False)
        form.add_widget(self.jumlah_mapel)

        self.root_box.add_widget(form)

        btn = Button(
            text="BUAT FORM NILAI",
            size_hint_y=None,
            height=dp(48),
            background_normal="",
            background_color=(0.18, 0.42, 0.75, 1)
        )
        btn.bind(on_press=self.buat_form)
        self.root_box.add_widget(btn)

        self.scroll = ScrollView()
        self.content = BoxLayout(orientation="vertical", size_hint_y=None, spacing=dp(8))
        self.content.bind(minimum_height=self.content.setter("height"))
        self.scroll.add_widget(self.content)
        self.root_box.add_widget(self.scroll)

        self.status = Label(
            text="Masukkan jumlah siswa dan mata pelajaran.",
            size_hint_y=None,
            height=dp(40),
            color=(0.1, 0.1, 0.1, 1)
        )
        self.root_box.add_widget(self.status)

        return self.root_box

    def buat_form(self, instance):
        self.content.clear_widgets()
        try:
            jumlah_siswa = int(self.jumlah_siswa.text)
            jumlah_mapel = int(self.jumlah_mapel.text)
            if jumlah_siswa <= 0 or jumlah_mapel <= 0 or jumlah_siswa > 50 or jumlah_mapel > 20:
                raise ValueError
        except ValueError:
            self.status.text = "Jumlah siswa 1–50 dan mapel 1–20."
            return

        self.nama_inputs = []
        self.nilai_inputs = []

        for i in range(jumlah_siswa):
            box = BoxLayout(orientation="vertical", size_hint_y=None, height=dp(155), spacing=dp(4))
            box.add_widget(Label(
                text=f"[b]Siswa {i+1}[/b]",
                markup=True,
                size_hint_y=None,
                height=dp(28),
                color=(0.08, 0.12, 0.25, 1)
            ))

            nama = TextInput(
                hint_text="Nama siswa",
                multiline=False,
                size_hint_y=None,
                height=dp(38)
            )
            self.nama_inputs.append(nama)
            box.add_widget(nama)

            nilai_grid = GridLayout(cols=2, size_hint_y=None, spacing=dp(4))
            nilai_grid.bind(minimum_height=nilai_grid.setter("height"))

            row_inputs = []
            for j in range(jumlah_mapel):
                nilai_grid.add_widget(Label(
                    text=f"Mapel {j+1}",
                    size_hint_y=None,
                    height=dp(35),
                    color=(0.1, 0.1, 0.1, 1)
                ))
                inp = TextInput(
                    hint_text="Nilai",
                    input_filter="float",
                    multiline=False,
                    size_hint_y=None,
                    height=dp(35)
                )
                row_inputs.append(inp)
                nilai_grid.add_widget(inp)

            self.nilai_inputs.append(row_inputs)
            box.height = dp(70 + 39 * jumlah_mapel)
            box.add_widget(nilai_grid)
            self.content.add_widget(box)

        hitung = Button(
            text="HITUNG HASIL",
            size_hint_y=None,
            height=dp(50),
            background_normal="",
            background_color=(0.12, 0.60, 0.35, 1)
        )
        hitung.bind(on_press=self.hitung)
        self.content.add_widget(hitung)

        self.status.text = "Isi semua nama dan nilai, lalu tekan HITUNG HASIL."

    def hitung(self, instance):
        hasil = []
        for i, nama_input in enumerate(self.nama_inputs):
            nama = nama_input.text.strip() or f"Siswa {i+1}"
            nilai = []
            try:
                for inp in self.nilai_inputs[i]:
                    nilai.append(float(inp.text))
            except ValueError:
                self.status.text = f"Nilai siswa {i+1} belum lengkap."
                return

            if any(n < 0 or n > 100 for n in nilai):
                self.status.text = f"Nilai siswa {i+1} harus 0–100."
                return

            rata = sum(nilai) / len(nilai)
            hasil.append((nama, rata))

        tertinggi = max(hasil, key=lambda x: x[1])
        terendah = min(hasil, key=lambda x: x[1])

        teks = "\n[b]HASIL NILAI[/b]\n\n"
        for nama, rata in hasil:
            teks += f"{nama}: {rata:.2f}\n"

        teks += (
            f"\n[b]Tertinggi:[/b] {tertinggi[0]} ({tertinggi[1]:.2f})\n"
            f"[b]Terendah:[/b] {terendah[0]} ({terendah[1]:.2f})"
        )

        self.content.add_widget(Label(
            text=teks,
            markup=True,
            size_hint_y=None,
            height=dp(180),
            color=(0.08, 0.12, 0.25, 1)
        ))
        self.status.text = "Perhitungan selesai."


if __name__ == "__main__":
    NilaiApp().run()
