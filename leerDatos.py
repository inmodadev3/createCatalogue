import os
from Conexion import conectar
from createPdf import generar_catalogo

def main():
    
    dataProductos = []
    ruta_CAREY_KOREANO = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/MODA Y ACCESORIOS/ACCESORIOS DE CABELLO/CAREY KOREANO/'
    ruta_CAREY_BASICO = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/MODA Y ACCESORIOS/ACCESORIOS DE CABELLO/CAREY BASICO/'
    ruta_CAREY_FRANCES = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/MODA Y ACCESORIOS/ACCESORIOS DE CABELLO/CAREY FRANCES/'

    ruta_BELLEZA = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/BELLEZA/'
    ruta_BELLEZA = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/BELLEZA/'
    ruta_BISUTERIA = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/BISUTERIA/'
    ruta_HOGAR_Y_FERRETERIA = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/HOGAR Y FERRETERIA/'
    ruta_INSUMOS_MEDICOS = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/INSUMOS MEDICOS/'
    ruta_JOYERIA_Y_FANTASIA = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/JOYERIA Y FANTASIA/'
    ruta_MASCOTAS = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/MASCOTAS/'
    ruta_MODA_Y_ACCESORIOS = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/MODA Y ACCESORIOS/'
    ruta_PAPELERIA = 'C:/xampp/htdocs/ownCloud/fotos_nube/FOTOS  POR SECCION CON PRECIO/PAPELERIA/'
    
    query = "SELECT strIdProducto,strDescripcion,intPrecio4 FROM tblProductos"
    
    #CONEXION A LA BASE DE DATOS
    connection = conectar()
    cursor = connection.cursor()
    ## REALIZAR LA CONSULTA DELA BASE DE DATOS
    cursor.execute(query)
    rows = cursor.fetchall()
    ### Crear un diccionario de precios a partir de los resultados de la base de datos
    precios_dict = {row[0]: int(row[2]) for row in rows}
    desc_dict = {row[0]: str(row[1]) for row in rows}

    #print(precios_dict)


    def procesar_data(ruta_principal):
        dataProductos.clear()
        for root, dirs, files in os.walk(ruta_principal):
            for name in files: 
                if name.endswith('$1.jpg'):
                    ref = name.split('$')
                    refe = ref[0]
                    precio = precios_dict.get(refe)
                    descrip = desc_dict.get(refe)
                #print( refe, descrip ,precio)

                    rutaFoto = os.path.join(root,name).replace("\\","/")
                    dataProductos.append([refe, descrip, precio, rutaFoto ])
                # print(os.path.join(refe, precio))
        #nombre_clase=(ruta_principal[66:-1])     # PARA CLASE NORMALES ESTA Y LINEA SIGUIENTE
        #generar_catalogo(f"{nombre_clase}", dataProductos)
        nombre_cAREY=(ruta_principal[106:-1])    #estas para sacar los carey
        print(nombre_cAREY)
        generar_catalogo(f"{nombre_cAREY}", dataProductos)
        #generar_catalogo("PAPELERIA", dataProductos)

    print("acaboo")

    procesar_data(ruta_CAREY_BASICO)
    procesar_data(ruta_CAREY_FRANCES)
    procesar_data(ruta_CAREY_KOREANO)
    # procesar_data(ruta_INSUMOS_MEDICOS)
    # procesar_data(ruta_BELLEZA)
    # procesar_data(ruta_BISUTERIA)
    # procesar_data(ruta_HOGAR_Y_FERRETERIA)
    # procesar_data(ruta_JOYERIA_Y_FANTASIA)
    # procesar_data(ruta_MASCOTAS)
    # procesar_data(ruta_MODA_Y_ACCESORIOS)
    # procesar_data(ruta_PAPELERIA)

if __name__ == "__main__":
    main()