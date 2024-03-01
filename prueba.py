s = "{   \n    \"receptor\": {\n        \"tipo_documento\": \"36\",\n        \"numero_documento\": \"06142307091063\",\n        \"nombre\": \"Obed Espinoza\",\n        \"correo\": \"obedaeg@gmail.com\",\n        \"codigo_actividad\": \"45401\",\n        \"descripcion_actividad\": \"VENTA AL POR MENOR DE OTROS PRODUCTOS EN COMERCIOS NO ESPECIALIZADOS\",\n        \"direccion\": {\n            \"departamento\": \"10\",\n            \"municipio\": \"10\",\n            \"complemento\": \"8 C OTE NO 1 3 B SAN SEBASTIAN AHUACHAPAN SC\"\n        },\n        \"telefono\": \"12345678\",\n        \"nrc\": \"1966072\"\n    },\n    \"codigo_actividad\":  \"45401\",\n    \"moneda\": \"USD\",\n    \"tipo_documento\": \"CRE\",\n    \"documento_relacion\":[\n        {\n            \"fecha_emision\": \"2024-02-011\"\n        }\n    ],\n    \"detalles\": [\n        {\n            \"codigo\": \"2282252\",\n            \"descripcion\": \"SNICKERS KS DOBLE BARRA  1X6X24UX93.3G||24\",\n            \"cantidad\": 24.0,\n            \"precio_unitario\": 1.15,\n            \"tipo_item\": 1,\n            \"unidad_medida\": 59,\n            \"monto_descuento\": 0.0,\n            \"venta_no_sujeta\": 0.0,\n            \"venta_exenta\": 0.0,\n            \"venta_gravada\": 27.6,\n            \"tributos\": [\"20\"],\n            \"psv\": 0,\n            \"no_gravado\": 0,\n            \"codigo_retencion_mh\": \"22\",\n            \"tipo_documento_tributario\": \"14\",\n            \"monto_sujeto_retencion\": 1.25,\n            \"iva_retenido\": 0.1438,\n            \"fecha_emision\": \"2024-02-11\",\n            \"tipo_generacion_documento\": 1\n        }\n    ]\n\n}"
print(s)

"""
{   
    "receptor": {
        "codigo_pais": "9320",
        "complemento": "PROLG. ALAMEDA JUAN PABLO II PSJ. SAN JORGE, # L-1, SAN SALVADOR, SAN SALVADOR",
        "tipo_documento": "36",
        "numero_documento": "06142307091063",
        "nombre": "Obed Espinoza",
        "correo": "obedaeg@gmail.com",
        "descripcion_actividad": "VENTA AL POR MENOR DE OTROS PRODUCTOS EN COMERCIOS NO ESPECIALIZADOS",
        "nombre_comercial": "Prueba de Receptor",
        "telefono": "12345667",
        "nombre_pais": "El Salvador",
        "tipo_persona": 1,
        "bien_titulo": "23",
        "codigo_actividad": "45401",
        "nit": "06142307091063",
        "direccion": {
            "departamento": "06",
            "municipio": "14",
            "complemento": "PROLG. ALAMEDA JUAN PABLO II PSJ. SAN JORGE, # L-1, SAN SALVADOR, SAN SALVADOR"
        }
    },
    "documento_relacionado": [{
        "fechaEmision": "2024-02-27",
        "numeroDocumento": "06142307091063",
        "tipoDocumento": "03",
        "tipoGeneracion": 1
    }],
    "codigo_actividad":  "45401",
    "tipo_documento":"NDE",
    "moneda": "USD",
    "detalles": [
        {
            "codigo": "2282252",
            "descripcion": "SNICKERS KS DOBLE BARRA  1X6X24UX93.3G||24",
            "cantidad": 24.0,
            "precio_unitario": 1.15,
            "tipo_item": 1,
            "unidad_medida": 59,
            "monto_descuento": 0.0,
            "venta_no_sujeta": 0.0,
            "venta_exenta": 0.0,
            "venta_gravada": 27.6,
            "tributos": ["20"],
            "psv": 0,
            "no_gravado": 0,
            "numero_documento": "123"
        },
        {
            "codigo": "2284431",
            "descripcion": "M&M LECHE/CHOC SHARING SIZE 1X6X24UX89G||24",
            "cantidad": 24.0,
            "precio_unitario": 1.15,
            "tipo_item": 1,
            "unidad_medida": 59,
            "monto_descuento": 0.0,
            "venta_no_sujeta": 0.0,
            "venta_exenta": 0.0,
            "venta_gravada": 27.6,
            "tributos": ["20"],
            "psv": 0,
            "no_gravado": 0,
            "numero_documento": "456"
        }
    ]
}
"""