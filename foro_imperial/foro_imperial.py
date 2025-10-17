from flask import Flask, request, make_response, render_template_string
import time

app = Flask(__name__)
app.secret_key = 'Gaius_Tempus_Maximus_secretum'

FLAG = "CHRONOSCTF{flag_descubierta_R0m4_N0_S3_C0nstruy0_3n_Un_D1a}"

# (Las plantillas HTML con el estilo romano se mantienen exactamente igual que antes)
# ... (template_normal y template_admin van aquí) ...

# --- Plantilla HTML con estilo Romano para el Ciudadano ---
template_normal = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>ChronosCTF - Foro Imperial</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Lora&display=swap" rel="stylesheet">
    <style>
        body { background-color: #1a1a1a; color: #E0D6B3; font-family: 'Lora', serif; margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; text-align: center; }
        .container { background-color: #4a0e1d; border: 4px solid #DAA520; padding: 2em 3em; max-width: 800px; box-shadow: 0 0 25px rgba(255, 215, 0, 0.3); border-radius: 5px; }
        h1 { font-family: 'Cinzel', serif; color: #FFD700; text-transform: uppercase; letter-spacing: 3px; font-size: 2.5em; border-bottom: 2px solid #DAA520; padding-bottom: 10px; margin-bottom: 20px; }
        p { font-size: 1.2em; line-height: 1.6; }
        strong { color: #FFFFFF; font-weight: bold; }
    </style>
</head>
<body> <div class="container"> <h1>Bienvenido, Ciudadano</h1> <p>Has entrado al Foro Imperial, pero el conocimiento de Minerva está reservado para los dignos.</p> <p>Tu sello de sesión temporal es: <strong>{{ session_id }}</strong></p> </div> </body>
</html>
"""

# --- Plantilla HTML con estilo Romano para el Administrador ---
template_admin = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Acceso Concedido - Panel de Minerva</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Lora&display=swap" rel="stylesheet">
    <style>
        body { background-color: #1a1a1a; color: #E0D6B3; font-family: 'Lora', serif; margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; text-align: center; }
        .container { background-color: #2a3a63; border: 4px solid #FFD700; padding: 2em 3em; max-width: 800px; box-shadow: 0 0 30px rgba(255, 215, 0, 0.5); border-radius: 5px; }
        h1 { font-family: 'Cinzel', serif; color: #FFD700; text-transform: uppercase; letter-spacing: 3px; font-size: 2.5em; border-bottom: 2px solid #DAA520; padding-bottom: 10px; margin-bottom: 20px; }
        p { font-size: 1.2em; line-height: 1.6; }
        .flag { background-color: #1a1a1a; border: 2px dashed #DAA520; padding: 15px; margin-top: 25px; font-size: 1.3em; color: #90EE90; font-family: 'Courier New', Courier, monospace; word-wrap: break-word; }
    </style>
</head>
<body> <div class="container"> <h1>Acceso Concedido, Administrador</h1> <p>Has doblegado el tiempo y demostrado ser digno de la sabiduría de Minerva. La infraestructura del Imperio está a tu disposición.</p> <p>El Fragmento de Sabiduría Ancestral es:</p> <div class="flag"><strong>{{ flag }}</strong></div> </div> </body>
</html>
"""

@app.route('/')
def foro():
    # Obtenemos la hora actual del servidor EN CADA PETICIÓN
    current_server_time = int(time.time())

    # Intentamos leer la cookie que nos envía el jugador
    try:
        user_session_id = int(request.cookies.get('session_id'))
    except (TypeError, ValueError):
        # Si el jugador no tiene cookie, le asignamos una con la hora actual
        user_session_id = current_server_time

    # --- LA LÓGICA CLAVE Y CORREGIDA ---
    # Calculamos la diferencia entre la hora actual y la cookie del jugador
    time_difference = current_server_time - user_session_id

    # Comprobamos si la diferencia está "cerca" de 1 hora (3600 segundos)
    # Damos un margen de 5 minutos (300 segundos) para evitar problemas de sincronización
    if 3300 <= time_difference <= 3900:  # ¿Está entre 55 y 65 minutos en el pasado?
        # Si es así, es el administrador
        resp = make_response(render_template_string(template_admin, flag=FLAG))
    else:
        # Si no, es un usuario normal
        resp = make_response(render_template_string(template_normal, session_id=user_session_id))
    
    # Le devolvemos al usuario su cookie para que la vea
    resp.set_cookie('session_id', str(user_session_id))
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)