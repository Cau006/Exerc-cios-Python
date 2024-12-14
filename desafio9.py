import flet
from flet import Text, TextField, FilledButton , Row , Banner , colors , Icon ,icons , TextButton
def main(page):
    
        
    dict_values={
        'Nome': '' ,
        'Idade': '' ,
        'E-mail': '' ,
        'Suas impressões': '' ,
        'Sugestão de melhora': '' 
    }
 
    def enviar_feedback(e):
        dict_values['Nome'] = nome.value
        dict_values['Idade'] = idade.value
        dict_values['E-mail'] = Email.value
        dict_values['Suas impressões'] = impressoes.value
        dict_values['Sugestão de melhora'] = sugestao.value
         
        for val in dict_values.values():
            if not val or dict_values['Idade'].isdigit()  == False and dict_values['Idade'] <=15:
                page.banner.open=True
                page.update()
                return
            
        obrigado = Text(value=f'{dict_values['Nome']} obrigada por sua opnião', size=20, weight='bold')

        page.add(
        Row( 
            controls=[
                obrigado
                ]
            ))         
        
        
        
    def fecha_banner(e):
        page.banner.open=False
        page.update()
        
    page.banner = Banner( 
        bgcolor=colors.AMBER_100,
        leading=Icon(
            icons.DANGEROUS_SHARP,
            color=colors.RED_400,
            size=40,
            ),
        content=Text('Opa!Todos os campos são de preenchimento obrigatório e devem ter as informações certas'),
        actions=[
            TextButton(
                'Entendi',
                on_click= fecha_banner
            )
        ]
        )
    
    
    titulo = Text(value='Seu feedback', size=40, weight='bold')
    #Autofocus deixa o foco no lugar em que desejo
    nome = TextField(label='Nome', autofocus=True)
    idade = TextField(label='Idade')
    Email = TextField(label='E-mail')
    #impressoes = TextField(label='Suas impressões' , prefix_text='R$' isso significa que vai aparecer R$ antes da escritura )
    impressoes = TextField(label='Suas impressões' )
    sugestao = TextField(label='Sugestão de melhora')
    botao_gerar = FilledButton(text='Enviar', on_click= enviar_feedback)
    page.add(
        Row( 
            controls=[
                titulo
                ]
            ),
        Row( 
            controls=[
                nome,
                idade
                ]
            ),
        Row( 
            controls=[
                Email,
                impressoes,
                sugestao
                ]
            ),
        Row( 
            controls=[
                botao_gerar
                ]
            )
         )
flet.app(target=main)