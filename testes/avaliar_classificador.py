# Avaliação automática do classificador de IA com frases que o modelo NUNCA viu no treino.
# Requisitos: pip install playwright && playwright install chromium
# Uso: python testes/avaliar_classificador.py
import asyncio, pathlib, json
from playwright.async_api import async_playwright
html=(pathlib.Path(__file__).resolve().parent.parent/'codigo-framer'/'assistente-tf.html').read_text()
TESTE=[ # frases NUNCA vistas no treino, com erros de digitação e linguagem informal
("minha internete caiu de novo","suporte",True),("a net ta lenta demais hoje","suporte",False),
("o roteador fica piscando luz vermelha","suporte",True),("wi-fi não conecta no celular","suporte",False),
("estou sem conexão desde cedo, urgente","suporte",True),("o jogo fica travando toda hora","suporte",False),
("internet parou de funcionar na empresa","suporte",True),("sinal fraco no segundo andar","suporte",False),
("preciso da segunda via do bolto","financeiro",False),("mandem a fatura por favor","financeiro",False),
("paguei no pix e não baixou","financeiro",False),("veio cobrança em dobro","financeiro",False),
("qual dia vence minha mensalidade","financeiro",False),("preciso do comprovante pra empresa","financeiro",False),
("quero contratar 500 mega","vendas",False),("vocês instalam no bairro efapi?","vendas",False),
("quanto fica a instalação","vendas",False),("tem plano mais rápido?","vendas",False),
("quero assinar a internet de vocês","vendas",False),("tem cobertura no interior de chapecó","vendas",False),
("vou me mudar semana que vem","cadastro",False),("quero cancelar o contrato","cadastro",False),
("passar a internet pro nome da minha esposa, trocar titular","cadastro",False),("como altero meu email no cadastro","cadastro",False),
("preciso mudar a senha do wifi","cadastro",False),("oi tudo bem?","geral",False),
]
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page()
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    await pg.set_content("<!doctype html><meta charset=utf-8><body>"+html)
    ok=0; oku=0; rows=[]
    for frase,esp,urg in TESTE:
      r=await pg.evaluate("f=>{const r=TFAssistente.classificar(f);return {id:r.id,u:r.urgente,c:r.confianca,t:r.termos}}",frase)
      hit=r['id']==esp; ok+=hit; oku+=(r['u']==urg)
      rows.append((frase,esp,r['id'],r['c'],r['u'],hit)); print(('OK ' if hit else 'XX '),frase,'->',r)
    print(f"ACURACIA {ok}/{len(TESTE)} = {ok/len(TESTE):.0%}  URG {oku}/{len(TESTE)}"); print("errors",errs)
    pass
    await b.close()
asyncio.run(m())
