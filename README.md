# **Estudio de Mercado y Análisis de Aguacates para Cadena Hotelera**

Nombre del proyecto
# **"AvoEconomics: The Business of Green Gold"**
Cómo el aguacate transforma estrategias en los hoteles de lujo de la cadena Hilton.



## **Equipo de Proyecto**

* Julieth Vasco Bueno
* Gustavo Chavez



## **Planificación**

En nuestro proyecto, adoptamos una metodología ágil para planificar y gestionar tareas, utilizando GitHub como nuestra principal herramienta de colaboración. 
Esta metodología nos permitió dividir el trabajo en pequeñas entregas incrementales, priorizando y ordenando la colaboración interna.  
En GitHub, implementamos un tablero Kanban, estructurando el flujo de trabajo en columnas como "Por hacer", "En progreso" y "Completado". 

![alt text](/images/imageagil.png)

Cada tarea fue registrada como un *issue*, con descripciones claras, asignaciones responsables y etiquetas que facilitaron la organización y priorización. 
Los *milestones* nos ayudaron a definir metas clave y seguir nuestro progreso en tiempo real.  

Esta estrategia no solo aumentó la transparencia del equipo, sino que también fomentó una comunicación más fluida y una toma de decisiones más ágil. 


---


## **1. Diagnóstico Actual: Explorando Oportunidades en el Mercado de Aguacates**

Nuestro cliente, la cadena hotelera Hilton (a partir de ahora "Cliente"), esta enfocada en mantener una experiencia premium, con una oferta gastronómica optimizada. 
Con huéspedes que en los últimos años han demostrado un creciente interés en alimentos saludables y sostenibles, el equipo de Planificación Estratégica del Cliente ha identificado una oportunidad para optimizar los costos y desperdicios de sus menús diseñados para atraer a un mercado de turistas estadounidenses y mexicanos, conocidos por su afinidad cultural con el aguacate focalizandose en dos zonas estratégicas:

1. Zona sur de EEUU: desde California hasta Florida, donde reside la mayoría de mexicanos debido a la cerca con su país de origen.
2. New York: por tener un público exigente y de alto poder adquisitivo.

Por lo tanto, los 12 hoteles alcanzados para este estudio son:

![alt text](images/tablahoteles.png)


Por lo tanto, las zonas geográficas alcanzadas en esta iniciativa son:

![alt text](images/maparegiones.png)



### Premisas Iniciales
- **Situación actual:** La cadena hotelera no tiene una buena gestión de compras, ni un enfoque claro en alimentos saludables ni en personalización cultural en sus menús premium.  

- **Problemáticas:**  
  1. Fluctuación de precios de aguacates en mercados clave.  
  2. Falta de claridad sobre la potencial demanda de aguacates en cada hotel.  
  3. Alta tasa de desperdicios de aguacates.

- **Mercado objetivo:** Turistas de EEUU y México, y visitantes internacionales que demandan opciones frescas y saludables.  

- **Competencia:** Resorts líderes que incluyen guacamole gourmet, tostadas de aguacate y opciones con aguacate en sus menús. 

Entre ellos, se destacan como principales competidores:

  **1.Ojai Valley Inn, California**
Este resort en California es famoso por su experiencia de bienestar y alimentos frescos, que incluyen opciones como guacamole en sus menús de cocina saludable​

**2.The Ritz-Carlton, Sarasota, Florida**
Ofrece menús que incorporan aguacate, aprovechando ingredientes frescos para opciones saludables como guacamole en sus platos de ensaladas y snacks​

**3.La Playa Beach & Golf Resort, Naples, Florida**
Se destacan sus opciones saludables, como ensaladas con aguacate y guacamole, integrados en el menú de su restaurante gourmet​

**4.Hotel del Coronado, San Diego, California**
Histórico hotel que incluye varias opciones frescas y saludables, con aguacate como un ingrediente clave, ya sea en ensaladas o como parte del menú de desayuno​

**5.The Standard, Miami, Florida**
Conocido por su enfoque en la alimentación saludable y productos frescos, el restaurante de este hotel incluye guacamole y otros platos a base de aguacate​s



### Informe As-Is
Actualmente, el menú de nuestro cliente carece de opciones diferenciadas, lo que podría representar una pérdida de mercado en comparación con hoteles de la misma categoría. Además, no se han evaluado los precios y calidad del aguacate de regiones clave como México, Perú o la misma California para garantizar rentabilidad y la sostenibilidad de la oferta en el tiempo. Tampoco se planifica y negocio la compra de aguacates de forma adecuada. Debido a la amplia opciones de mejor se acuerda con el Cliente focalizarnos en responder 3 preguntas claves de negocio:


  **Eficiencia en la cadena de suministro y abastecimiento** 
  
  Pregunta clave: ¿Estamos comprando los aguacates de proveedores que equilibran precio, calidad y confiabilidad, minimizando el tiempo de transporte y maximizando la frescura?
  Por qué es importante: Los aguacates tienen una vida útil limitada. Trabajar con proveedores cercanos o con procesos logísticos ágiles asegura que lleguen frescos y se reduzca el desperdicio.
  Palanca clave: Optimización de proveedores con contratos flexibles y métodos sostenibles.


  **Control de costos y márgenes en el menú**
  
  Pregunta clave: ¿Estamos generando el margen esperado en los platos que contienen aguacates sin sacrificar la calidad o elevar los costos de operación?
  Por qué es importante: Los aguacates son un ingrediente premium. Es crucial evaluar su contribución al margen bruto del menú y ajustar los precios si es necesario, asegurando que los platos sigan siendo competitivos y rentables.


  **Monitoreo del desperdicio**

  Pregunta clave: ¿Qué porcentaje de los aguacates comprados termina en desperdicio, y qué procesos estamos implementando para reducirlo?
  Por qué es importante: El desperdicio no solo afecta la rentabilidad, sino que también contradice objetivos sostenibles. Evaluar puntos críticos (preparación, almacenamiento o sobrantes en platos) es clave para minimizar pérdidas.


---



## **2. Transformando Datos en Oportunidades: Análisis de los Datos**

Para abordar estos desafíos, hemos realizado un análisis exhaustivo basado en datos relevantes sobre precios y calidad del aguacate. Para ellos hemos incorporado variables internas y exógenas. A continuación detallamos las fuentes de datos utilizadas:

### Fuentes Internas:
- **Consumo gastronómico de la cadena hotelera:** (consumoshistoricos.csv): Contiene ...<COMPLETAR> 

- **Avocado:** (avocado.csv): Contiene los datos venta de aguacate que nuestro cliente ha comprado de una consultora para analizar internamente. Este acrchivo contiene los campos: Date,AveragePrice,Total Volume,4046,4225,4770,Total Bags,Small Bags,Large Bags,XLarge Bags,type,year,region 


- **Campo derivado**: Para poder estimar la cantidad de aguacate convencionales y orgánicos contenidos en una tonelada y estimar el precio de la tonelada, hemos creado/agregado nuevos campos derivados. Para estimar los pesos promedios de cada aguacate según su tipo nos hemos basado en la siguiente tabla de estandarización:

![alt text](images/imagepesosavg.jpeg)

Por lo tanto, determinamos los siguientes pesos promedio según el tipo de aguacate: convencional 250gr y orgánico 300gr 



### Fuentes Exógenas:
- **Organización de las Naciones Unidas para la Alimentación y la Agricultura:** (FAOSTAT_Crops and livestock products.csv) Datos históricos y en tiempo real de mercados clave (México, Perú, California).  
- **DOrganización de las Naciones Unidas para la Alimentación y la Agricultura:** (FAOSTAT_data_avocado_Producer_Prices.csv) Datos de búsqueda y tendencias de redes sociales, como Instagram y Google Trends.  




- **Estadísticas de Turismo:** Afiliación cultural y preferencias alimentarias de turistas mexicanos en los destinos clave.

### Metodología
1. **Scraping de Precios:** Datos recopilados de mercados mayoristas y minoristas de aguacates. <COMPLETAR> 
2. **Análisis Exploratorio:** Visualización de fluctuaciones de precios según región y temporada.  
3. **Modelos Predictivos:** Forecasting para determinar los precios en las próximas temporadas.  
4. **Clusterización:** Identificación de regiones con mejor balance de precio y calidad.  
5. **Correlación:** Relación entre precio del aguacate y popularidad de menús con aguacate en hoteles competidores.


### Análisis
- **Hallazgo 1:** Los precios de los aguacates tienden a ser más bajos de marzo a junio, coincidiendo con la temporada baja de turismo.  
- **Hallazgo 2:** México ofrece el mejor balance precio-calidad, pero su precio es más volátil que el de Perú.  
- **Hallazgo 3:** El 35% de las reseñas en redes sociales que mencionan aguacates también hacen referencia a experiencias de lujo, destacando su potencial en el segmento premium.  
- **Visualizaciones:** Incluye gráficos de tendencias, correlaciones y clusters.

---

## **3. Recomendaciones Estratégicas y Conclusiones**

### Insights Relevantes
1. **Adopción de Aguacates Mexicanos:** Incorporar opciones en el menú premium basadas en aguacates mexicanos, destacando su autenticidad cultural.  
2. **Sostenibilidad y Marketing:** Promocionar la inclusión de aguacates como parte de un menú saludable y eco-friendly para mejorar la percepción de marca.  
3. **Ajuste Estacional:** Diseñar estrategias de compra estacional para minimizar el impacto de la volatilidad en precios.  

### Propuesta de Acción
- Incluir platos como tostadas gourmet, guacamole en piedra y smoothies con aguacate.  
- Negociar contratos estacionales con productores mexicanos para asegurar la mejor calidad a precios competitivos.  
- Realizar campañas dirigidas en redes sociales para atraer al mercado objetivo.

---

## **Cómo Usar Este Repositorio**
1. **Carpeta `/data`:** Contiene los datasets utilizados, incluyendo precios históricos y datos turísticos.  
2. **Carpeta `/notebooks`:** Jupyter Notebooks con los análisis de datos y visualizaciones.  
3. **Carpeta `/reports`:** Resúmenes ejecutivos y gráficos listos para presentaciones.  

---

## **Acerca del Proyecto**
Este proyecto fue desarrollado como parte de un trabajo práctico para un posgrado en Data Science. Nuestro enfoque combina análisis de datos avanzados con una narrativa estratégica para apoyar decisiones empresariales en la industria hotelera.
