# Dataset Card

## Identificación

- Nombre: SMS Spam Collection
- Fuente original: UCI Machine Learning Repository
- Responsable: Tiago A. Almeida y José María Gómez Hidalgo
- Versión o fecha: 2012
- Licencia: Uso académico e investigación
- Idioma: Inglés

## Propósito y variable objetivo

El conjunto de datos contiene mensajes SMS clasificados como legítimos (ham) o spam. El propósito de este proyecto es desarrollar y evaluar técnicas de Procesamiento de Lenguaje Natural (PLN) para la clasificación automática de mensajes de texto.

Variable objetivo:

- label
  - ham: mensaje legítimo
  - spam: mensaje no deseado

## Diccionario de datos

| Columna | Tipo | Descripción | Valores o unidad |
|---|---|---|---|
| label | Categórica | Clasificación del mensaje SMS | ham, spam |
| text | Texto | Contenido del mensaje SMS | Texto libre |

## Procedimiento de obtención

El dataset fue descargado desde el repositorio UCI Machine Learning Repository. El archivo original denominado SMSSpamCollection fue transformado a formato CSV para asegurar compatibilidad con las herramientas de auditoría y procesamiento utilizadas en el proyecto. La transformación consistió en la creación de las columnas label y text preservando íntegramente el contenido original de cada registro.

## Calidad observada

Resultados de la auditoría automática:

- Total de registros: 5,572
- Total de variables: 2
- Valores nulos en texto: 0
- Valores nulos en la variable objetivo: 0
- Duplicados de texto: 403
- Distribución de clases:
  - ham: 86.59 %
  - spam: 13.41 %

Longitud de textos:

- Mediana (p50): 62 caracteres
- Percentil 90 (p90): 156 caracteres
- Percentil 99 (p99): 277 caracteres
- Longitud máxima observada: 910 caracteres

Hash SHA-256:

d368d659ea5fa1c2cbf9f6be756622b4329ef8c3bf105572c03eb0741f908701

## Ejemplos anonimizados

1. ham → "Go until jurong point, crazy.. Available only in bugis n great world..."
2. ham → "Ok lar... Joking wif u oni..."
3. spam → "Free entry in 2 a wkly comp to win FA Cup final tkts..."
4. ham → "U dun say so early hor..."
5. ham → "Nah I don't think he goes to usf..."

Los ejemplos fueron seleccionados únicamente con fines ilustrativos y corresponden a mensajes presentes en el corpus original.

## Población cubierta y excluida

La población cubierta corresponde a mensajes SMS en idioma inglés recopilados de distintas fuentes públicas utilizadas para investigación en detección de spam. El corpus no representa correos electrónicos, publicaciones en redes sociales, mensajería instantánea moderna ni comunicaciones en otros idiomas distintos del inglés.

## Riesgos, sesgos y usos prohibidos

Posibles sesgos identificados:

- Predominio de mensajes legítimos frente a mensajes spam.
- Limitación al idioma inglés.
- Contexto temporal específico asociado a la época de recopilación del corpus.
- Posible presencia de mensajes repetidos.

Usos prohibidos:

- Inferir características personales de individuos.
- Tomar decisiones automatizadas sobre personas.
- Generalizar resultados a otros idiomas o canales de comunicación sin validación previa.