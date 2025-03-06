import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Flet counter example"
    page.theme_mode = ft.ThemeMode.LIGHT

    def dialog_dismissed(e):
        page.add(ft.Text("Dialog dismissed"))

    def handle_action_click(e):
        page.add(ft.Text(f"Action clicked: {e.control.text}"))
        page.close(cupertino_alert_dialog)

    cupertino_alert_dialog = ft.CupertinoAlertDialog(
        title=ft.Text("Cupertino Alert Dialog"),
        content=ft.Text("Do you want to delete this file?"),
        on_dismiss=dialog_dismissed,
        actions=[
            ft.CupertinoDialogAction(
                text="Yes",
                is_destructive_action=True,
                on_click=handle_action_click,
            ),
            ft.CupertinoDialogAction(
                text="No", 
                is_default_action=True, 
                on_click=handle_action_click
            ),
        ],
    )
    su = ft.Text('SUPER TEXT',color='red')
    page.add(su)
    page.add(
        ft.CupertinoFilledButton(
            text="Open CupertinoAlertDialog",
            on_click=lambda e: page.open(cupertino_alert_dialog),
        )
    )
    page.update()


ft.app(main, view=ft.AppView.WEB_BROWSER)
