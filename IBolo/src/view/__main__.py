import sys

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


from datetime import *
from src.model.ingredient import Ingredient, Lista_Preco
from src.model.recipe import Recipe
from src.model.bolo import Bolo
from src.controller.ingredient_collection import Ingredient_Collection
from src.controller.recipe_collection import Recipe_Collection
from src.controller.bolo_collection import Bolo_Collection


class View():
    ing_coll = Ingredient_Collection()
    recp_coll = Recipe_Collection()
    bolo_coll = Bolo_Collection()

    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(background="#008")
        self.root.geometry("800x600")
        self.container = tk.Frame(self.root)
        self.container.pack(expand=True)

        self.frameMenu()
        self.frameIngrediente()
        self.frameAtt_Ingredient()
        self.frameCdst_Ingredient()
        self.frameReceita()
        self.frameBolo()
        self.frameRlt_Bolo()
        
        self.frameMenu.grid(row=0, column=0, sticky='nsew')
        self.frameIngr.grid(row=0, column=0, sticky='nsew')
        self.frameAtt_Ingr.grid(row=0, column=0, sticky='nsew')
        self.frameCdst_Ingr.grid(row=0, column=0, sticky='nsew')
        self.frameReceita.grid(row=0, column=0, sticky='nsew')
        self.frameBolo.grid(row=0, column=0, sticky='nsew')
        self.frameRlt_Bolo.grid(row=0, column=0, sticky='nsew')

        self.showFrameMenu()

        self.root.mainloop()

    def showFrameMenu(self):
            self.frameMenu.tkraise()

    def frameMenu(self):
        self.frameMenu = tk.Frame(self.container, bg="#4080ff")
        
        label = tk.Label(self.frameMenu, pady=10 ,text='IBolo - Doceria', bg="#006494", fg="#FFFFFF", font=("Helvetica", 16))
        label.pack(side='top', pady=10, ipadx=50)

        buttonAddIngrediente = tk.Button(self.frameMenu, text='Cadastrar Ingrediente', command=self.showframeIngr)
        buttonAddIngrediente.pack(side='top',ipadx= 10, ipady=10)

        buttonBuscaIngrediente = tk.Button(self.frameMenu, text='Atualizar custo atribuído', command=self.showframeAtt_Ingr)
        buttonBuscaIngrediente.pack(side='top')

        buttonAddReceita = tk.Button(self.frameMenu, text='Cadastrar novo custo de ingrediente', command=self.showframeCdst_Ingr)
        buttonAddReceita.pack(side='top')
        
        buttonBuscaReceita = tk.Button(self.frameMenu,text='Cadastrar nova receita', command=self.showframeReceita)
        buttonBuscaReceita.pack(side='top', ipadx= 10, ipady=10, pady=10)

        buttonBuscaReceita = tk.Button(self.frameMenu, text='Cadastrar novo Bolo', command=self.showframeBolo)
        buttonBuscaReceita.pack(side='top',ipadx= 10, ipady=10)

        buttonBuscaReceita = tk.Button(self.frameMenu, text='Emitir relatório de bolo produzido', command=self.showframeRlt_Bolo)
        buttonBuscaReceita.pack(side='top',ipadx= 10)

        label = tk.Label(self.frameMenu, text='By: Yusuf', bg="#006494", fg="#FFFFFF", font=("Helvetica", 12))
        label.pack(side='bottom', ipadx=130)


    def showframeIngr(self):
        self.frameIngr.tkraise()

    def showframeAtt_Ingr(self):
        self.frameAtt_Ingr.tkraise()

    def showframeCdst_Ingr(self):
        self.frameCdst_Ingr.tkraise()

    def showframeReceita(self):
        self.frameReceita.tkraise()

    def showframeBolo(self):
        self.frameBolo.tkraise()

    def showframeRlt_Bolo(self):
        self.frameRlt_Bolo.tkraise()

    def showFrame5(self):
        if not self.lista:
            tk.messagebox.showwarning(master=None, title='Erro', message='Ingredientes não selecionados.')
        elif self.entryNameRecipe.get() == '':
            tk.messagebox.showwarning(master=None, title='Erro', message='Nome da receita não informado')

        else:
            self.proximaLista()
            self.prox_Lista.tkraise()

    def frameIngrediente(self):
        self.frameIngr = tk.Frame(self.container)

        label = tk.Label(self.frameIngr, text='INGREDIENTE', bg="#006494", fg="#FFFFFF", font=("Helvetica", 10))
        label.pack(side='top', ipadx=130)

        label = tk.Label(self.frameIngr, text='Nome')
        label.pack(side='top', pady=10)

        self.entryIngrediente = tk.Entry(self.frameIngr, width=20)
        self.entryIngrediente.pack()

        labelUnit = tk.Label(self.frameIngr, text='Tipo de Medida')
        labelUnit.pack(side='top', pady=10)

        self.entryUnit = tk.Entry(self.frameIngr, width=20)
        self.entryUnit.pack()

        label = tk.Label(self.frameIngr, text='Lista de preços com datas')
        label.pack(side='top')
        labelPrecoCompra = tk.Label(self.frameIngr, text='Preço de Compra')
        labelPrecoCompra.pack(side='top')

        self.entryPrecoCompra = tk.Entry(self.frameIngr, width=20)
        self.entryPrecoCompra.pack()

        labelUnitCompra = tk.Label(self.frameIngr, text='Unidade')
        labelUnitCompra.pack(side='top')

        self.entryUnitCompra = tk.Entry(self.frameIngr, width=20)
        self.entryUnitCompra.pack()

        buttonMsg = tk.Button(self.frameIngr, text='Salvar', bg="#4080ff", fg="gray1" , command=self.salvarIngrediente)
        buttonMsg.pack(side='top', pady=20)

        buttonBack = tk.Button(self.frameIngr, text='Tela anterior',
                               command=self.showFrameMenu, bg="#4080ff", fg="gray1")
        buttonBack.pack(side='bottom', anchor="sw")

    def frameAtt_Ingredient(self):
        self.frameAtt_Ingr = tk.Frame(self.container)
        labelAt = tk.Label(self.frameAtt_Ingr, text='Atualizar', bg="#006494", fg="#FFFFFF", font=("Helvetica", 10) )
        labelAt.pack(side='top', ipadx=130)
        labelIngredienteAt = tk.Label(self.frameAtt_Ingr, text='Ingrediente')
        labelIngredienteAt.pack(side='top', pady=10)
        self.entryOption = tk.Entry(self.frameAtt_Ingr, width=20)
        self.entryOption.pack()

        buttonMsg = tk.Button(self.frameAtt_Ingr, text='Buscar', bg="#4080ff", fg="gray1",
                              command=self.buscarIngrediente)
        buttonMsg.pack(side='top', pady=10)

        self.dadosAtualizarCusto()

        buttonBack = tk.Button(self.frameAtt_Ingr, text='Tela anterior',
                               command=self.showFrameMenu, bg="#4080ff", fg="gray1")
        buttonBack.pack(side='bottom', anchor="sw")

    def frameCdst_Ingredient(self):
        self.frameCdst_Ingr = tk.Frame(self.container)

        labelAt = tk.Label(self.frameCdst_Ingr,text='Cadastrar Novo Custo', bg="#006494", fg="#FFFFFF", font=("Helvetica", 10))
        labelAt.pack(side='top', ipadx=130)

        labelIngredienteNew = tk.Label(self.frameCdst_Ingr, text='Ingrediente')
        labelIngredienteNew.pack(side='top',pady=10)
        self.entryOptionNew = tk.Entry(self.frameCdst_Ingr, width=20)
        self.entryOptionNew.pack()

        buttonMsg = tk.Button(self.frameCdst_Ingr, text='Buscar',  bg="#4080ff", fg="gray1",
                              command=self.buscarIngredienteCadastro)
        buttonMsg.pack(side='top', pady=10)

        self.dadosCadastrarCusto()

        buttonBack = tk.Button(self.frameCdst_Ingr, text='Tela anterior',
                               command=self.showFrameMenu, bg="#4080ff", fg="gray1")
        buttonBack.pack(side='bottom', anchor="sw")

    def frameReceita(self):
        self.frameReceita = tk.Frame(self.container)

        labelAt = tk.Label(self.frameReceita, text='Cadastrar Receita', bg="#006494", fg="#FFFFFF", font=("Helvetica", 10))
        labelAt.pack(side='top', ipadx=130)

        labelRec = tk.Label(self.frameReceita, text='Nome para receita')
        labelRec.pack(side='top', pady=10)
        self.entryNameRecipe = tk.Entry(self.frameReceita, bg='whitesmoke', width=20)
        self.entryNameRecipe.pack()
        self.lista = []

        labelIng = tk.Label(self.frameReceita, text='Ingredientes')
        labelIng.pack(side='top', pady=10)
        self.entryOptionRecipe = tk.Entry(self.frameReceita, bg='whitesmoke', width=20)
        self.entryOptionRecipe.pack()

        buttonMsg = tk.Button(self.frameReceita, text='Buscar', bg="#4080ff", fg="gray1",command=self.newEntry)
        buttonMsg.pack(side='top')
        self.listOption = tk.Listbox(self.frameReceita)
        self.labelOptions = tk.Label(self.frameReceita, text="Ingredientes selecionados: ")
        self.labelOptions.pack()
        self.listOption.pack()

        buttonMsg = tk.Button(self.frameReceita, text='Proximo', bg="#4080ff", fg="gray1",command=self.showFrame5)
        buttonMsg.pack(side='top')

        buttonBack = tk.Button(self.frameReceita, text='Tela anterior', command=self.showFrameMenu, bg="#4080ff", fg="gray1")
        buttonBack.pack(side='bottom', anchor="sw")

    def frameBolo(self):
        self.frameBolo = tk.Frame(self.container)

        label = tk.Label(self.frameBolo, text='Nome do Bolo')
        label.pack(side='top')

        self.entryBolo = tk.Entry(self.frameBolo, width=20)
        self.entryBolo.pack()

        labelBoloRecipe = tk.Label(self.frameBolo, text='Receita')
        labelBoloRecipe.pack(side='top')

        self.entryBoloRecipe = tk.Entry(self.frameBolo, width=20)
        self.entryBoloRecipe.pack()

        buttonMsg = tk.Button(self.frameBolo, text='Buscar', command=self.calculoCustoIngrediente,  bg="#4080ff", fg="gray1")
        buttonMsg.pack(side='top', pady=10)

        labelBoloVenda = tk.Label(self.frameBolo, text='Preço de Venda')
        labelBoloVenda.pack(side='top')

        self.entryBoloSell = tk.Entry(self.frameBolo, width=20)
        self.entryBoloSell.pack()

        labelBoloCliente = tk.Label(self.frameBolo, text='Cliente')
        labelBoloCliente.pack(side='top')

        self.entryBoloCliente = tk.Entry(self.frameBolo, width=20)
        self.entryBoloCliente.pack()

        self.labelBoloIngrediente = tk.Label(self.frameBolo, text='Ingredientes: ').pack()
        self.ingText = tk.StringVar()
        self.entryIng = tk.Entry(self.frameBolo, state="readonly", text=self.ingText)
        self.entryIng.pack()

        self.labelBoloCustoIngrediente = tk.Label(self.frameBolo, text='Custo: ').pack()
        self.ingCustoText = tk.StringVar()
        self.entryIngCusto = tk.Entry(self.frameBolo, state="readonly", text=self.ingCustoText)
        self.entryIngCusto.pack()

        buttonMsg = tk.Button(self.frameBolo, text='Salvar', command=self.salvarBolo,  bg="#4080ff", fg="gray1")
        buttonMsg.pack(side='top', pady=10)

        buttonBack = tk.Button(self.frameBolo, text='Tela anterior', command=self.showFrameMenu, bg="#4080ff", fg="gray1")
        buttonBack.pack(side='bottom', anchor="w")

    def frameRlt_Bolo(self):
        self.frameRlt_Bolo = tk.Frame(self.container)

        label = tk.Label(self.frameRlt_Bolo, text='Cálculo de Lucro', bg="#006494", fg="#FFFFFF", font=("Helvetica", 10))
        label.pack(side='top', ipadx=130)

        label = tk.Label(self.frameRlt_Bolo, text='Nome do Bolo')
        label.pack(side='top', pady=10)
        self.entryBoloSearch = tk.Entry(self.frameRlt_Bolo, width=20)
        self.entryBoloSearch.pack()

        buttonMsg = tk.Button(self.frameRlt_Bolo, text='Buscar', command=self.calculoLucro, bg="#4080ff", fg="gray1")
        buttonMsg.pack(side='top', pady=10)

        self.labelCusto = tk.Label(self.frameRlt_Bolo, text='Custo: ').pack(pady=10)
        self.ingCustoLucroText = tk.StringVar()
        self.entryIngCusto = tk.Entry(self.frameRlt_Bolo, state="readonly", text=self.ingCustoLucroText)
        self.entryIngCusto.pack()

        self.labelVenda = tk.Label(self.frameRlt_Bolo, text='Preço de Venda: ').pack(pady=10)
        self.ingVendaText = tk.StringVar()
        self.entryIngVenda = tk.Entry(self.frameRlt_Bolo, state="readonly", text=self.ingVendaText)
        self.entryIngVenda.pack()

        self.labelLucro = tk.Label(self.frameRlt_Bolo, text='Lucro: ').pack(pady=10)
        self.ingLucroText = tk.StringVar()
        self.entryIngLucro = tk.Entry(self.frameRlt_Bolo, state="readonly", text=self.ingLucroText)
        self.entryIngLucro.pack()

        buttonBack = tk.Button(self.frameRlt_Bolo, text='Tela anterior',
                               command=self.showFrameMenu, bg="#4080ff", fg="gray1")
        buttonBack.pack(side='left', pady=10)


    def buscarIngrediente(self):
        try:
            ingrediente = self.ing_coll.find_ingredient(self.entryOption.get())
        except ValueError:
            tk.messagebox.showerror(master=None, title="Erro", message='Ingrediente não encontrado!')
            if self.entryOption.get() is not None:
                self.entryPrecoCompra.delete(0, 100)
            else:
                tk.messagebox.showerror(master=None, title="Erro", message='Informe o ingrediente para busca-lo!')
        else:
            tk.messagebox.showinfo(master=None, title="Sucesso", message='Ingrediente encontrado com sucesso!')

    def buscarIngredienteCadastro(self):
        global ingrediente
        try:
            ingrediente = self.ing_coll.find_ingredient(self.entryOptionNew.get())
        except ValueError:
            tk.messagebox.showerror(master=None, title="Erro", message='Ingrediente não encontrado!')
            if self.entryOptionNew.get() is not None:
                self.entryPrecoNew.delete(0, 100)
            else:
                tk.messagebox.showerror(master=None, title="Erro", message='Informe o ingrediente para busca-lo!')
        else:
            tk.messagebox.showinfo(master=None, title="Sucesso", message='Ingrediente encontrado com sucesso!')

    def atualizarIngredienteCusto(self):
        try:
            ingrediente = self.ing_coll.find_ingredient(self.entryOption.get())
        except ValueError:
            tk.messagebox.showerror(master=None, title="Erro", message='Ingrediente não atualizado.')
            self.entryPrecoCompraAt.delete(0, 100)
            self.entryUnitCompraAt.delete(0, 100)

        else:
            tk.messagebox.showinfo(master=None, title="Sucesso", message='Ingrediente atualizado com sucesso.')
            lista = Lista_Preco.from_data(
                float(self.entryPrecoCompraAt.get()),
                datetime.today(),
                self.entryUnitCompraAt.get()
            )
            self.ing_coll.update_ingredient(ingrediente, lista.dict_data)
            self.entryPrecoCompraAt.delete(0, 100)
            self.entryUnitCompraAt.delete(0, 100)
            self.entryOption.delete(0, 100)

    def cadastrarIngredienteCusto(self):
        custo = float(self.entryPrecoNew.get()) / float(self.entryUnitCompraNew.get())
        try:
            ingrediente = self.ing_coll.find_ingredient(self.entryOptionNew.get())
        except ValueError:
            tk.messagebox.showerror(master=None, title="Erro", message='Ingrediente não atualizado.')
            self.entryPrecoNew.delete(0, 100)
            self.entryUnitCompraNew.delete(0, 100)

        else:
            tk.messagebox.showinfo(master=None, title="Sucess",
                                   message='Novo custo cadastrado com sucesso. Valor do custo: '
                                           + str(custo))
            lista = Lista_Preco.from_data(
                float(self.entryPrecoNew.get()),
                datetime.today(),
                self.entryUnitCompraNew.get()
            )
            self.ing_coll.new_cost_ingredient(ingrediente, lista.dict_data)
            self.clearIngredientCadastrado()

    def salvarIngrediente(self):
        lista = Lista_Preco.from_data(
            float(self.entryPrecoCompra.get()),
            datetime.today(),
            self.entryUnitCompra.get()
        )
        ing_1 = Ingredient.from_data(
            self.entryIngrediente.get(),
            float(self.entryPrecoCompra.get()) / float(self.entryUnitCompra.get()),
            self.entryUnit.get(),
            lista.dict_data
        )
        try:
            _id = self.ing_coll.insert_ingredient(ing_1)

        except ValueError:
            tk.messagebox.showerror(master=None, title="Error", message='Ingrediente já inserido na coleção.')
            self.clearIngredient()
        else:
            tk.messagebox.showinfo(master=None, title="Sucesso", message="Ingrediente adicionado com sucesso!")
            self.clearIngredient()

    def calculoCustoIngrediente(self):
        costIngrediente = []
        ingredient = []
        ingText = []
        try:
            self.recipe = self.recp_coll.find_recipe(self.entryBoloRecipe.get())
            for i in range(len(self.recipe['ingredientes'])):
                ingredient = self.ing_coll.find_ingredient(self.recipe['ingredientes'][i]['name'])
                ingText += [ingredient['name']]
                costIngrediente += [(ingredient['cost'] * int(self.recipe['ingredientes'][i]['quantidade']))]
            self.ingText.set(ingText)
        except ValueError as err:
            tk.messagebox.showerror(master=None, title="Erro", message="Receita não encontrada, não foi possivel calcular o custo")
        else:
            custo = sum(costIngrediente)
            self.ingCustoText.set(custo)
            self.listaIngrediente = []
            for i in range(len(self.recipe['ingredientes'])):
                self.listaIngrediente += [{
                    'name': self.recipe['ingredientes'][i]['name'],
                    'quantidade': self.recipe['ingredientes'][i]['quantidade']
                }]
            self.recipe = [{
                'name': self.recipe['name'],
                'ingredientes':
                    self.listaIngrediente

            }]

    def proximaLista(self):
        self.prox_Lista = tk.Frame(self.container)
        self.prox_Lista.grid(row=0, column=0, sticky='nsew')
        self.labelQtd = tk.Label(self.prox_Lista, text="Quantidade dos ingredientes", bg="#006494", fg="#FFFFFF", font=("Helvetica", 10))
        self.labelQtd.pack(ipadx=130)
        self.entryQtd = []
        self.labelQtd = []
        for i in range(len(self.lista)):
            self.labelQtd.append(tk.Label(self.prox_Lista, pady=10, text="Quantidade do Ingrediente: " + self.lista[i]))
            self.entryQtd.append(tk.Entry(self.prox_Lista, width="20"))
        for i in range(len(self.lista)):
            self.labelQtd[i].pack()
            self.entryQtd[i].pack()

        buttonMsg = tk.Button(self.prox_Lista, text='Enviar',bg="#4080ff", fg="gray1", command=self.newRecipe)
        buttonMsg.pack(side='top', pady=20)

    def newRecipe(self):
        listaIngrediente = []
        for i in range(len(self.entryQtd)):
            qtdList = self.entryQtd[i].get()
            listaIngrediente += [{
                'name': self.lista[i],
                'quantidade': qtdList
            }]
        recipe = Recipe.from_data(
            self.entryNameRecipe.get(),
            listaIngrediente
        )
        try:
            _id = self.recp_coll.insert_recipe(recipe)

        except ValueError:
            tk.messagebox.showerror(master=None, title="Erro", message=ValueError)
        else:
            tk.messagebox.showinfo(master=None, title="Sucesso", message="Receita adicionada com sucesso!")
            self.clearRecipe()
            self.showframeReceita()

    def newEntry(self):
        try:
            _id = self.ing_coll.find_ingredient(self.entryOptionRecipe.get())
        except ValueError:
            tk.messagebox.showerror(master=None, title="Erro", message="Ingrendiente não encontrado")
            self.entryOptionRecipe.delete(0, 100)
        else:
            if self.entryOptionRecipe.get() not in self.lista:
                self.lista += [self.entryOptionRecipe.get()]
                self.listOption.insert('end', self.entryOptionRecipe.get())

        self.entryOptionRecipe.delete(0, 100)

    def dadosAtualizarCusto(self):
        labelAt = tk.Label(self.frameAtt_Ingr, text='Lista de preços\datas')
        labelAt.pack(side='top')
        labelPrecoCompraAt = tk.Label(self.frameAtt_Ingr, text='Preço de Compra')
        labelPrecoCompraAt.pack(side='top')

        self.entryPrecoCompraAt = tk.Entry(self.frameAtt_Ingr, width=20,)
        self.entryPrecoCompraAt.pack()

        labelUnitCompraAt = tk.Label(self.frameAtt_Ingr, text='Unidade')
        labelUnitCompraAt.pack(side='top', pady=10)

        self.entryUnitCompraAt = tk.Entry(self.frameAtt_Ingr, width=20)
        self.entryUnitCompraAt.pack()

        buttonMsg = tk.Button(self.frameAtt_Ingr, text='Atualizar', bg="#4080ff", fg="gray1",
                              command=self.atualizarIngredienteCusto)
        buttonMsg.pack(side='top', pady=10)

    def dadosCadastrarCusto(self):

        labelAt = tk.Label(self.frameCdst_Ingr, text='Lista de preços\datas')
        labelAt.pack(side='top')
        labelPrecoCompraAt = tk.Label(self.frameCdst_Ingr, text='Preço de Compra')
        labelPrecoCompraAt.pack(side='top')

        self.entryPrecoNew = tk.Entry(self.frameCdst_Ingr, width=20)
        self.entryPrecoNew.pack()

        labelUnitCompraAt = tk.Label(self.frameCdst_Ingr, text='Unidade')
        labelUnitCompraAt.pack(side='top', pady=10)

        self.entryUnitCompraNew = tk.Entry(self.frameCdst_Ingr, width=20)
        self.entryUnitCompraNew.pack()

        buttonMsg = tk.Button(self.frameCdst_Ingr, text='Salvar', bg="#4080ff", fg="gray1",
                              command=self.cadastrarIngredienteCusto)
        buttonMsg.pack(side='top', pady=20)

    def close(self, evento=None):
        sys.exit()



    def salvarBolo(self):
        if len(self.entryBolo.get()) == 0:
            tk.messagebox.showerror(master=None, title="Error", message="Insira o nome do bolo")
        elif len(self.entryBoloRecipe.get()) == 0:
            tk.messagebox.showerror(master=None, title="Error", message="Insira o nome da receita")
        elif len(self.entryBoloSell.get()) == 0:
            tk.messagebox.showerror(master=None, title="Error", message="Insira o valor da venda")
        elif len(self.entryBoloCliente.get()) == 0:
            tk.messagebox.showerror(master=None, title="Error", message="Insira o nome do cliente")
        else:
            try:
                bolo = Bolo.from_data(
                    self.entryBolo.get(),
                    self.entryBoloCliente.get(),
                    float(self.ingCustoText.get()),
                    datetime.today(),
                    float(self.entryBoloSell.get()),
                    self.recipe
                )
                _id = self.bolo_coll.insert_bolo(bolo)
            except ValueError:
                tk.messagebox.showerror(master=None, title="Erro", message="Bolo já inserido na coleção ou Receita não encontrada.")
            else:
                tk.messagebox.showinfo(master=None, title="Sucesso", message="Bolo inserido com sucesso")
                self.clearBolo()

    def calculoLucro(self):
        try:
            bolo = self.bolo_coll.find_bolo(self.entryBoloSearch.get())

        except ValueError:
            tk.messagebox.showerror(master=None, title="Erro", message="Bolo não encontrado")
            self.ingCustoLucroText.set("")
            self.ingVendaText.set("")
            self.ingLucroText.set("")
        else:
            tk.messagebox.showinfo(master=None, title="Sucesso", message="Calculo do lucro efetuado com sucesso!")
            self.ingCustoLucroText.set(bolo['cost_ingredients'])
            self.ingVendaText.set(bolo['price_sell'])
            self.ingLucroText.set((bolo['price_sell'] - bolo['cost_ingredients']))

    def clearIngredient(self):
        self.entryIngrediente.delete(0, 100)
        self.entryUnit.delete(0, 100)
        self.entryUnitCompra.delete(0, 100)
        self.entryPrecoCompra.delete(0, 100)

    def clearBolo(self):
        self.entryBoloSell.delete(0, 100)
        self.entryBoloCliente.delete(0, 100)
        self.entryBoloRecipe.delete(0, 100)
        self.entryBoloSearch.delete(0, 100)
        self.ingCustoText.set("")
        self.ingText.set("")

    def clearRecipe(self):
        self.entryNameRecipe.delete(0, 100)
        self.entryOptionRecipe.delete(0, 100)
        self.listOption[:] = []
        self.entryQtd.clear()

    def clearIngredientCadastrado(self):
        self.entryUnitCompraNew.delete(0, 100)
        self.entryPrecoNew.delete(0, 100)
        self.entryOptionNew.delete(0, 100)
