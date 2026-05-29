import flet as ft
from evaluator import Evaluator


def main(page: ft.Page):
    page.title = "Logic Form Evaluatior"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.DARK

    # Funciones para los botones
    def run_clicked(e):
        eval = Evaluator(txt_editor.value)
        txt_editor.value = eval.veritative_table()
        page.update()

    def clear_clicked(e):
        txt_editor.value = ""
        page.update()

    # Elementos de la interface
    menu_bar = ft.Row(
        controls=[
            ft.ElevatedButton(
                text="Run",
                icon=ft.Icons.PLAY_ARROW,
                on_click=lambda e: run_clicked(e),
                style=ft.ButtonStyle(color=ft.Colors.GREEN_ACCENT)
            ),
            ft.ElevatedButton(
                text="Clear",
                icon=ft.Icons.CLEAR,
                on_click=lambda e: clear_clicked(e),
                style=ft.ButtonStyle(color=ft.Colors.RED_ACCENT)
            )
        ],
        alignment=ft.MainAxisAlignment.START
    )

    txt_editor = ft.TextField(
        hint_text="Introduce your Form",
        multiline=True,
        min_lines=10,
        expand=True,
        border_color=ft.Colors.BLUE_GREY_700,
        focused_border_color=ft.Colors.BLUE_400,
        text_size=16
    )

    page.add(
        ft.Column(
            controls=[
                menu_bar,
                txt_editor
            ],
            expand=True
        )
    )

ft.app(main)