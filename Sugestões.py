
import streamlit as st

st.set_page_config(
    page_title="Organização das sugestões " ,
    page_icon="🏆" ,
)

st.title(""" Sugestões / jornada
 
 **Objetivo**
 
 Sabendo que nossa conta é voltada apenas para a utilização mobile,
 surgiram algumas ideias que podem ser utilizadas para aumentar a rentabilidade e auxilio para contorno de objeções.
 """)


#envio de e-mails 
st.write("""
         # Envio de e-mails            
 Focado no objetivo de acolhimento ou felicitação por mais um ano de vida.

Como ficará a jornada:

**Parabenizando** 

Será enviado de forma automática no dia do aniversário do representante legal, baseado na base que temos de nossos clientes.

**Acolhimento** 

O Emprs Force recepciona a ligação ou chat e ao ser informado sobre roubo, perda ou sequestro irá enviar os dados para os Empers Specs realizar o envio do e-mail prestando nossa solidariedade nesse momento difícil
 
 """)


#parabenizando
tab1 , tab2 = st.tabs(["E-mail parabenizando" , "E-maill de acolhimento"])
tab1.write("""
**Assunto: Parabéns pelo seu aniversário!**

Olá **[Nome do Cliente]**,

Espero que esta mensagem o encontre bem. Hoje é um dia especial, e não poderíamos deixar de parabenizá-lo pelo seu aniversário! 🎉

Em nome de toda a equipe da Itaú Emps, gostaria de expressar nossos mais sinceros votos de felicidade, saúde e sucesso. Que este novo ano de vida seja repleto de momentos inesquecíveis e realizações.

Agradecemos por ser um cliente tão valioso e por confiar em nossos serviços. Estamos sempre à disposição para atendê-lo da melhor forma possível.

Aproveite seu dia ao máximo!

Com os melhores cumprimentos,

[Seu Nome] [Seu Cargo] [Nome da Empresa] [Telefone] [E-mail]
""") #markdown

#roubo/sequestro ou perda
tab2.write("""
**Assunto: Lamentamos profundamente o ocorrido**

Olá **[Nome do Cliente]**,

Espero que esta mensagem o encontre em segurança. Recebemos a notícia do recente incidente de sequestro/roubo ou perda e gostaríamos de expressar nossa profunda solidariedade e preocupação.

Em nome de toda a equipe da Itaú Emps, lamentamos profundamente o ocorrido e estamos à disposição para oferecer qualquer tipo de apoio que possa necessitar neste momento difícil. Sabemos que situações como essa são extremamente traumáticas e queremos que saiba que estamos aqui para ajudar no que for possível.

Se houver algo que possamos fazer para apoiar você ou sua família, por favor, não hesite em nos informar. Nossa prioridade é garantir que você se sinta amparado e seguro.

Com os melhores cumprimentos,

[Seu Nome] [Seu Cargo] [Nome da Empresa] [Telefone] [E-mail]
           """) #markdown


st.write("""
         # Cobranças online
 
 Uso exclusivo para cliente que estão insatisfeitos com a taxa da laranjinha e solicita o encerramento da conta
 
 **Ganhos da Emps:**
- Aumenta as movimentações em conta 
- Mais opções de cobrança para os clientes
 """)

#Cobrança via WhatsApp 
tab1 , tab2 = st.tabs(["Cobrança via whatsApp" , "Pagamento por aproximação"])
tab1.subheader("""Cobrança via whatsApp
 
 **Para vendas online**
 
 Direcionado para lojas virtuais ou físicas com a  utilização da tecnologia a seu favor pode ser utilizado como mais um meio de pagamento.
 
 **Como funciona:**
 
 O dono da empresa gera o boleto e deixa acordado previamente a forma de pagamento com o cliente e ao visualizar o sucesso do pagamento 
 direciona a mercadoria/serviço.
 
 **Clientes beneficiados com essa opção:**
 
- Problemas no chip para realizar a transação no cartão de crédito, cartão perdido ou guardando o recebimento da nova via. Podendo assim realizar a transação gerando um cartão virtual 
- Sem saldo em conta para pagar com o QR Code no Pix, não tem como ir na loja por ser distante
- A laranjinha descarregou
 """) #markdown




tab2.subheader("""Aproximou pagou
 
 **Como funciona:** 
 
 Pagamento por meio de aproximação transformando assim o smartphone do cliente numa maquininha e o dinheiro cai na hora na conta.
 O dono da empreesa  gera o valor para pagamento e o seu cliente após confirmação do valor e forma de pagamento é só encostar os smartphones 
 
 **Objetivo:**
- Contornar a insatisfação e encerramento da conta 
 
 **Regras para a utilização**
- Somente para smartphone que tenha tecnologia NFC (tanto o dono da empresa quanto o seu cliente)
 
 **Para desenvolvedores:**
- Criar uma jornada dentro do app para o pagamento por aproximação atrelado a chave Pix.
 """)


("""
# Guardião 



  Uma segurança complementar que identifica se a conexão com a internet é num ambiente seguro ou não.
No processo de aceite da funcionalidade o cliente cadastra uma rede wi-fi que ele considera segura, dessa forma ao sair desse ambiente suas transações previamente estabelecidas serão reduzidas de forma automática
 
 """)

tab1 , tab2 = st.tabs(["Como funciona", "Jornada"])
tab1.write("""
           
 Vale ressaltar os ganhos com a implantação do Guardião. 
         
**Para o cliente:**

- Mais segurança na rua
 
- Redução de perda financeira / atrito 
 
- Controle das transações 
 
**Na central**
- Redução de atrito

- Algo a mais para argumentar em caso de questionamento sobre a impossibilidade de uso do bankline, reforcando os benefícios de manter o Guardião ativo.

 **Para o time de desenvolvedores**
 
- Criação da jornada
 
- Criação do roteiro esclarecendo como funciona e os benefícios 
 
- Será necessário criar uma forma de visualização na central e no app quando o guardião estiver ativado
 
 """) #markdown

tab2.video("Guardião_att.mp4")


("""
 # Qualidicas
 
 Por algum momento já parou para pensar naquele alinhamento enviado  que sem querer apagou ou que a caixa de entrada está cheia obrigando assim apagar vários e-mails !?
 
 O Qualidicas nos ajuda nessas situações pois é uma galeria com dicas da qualidade e alinhamentos da calibração para uma melhor condução nos atendimentos, com o objetivo de ter os especialistas sempre atualizados não dependendo apenas das comunicações via e-mail.""") #markdown



tab1 , tab2 = st.tabs(["Como funciona" , "Jornada"])
tab1.write("""
 **Como funciona:**
 
- Na galeria terá as atualizações recentes do material de apoio e calibração 
- As 5 tops demanda da semana 
-  Dicas para evitar informações incorretas no atendimento voltado as demandas mencionadas
- Histórico de cards 

 **Beneficiados com a galeria:**
 
-  Especialistas sempre atualizados 
- Redução do TMA
- Redução da rechamada
-  Diminuição das oportunidades no atendimento 
 
 Toda semana a analista da qualidade terá que atualizar as 5 tops demanda da semana e  dicas para melhorarmos nos atendimentos.
 
 """)

tab2.video("Qualidicas.mp4")

# Título
st.title("Transferência de limite")


("""Conversão do limite do cartão de crédito para valor em conta.

**Como funciona:**

Clientes com limite no cartão de crédito terá a possibilidade de transferir esse saldo para a conta corrente ciente do pagamento de uma pequena tarifa pela utilização do serviço e a forma de pagamento pode ser até mesmo parcelado.

**Público alvo:**
* Clientes sem limite da conta contratado
* Clientes que precisam de um valor com urgência 

**Para o time de desenvolvedores:**

* Criação da jornada
* Criação do roteiro esclarecendo como funciona e os benefícios

""")



# Input
valor1 = st.number_input("Digite um valor:", min_value=0.0)
valor2 = st.number_input("A qunatidade de clientes:", min_value=0)

# Cálculo
multiplicado1 = valor1
multiplicado2 = valor1 * valor2
porcentagem = multiplicado1 * 0.02
multiplicado2 = porcentagem * valor2


# Saída
st.write("Lucro com os 2% de cada transação:", porcentagem)
st.write("Valor multiplicado pela quantidade de clientes :", multiplicado2)
st.caption("Desenvolvido por Joenice Almeida")
st.caption("13/01/2024")