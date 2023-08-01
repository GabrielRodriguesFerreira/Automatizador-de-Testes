import Utilitarios
import pyautogui

utilitarios = Utilitarios.Utilitarios()

if utilitarios.valida_spoon_aberto("Spoon - [no name]") or utilitarios.valida_source_aberto("Spoon - sourceUpdate"):

    utilitarios.clicar_em_local_pastas(utilitarios.x_coord,utilitarios.y_coord)

    if utilitarios.aguardar_abrir_aplicativo_abrir():

        utilitarios.clicar_em_local_arquivo_source(utilitarios.x_coord_src, utilitarios.y_coord_src)

        utilitarios.rolar_pesquisa()

        utilitarios.clicar_em_local_arquivo_source(utilitarios.x_coord_src, utilitarios.y_coord_src)

        utilitarios.clicar_em_local_arquivo_source_open(utilitarios.x_coord_open,utilitarios.y_coord_open)
        
    if utilitarios.aguardar_abrir_aplicativo_Update():

        utilitarios.clicar_executar()

        utilitarios.clicar_dtfim(utilitarios.x_coord_dtfim, utilitarios.y_coord_dtfim)

        utilitarios.escrever_data("2100-01-01")

        utilitarios.clicar_dtfim(utilitarios.x_coord_dtini, utilitarios.y_coord_dtini)

        utilitarios.escrever_data("1900-01-01")

        utilitarios.clicar_run(utilitarios.x_clicarRun, utilitarios.y_clicarRun)

        if utilitarios.valida_integration_aberto("Spoon - integrationClient"):
            
else:

    if utilitarios.abrir_aplicativo():

        pyautogui.sleep(30)
    
        if utilitarios.aguardar_abrir_aplicativo():

            utilitarios.clicar_em_local_pastas(utilitarios.x_coord,utilitarios.y_coord)

        if utilitarios.aguardar_abrir_aplicativo_abrir():

            utilitarios.clicar_em_local_arquivo_source(utilitarios.x_coord_src, utilitarios.y_coord_src)

            utilitarios.rolar_pesquisa()

            utilitarios.clicar_em_local_arquivo_source(utilitarios.x_coord_src, utilitarios.y_coord_src)

            utilitarios.clicar_em_local_arquivo_source_open(utilitarios.x_coord_open,utilitarios.y_coord_open)
        
        if utilitarios.aguardar_abrir_aplicativo_Update():

            utilitarios.clicar_executar()

            utilitarios.clicar_dtfim(utilitarios.x_coord_dtfim, utilitarios.y_coord_dtfim)

            utilitarios.valida_escrita("2100-01-01")

            utilitarios.clicar_dtfim(utilitarios.x_coord_dtini, utilitarios.y_coord_dtini)

            utilitarios.escrever_data("1900-01-01")

            utilitarios.clicar_run(utilitarios.x_clicarRun, utilitarios.y_clicarRun)


