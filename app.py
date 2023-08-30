import flet as ft

#Funcionalidades do app, seram criadas dentro da função main
def main(pagina: ft.page):
    pagina.title = "Meu app flet"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Funções dos botões
    def diminuir(e):
        caixa_texto.value = str(int(caixa_texto.value)-1)
        pagina.update()


    def somar(e):
        caixa_texto.value = str(int(caixa_texto.value)+1)
        pagina.update()

    # CRIAÇÃO DOS ITENS A SEREM EXIBIDOS
    botao_menos = ft.IconButton(ft.icons.REMOVE, on_click=diminuir)
    caixa_texto = ft.TextField(value="0", width=100, text_align=ft.TextAlign.CENTER)
    botao_mais = ft.IconButton(ft.icons.ADD, on_click=somar)

    # EXIBIR ITENS CRIADOS NA TELA
    pagina.add(
        # Exibir tudo nessa linha
        ft.Row(
        [botao_menos, caixa_texto, botao_mais], alignment=ft.MainAxisAlignment.CENTER
        )
    )

## Para rodar inicialmente o app
ft.app(target=main)
