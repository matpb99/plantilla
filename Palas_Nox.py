import re
import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard

data = {
    "EN EL MARCO DE LA PALA": [
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/carbon_frame.png?v=1.0",
            "description": "<strong>CARBON Frame</strong>: Marco de carbono. Utilizando este material en los marcos damos más rigidez y durabilidad al marco y a la pala en general."
        },
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/dcs.png?v=1.0",
            "description": "<strong>DCS Dynamic Composite Structure</strong>: Con la aplicación de más cantidad de material desde el marco hasta cuatro centímetros dentro de la cara conseguimos que no se note la diferencia de dureza entre el marco y la cara. De este modo conseguimos que no se produzcan grietas en la parte exterior de la pala."
        }
                                ],

    "EN EL NÚCLEO DE LA PALA": [
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/hrs_core_plus.png?v=1.0",
            "description": "<strong>HRS Core+</strong>: Núcleo con goma más densa aún que la HR3. Amplía la rapidez con la que el núcleo de la pala recupera su estado previo al golpeo de la bola. Con esta goma se consigue la máxima potencia."
        },

        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/hr2_core.png?v=1.0",
            "description": "<strong>HR2 Core+</strong>: Núcleo de goma de baja densidad, con un menor peso/m2 por lo que se utiliza siempre para palas en las que se busca un tacto más blando"
        },
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/hr3_core.png?v=1.0",
            "description": "<strong>HR3 Core</strong>: Núcleo con goma HR3 de alta densidad con el mayor efecto de memoria. Se consigue así una mayor potencia en el golpeo y salida de bola."
        },
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/hr3_black_eva.png?v=1.0",
            "description": "<strong>HR3 Core Black Eva</strong>: Núcleo con goma HR3 negra de alta densidad con el mayor efecto de memoria. Se consigue así una mayor potencia en el golpeo y salida de bola."
        },

        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/mbe.png?v=1.0",
            "description": "<strong>MLD Black Eva</strong>: Núcleo multicapa que conjuga distintas densidades de goma para optimizar la salida de bola en golpeos defensivos de baja velocidad y la potencia en remates."
        }

                                ],

    "EN LA CARA DE LA PALA": [
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/fiber_glass_silver.png?v=1.0",
            "description": "<strong>FIBER GLASS Silver</strong>: Tejido de fibra de vidrio con un acabado metalizado para darle a este material un grado de rigidez que está entre el carbono y la fibra de vidrio."
        },

        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/fiber_carbon_3k.png?v=1.0",
            "description": "<strong>FIBER CARBON 3K</strong>: El tejido 3K se consigue entrelazando los hilos de fibra de carbono formando cuadrados pequeños. "
        },

        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/fiber_glass_3k.png?v=1.0",
            "description": "<strong>FIBER GLASS 3K</strong>: El tejido 3K se consigue entrelazando los hilos de fibra formando cuadrados pequeños. En nuestro caso utilizamos una fibra 3K con un gramaje superior a la fibra de carbono normal logrando una mayor durabilidad del producto."
        },
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/carbon_12k.png?v=1.0",
            "description": "<strong>CARBON 12K</strong>: Carbono que se consigue entrelazando cintas de carbono vertical y horizontalmente. Al conseguir mucha más rigidez es un carbono más fino y con un peso 25% menor. Reducimos el peso de la pala sin perder rigidez ni durabilidad."
        },
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/carbon_18k.png?v=1.0",
            "description": "<strong>CARBON 18K</strong>: Máxima rigidez y resistencia manteniendo la ligereza de la pala gracias a los microfilamentos de carbono entrelazados más finos de nuestra gama de palas."
        },
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/18k_alum.png?v=1.0",
            "description": "<strong>CARBON 18K Alum</strong>: Carbono 18K Aluminizado que otorga un tacto sólido y confortable y un rendimiento más homogéneo ante los cambios de temperatura."
        },

        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/rough_surface.png?v=1.0",
            "description": "<strong>ROUGH Surface</strong>: Superficie rugosa sobre la última capa de la cara de la pala. Puede hacerse mediante material plástico premoldeado o con un baño en arena de sílice de bajo gramaje. Con esta rugosidad se consigue golpes con mayor efecto."
        },

        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/spin_plus.png?v=1.0",
            "description": "<strong>SPIN+</strong>: Novedosa tecnología que incluye dos tipos de acabado rugoso en la superficie de la cara, el 3D hexagonal ubicado en el centro de la pala y el acabado arena en el resto. Con esta doble rugosidad obtenemos mayor control y la posibilidad de imprimir mayores efectos a la bola. Moldeado con un baño en arena de sílice de bajo gramaje. Con esta rugosidad se consigue golpes con mayor efecto."
        },

        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/texture_3d.png?v=1.0",
            "description": "<strong>TEXTURE 3D</strong>: Acabado rugoso aplicado a la última capa de la cara de la pala para incrementar el efecto de los golpeos sin renunciar a la durabilidad del rugoso."
        }
                            ],

    "OTRAS ZONAS DE LA PALA": [
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/smartstrap.png?v=1.0",
            "description": "<strong>SMARTSTRAP®</strong>: El Nox Smart Strap es la última tecnología implementada a la nueva colección de palas que te permitirá cambiar el cordón de agarre de forma ágil y sencilla."
        },
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/oversize_grip.png?v=1.0",
            "description": "<strong>OVERSIZE Grip</strong>: Ampliación de la empuñadura de 30 mm. para los jugadores que necesitan un grip más largo tanto si tienen algún golpe a dos manos como si no. "
        },
        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/avs.png?v=1.0",
            "description": "<strong>AVS Anti Vibration System</strong>: Piezas de goma que se incrustan en el marco de la pala para absorber las posibles vibraciones que se producen cuando no se golpea la pelota en el centro de la pala."
        },

        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/eos_flap.png?v=1.0",
            "description": "<strong>EOS Flap</strong>: Perforaciones laterales diseñadas para incrementar la manejabilidad de la pala y repartir la distribución de pesos para que tengas en tus manos una pala rápida y letal."
        },

        {
            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/pulse_system.png?v=1.0",
            "description": "<strong>Pulse System</strong>: Disminución de las vibraciones que se transmiten a la mano del jugador con la inserción de gomas laterales que van desde la base del marco hasta la parte inferior del tapón de la pala."
        },

        {

            "image": "https://cdn.shopify.com/s/files/1/0813/9531/9081/files/custom_grip.png?v=1.0",
            "description": "<strong>CUSTOM Grip</strong>:Toda la gama Luxury incorpora la tecnología patentada NOX Custom Grip®, certificada por Testea Padel para el aumento de agarre y disminución de vibraciones."
        }
    ]
}

def create_table_from_raw(texto):

    html_output = '<h4>CARACTERÍSTICAS</h4>\n <table width="100%">\n<tbody>\n' 
    
    lineas = texto.split('#')

    for linea in lineas:
        try:

            linea = linea.strip()
            clave,valor = linea.split(":")
            html_output += f' <tr>\n  <td><b>{clave}</b></td>\n    <td>{valor}</td>\n  </tr>\n'
    
        except: pass

    html_output += '</tbody>\n</table>'

    html_output += '<h3>Calidad Certificada</h3> <p><strong>Testea Padel certifica la calidad de esta pala de pádel</strong> frente a roturas del marco y las caras de la pala, así como la durabilidad del producto frente a la fatiga.</p> <table style="border: 0;" width="100%"> <tbody style="border: 0;"> <tr style="border: 0;"> <td style="border: 0;"> <p style="text-align: center; border: 0;"><iframe title="YouTube video player" src="https://www.youtube.com/embed/C9S0kt2OgIs" frameborder="0" allowfullscreen="allowfullscreen"></iframe></p> </td> <td style="border: 0;"> <p style="text-align: center; border: 0;"><img src="https://cdn.shopify.com/s/files/1/2232/3715/files/CERTIFICATTESTEA_QualityCertificatedcopia_100x100.png?v=1.0"></p> </td> </tr> </tbody> </table>'

    
    return html_output

def extract_category(text):
    
    match = re.search(r'<strong>(.*?)</strong>', text)
    return match.group(1) if match else text 

def html_tech(selected_data):
    html_output = "<h4>TECNOLOGÍAS</h4>\n"

    for category, elements in selected_data.items():
        html_output += f'<h5>{category}</h5>\n'
        html_output += '<div class="table-wrapper">\n<table width="100%">\n<tbody>\n'
        
        for element in elements:
            image_url = element["image"]
            description = element["description"]
            html_output += f'<tr>\n<td style="width: 100%;"> <img src="{image_url}" width="80" height="80"> {description}</td>\n</tr>\n'
        
        html_output += '</tbody>\n</table>\n</div>\n'
    
    return html_output

def html_master(body, specs, tech):

    html_master_output = body + specs + tech

    return html_master_output

def main_function(data):

    st.title("Palas Nox")

    st.title('Descripción')
    body = st.text_input(label='Inserte texto', key=28)

    st.title('Especificaciones')
    specs = st.text_input(label= 'Inserte texto', key=22)

    st.title('Caracteristicas Técnicas')

    selected_data, checkbox_vars = {} , {}

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('EN EL MARCO DE LA PALA'.capitalize())
        checkbox_vars['EN EL MARCO DE LA PALA'] = []

        for element in data['EN EL MARCO DE LA PALA']:
            strong_text = extract_category(element['description'])
            is_checked = st.checkbox(strong_text)
            checkbox_vars['EN EL MARCO DE LA PALA'].append(is_checked)

        st.subheader('EN LA CARA DE LA PALA'.capitalize())
        checkbox_vars['EN LA CARA DE LA PALA'] = []

        for element in data['EN LA CARA DE LA PALA']:
            strong_text = extract_category(element['description'])
            is_checked = st.checkbox(strong_text)
            checkbox_vars['EN LA CARA DE LA PALA'].append(is_checked)
  
    with col2:

        st.subheader('OTRAS ZONAS DE LA PALA'.capitalize())
        checkbox_vars['OTRAS ZONAS DE LA PALA'] = []

        for element in data['OTRAS ZONAS DE LA PALA']:
            strong_text = extract_category(element['description'])
            is_checked = st.checkbox(strong_text)
            checkbox_vars['OTRAS ZONAS DE LA PALA'].append(is_checked)
        
        st.subheader('EN EL NÚCLEO DE LA PALA'.capitalize())
        checkbox_vars['EN EL NÚCLEO DE LA PALA'] = []

        for element in data['EN EL NÚCLEO DE LA PALA']:
            strong_text = extract_category(element['description'])
            is_checked = st.checkbox(strong_text)
            checkbox_vars['EN EL NÚCLEO DE LA PALA'].append(is_checked)

    if st.button("Generar HTML"):
        selected_data.clear()  

        for category, elements in data.items():
            selected_data[category] = []
            for idx, is_selected in enumerate(checkbox_vars[category]):
                if is_selected:
                    selected_data[category].append(elements[idx])
            if not selected_data[category]:
                del selected_data[category]

        html_master_output = html_master(body, create_table_from_raw(specs), html_tech(selected_data) )

        st.text_area(label="Resultado HTML", value=html_master_output, height=300)
        st_copy_to_clipboard(html_master_output, before_copy_label='📋Copiar al Portapapeles', after_copy_label='✅Texto Copiado!')

        st.title('Vista Previa')
        st.markdown(html_master_output, unsafe_allow_html=True)

if __name__ == '__main__':
    st.set_page_config(layout = "centered", initial_sidebar_state = "auto", page_title = "Plantillas SurSports")

    with st.sidebar:
        pass
    main_function(data)
